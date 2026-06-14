# Databricks notebook source
from pyspark.sql.functions import col, expr, lit, current_timestamp
from functools import reduce

df_high = spark.table("spotify_catalog.bronze.high_popularity_spotify_data_raw")
df_low = spark.table("spotify_catalog.bronze.low_popularity_spotify_data_raw")


def create_silver_table(df):
    excluded = [
        "analysis_url",
        "key",
        "mode",
        "playlist_id",
        "track_album_id",
        "track_href",
        "track_id",
        "uri"
    ]

    selected_columns = sorted([
        c for c in df.columns if c not in excluded
    ])

    return (
        df
        .select(*selected_columns)
        .dropDuplicates()
    )


columns_to_cast = {
    "acousticness": "double",
    "danceability": "double",
    "duration_ms": "int",
    "energy": "double",
    "id": "string",
    "instrumentalness": "double",
    "liveness": "double",
    "loudness": "double",
    "playlist_genre": "string",
    "playlist_name": "string",
    "playlist_subgenre": "string",
    "speechiness": "double",
    "tempo": "double",
    "time_signature": "int",
    "track_album_name": "string",
    "track_album_release_date": "date",
    "track_artist": "string",
    "track_name": "string",
    "track_popularity": "int",
    "type": "string",
    "valence": "double"
}


def apply_types_with_errors(df, category):
    df_typed = df.withColumn("category", lit(category))

    for column_name, data_type in columns_to_cast.items():
        df_typed = (
            df_typed
            .withColumn(f"{column_name}_original", col(column_name))
            .withColumn(column_name, expr(f"try_cast({column_name} as {data_type})"))
        )

    error_conditions = [
        (col(f"{column_name}_original").isNotNull()) &
        (col(column_name).isNull())
        for column_name in columns_to_cast.keys()
    ]

    has_error = reduce(lambda a, b: a | b, error_conditions)

    df_errors = (
        df_typed
        .filter(has_error)
        .withColumn("error_date", current_timestamp())
    )

    original_columns = [
        f"{column_name}_original"
        for column_name in columns_to_cast.keys()
    ]

    df_clean = df_typed.drop(*original_columns)

    return df_clean, df_errors


df_high_silver, df_high_errors = apply_types_with_errors(
    create_silver_table(df_high),
    "high"
)

df_low_silver, df_low_errors = apply_types_with_errors(
    create_silver_table(df_low),
    "low"
)


df_all = df_high_silver.unionByName(df_low_silver)
df_all_errors = df_high_errors.unionByName(df_low_errors)


df_all.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("spotify_catalog.silver.spotify_tracks")


df_all_errors.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("spotify_catalog.silver.spotify_tracks_errors")


display(df_all)
display(df_all_errors)