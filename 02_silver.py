-- Databricks notebook source
CREATE OR REPLACE TABLE spotify_catalog.gold.track_summary AS

SELECT
    category,
    COUNT(*) AS total_tracks,
    AVG(acousticness) AS avg_acousticness,
    AVG(danceability) AS avg_danceability,
    AVG(energy) AS avg_energy,
    AVG(instrumentalness) AS avg_instrumentalness,
    AVG(liveness) AS avg_liveness,
    AVG(loudness) AS avg_loudness,
    AVG(speechiness) AS avg_speechiness,
    AVG(tempo) AS avg_tempo,
    AVG(time_signature) AS avg_time_signature,
    AVG(track_popularity) AS avg_track_popularity,
    AVG(valence) AS avg_valence
FROM spotify_catalog.silver.spotify_tracks
GROUP BY category
ORDER BY category ASC;

SELECT * FROM
spotify_catalog.gold.track_summary


-- COMMAND ----------

CREATE OR REPLACE TABLE spotify_catalog.gold.genre_summary AS

SELECT
    playlist_genre,
    COUNT(*) AS total_tracks,
    AVG(track_popularity) AS avg_popularity,
    AVG(energy) AS avg_energy,
    AVG(danceability) AS avg_danceability
FROM spotify_catalog.silver.spotify_tracks
GROUP BY playlist_genre;

SELECT * FROM
spotify_catalog.gold.genre_summary

-- COMMAND ----------

CREATE OR REPLACE TABLE spotify_catalog.gold.music_dashboard AS

SELECT
    category,
    playlist_genre,

    COUNT(*) AS total_tracks,

    ROUND(
        AVG(track_popularity),
        2
    ) AS avg_popularity,

    ROUND(
        AVG(danceability),
        2
    ) AS avg_danceability,

    ROUND(
        AVG(energy),
        2
    ) AS avg_energy,

    ROUND(
        AVG(valence),
        2
    ) AS avg_valence

FROM spotify_catalog.silver.spotify_tracks

GROUP BY
    category,
    playlist_genre;

SELECT * FROM
spotify_catalog.gold.music_dashboard;