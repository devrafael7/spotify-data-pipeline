# 🎵 Spotify Data Pipeline

## 📖 Overview

This project demonstrates a complete Data Engineering pipeline built using Databricks, PySpark, SQL, Delta Lake, and Workflow Scheduling.

The dataset contains Spotify track information and audio features commonly used in Data Science and Machine Learning projects, including:

* Acousticness
* Danceability
* Energy
* Instrumentalness
* Liveness
* Loudness
* Speechiness
* Tempo
* Valence
* Popularity
* Genre
* Artist Information

The pipeline follows the Medallion Architecture pattern:

```text
Raw Data
   ↓
Bronze Layer
   ↓
Silver Layer
   ↓
Gold Layer
```

---

# 🏗️ Architecture

```text
CSV Files
    ↓
Bronze Layer
    ↓
Silver Layer
    ├── Data Type Validation
    ├── Duplicate Removal
    ├── Data Quality Checks
    └── Error Table
    ↓
Gold Layer
    ├── Genre Summary
    ├── Category Summary
    └── Track Summary
    ↓
Analytics & BI
```

---

# ⚙️ Technologies Used

| Technology           | Purpose                  |
| -------------------- | ------------------------ |
| Databricks           | Data Platform            |
| PySpark              | Data Processing          |
| SQL                  | Analytics & Aggregations |
| Delta Lake           | Data Storage             |
| GitHub               | Version Control          |
| Databricks Workflows | Pipeline Orchestration   |

---

# 🥉 Bronze Layer

The Bronze Layer stores raw Spotify data exactly as received from source files.

### Source Files

* High Popularity Tracks
* Low Popularity Tracks

### Characteristics

* Raw ingestion
* Minimal transformations
* Original schema preservation
* Historical data retention

---

# 🥈 Silver Layer

The Silver Layer applies cleansing, validation, and standardization rules.

### Transformations

✅ Removed unnecessary columns

✅ Removed duplicates

✅ Standardized data types

✅ Added category classification

✅ Created unified dataset

### Data Type Conversions

Examples:

```python
acousticness → DOUBLE
danceability → DOUBLE
duration_ms → INT
track_popularity → INT
track_album_release_date → DATE
```

### Data Quality Process

Invalid values are automatically converted using:

```python
try_cast()
```

Example:

| Original Value | Expected Type | Result |
| -------------- | ------------- | ------ |
| 0.89           | DOUBLE        | Valid  |
| 1.2E-05        | DOUBLE        | Valid  |
| abc            | DOUBLE        | NULL   |

---

# 🚨 Error Handling

Records containing invalid values are redirected to a dedicated error table.

### Error Table

```text
spotify_tracks_errors
```

Captured information:

* Original values
* Invalid columns
* Category source
* Error timestamp

Benefits:

* Data lineage
* Quality monitoring
* Easier debugging
* Auditability

---

# 🥇 Gold Layer

The Gold Layer contains business-ready datasets optimized for analytics and dashboards.

## Genre Summary

Aggregated metrics by music genre.

Examples:

* Average Popularity
* Average Energy
* Average Danceability
* Track Count

---

## Category Summary

Comparison between:

```text
High Popularity
Low Popularity
```

Metrics include:

* Total Tracks
* Average Popularity
* Average Energy
* Average Valence

---

## Track Summary

Track-level curated dataset ready for consumption by analytics tools.

---

# 🔄 Workflow Automation

The entire pipeline is orchestrated through Databricks Workflows.

Execution sequence:

```text
00_setup
    ↓
01_bronze
    ↓
02_silver
    ↓
03_gold
```

### Scheduling

* Automated Daily Execution
* Dependency Control
* End-to-End Processing

---

# 📊 Potential Use Cases

This dataset can be used for:

* Data Engineering Practice
* Machine Learning Projects
* Music Analytics
* Popularity Prediction Models
* Feature Engineering
* Dashboard Development
* Exploratory Data Analysis (EDA)

---

# 📈 Future Improvements

Planned enhancements:

* Incremental Loads
* Data Quality Metrics Dashboard
* ML Popularity Prediction Model
* Power BI Integration
* CI/CD Deployment
* Cloud Storage Integration (GCP)

---

# 📂 Repository Structure

```text
spotify-data-pipeline
│
├── README.md
│
├── notebooks
│   ├── 00_setup.py
│   ├── 01_bronze.py
│   ├── 02_silver.py
│   └── 03_gold.sql
│
├── screenshots
│   ├── workflow.png
│   ├── bronze.png
│   ├── silver.png
│   └── gold.png
│
└── diagrams
    └── architecture.png
```

---

# 👨‍💻 Author

Rafael Oliveira

Data Engineering | Databricks | PySpark | SQL | Power BI
