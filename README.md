# Uber Insight: End-to-End Sentiment Analysis & ETL Pipeline
End-to-End Sentiment Analysis Pipeline for Product Insights. This project implements a complete data pipeline using Pandas, SQLAlchemy, NLP to ingest and classify Uber customer reviews into PostgreSQL. Features ML sentiment analysis to categorize feedback (UX/UI, Finance, Service) and a Tableau dashboard for visualizing actionable product insights.

This project implements a complete End-to-End Data Pipeline to analyze Uber customer reviews. It combines robust Data Engineering practices with Natural Language Processing (NLP) to transform raw text data into actionable product insights.

## Project Objective

To transform 12,000+ raw user reviews into a Business Intelligence dashboard that enables Product Managers to identify:

Version Friction: Detect if a specific app update caused a drop in user satisfaction.

Root Cause Analysis: Automatically classify feedback into key operational areas (App/Technical, Finances, Trip).

Sentiment Evolution: Visualize temporal trends in customer satisfaction using Machine Learning.

## Pipeline Architecture

The data flow follows a modern ETL architecture:

```
graph LR
A[CSV Raw Data] -->|Ingestion (ingest_data.py)| B[(PostgreSQL DB)]
B -->|Extraction & NLP| C(sentimental_analysis.py)
C -->|Classification & Scoring| D[(PostgreSQL DB)]
D -->|SQL View Integration| E(to_csv.py)
E -->|Export CSV| F[Tableau Dashboard]
```
### Tech Stack

- Language: Python (Pandas, NumPy)
- Database: PostgreSQL (Schema Design, Views, Constraints)
- Connectivity: SQLAlchemy, Psycopg2
- AI/NLP: NLTK (VADER Sentiment Analysis)
- Visualization: Tableau Public 📊

### Key Features

1. Data Engineering (ETL)
  - Robust Ingestion: Python scripts designed to handle bulk data loads from CSV to SQL.
  - Relational Schema: Implementation of Primary Keys and Foreign Keys to ensure data integrity between raw and analyzed data.
  - SQL Views: Usage of CREATE OR REPLACE VIEW to abstract complex joins, facilitating data extraction for the dashboard.

2. Natural Language Processing (AI)
  - Sentiment Scoring: Utilization of NLTK's VADER lexicon to calculate compound scores and map them to 5 distinct labels (from `Very Satisfied` to `Very Unsatisfied`).
  - Text Classification: Logic-based algorithm using keyword set intersection to categorize reviews into:
    - App/Technical: Issues related to UI, login, location, and app performance.
    - Finances: Issues related to payments, pricing, and extra charges.
    - Trip: Issues related to driver behavior, safety, and ride quality.

3. Business Intelligence
  - Tableau Dashboard: Interactive visualization featuring dynamic filters and dual-axis charts to monitor satisfaction averages across different app versions.

## Installation & Usage
### Prerequisites

  - Python 3.10+
  - PostgreSQL installed and running locally.

### Steps

1. Clone the repository
```
git clone [https://github.com/omarrl05/uber-insight.git](https://github.com/omarrl05/uber-insight.git)
cd uber-insight
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Database Setup
  Ensure you have a PostgreSQL database created (default: proj_data_analysis) and update the connection credentials in the scripts if necessary.

4. Run the Pipeline
  Step 1: Ingest Raw Data -> Loads the raw CSV data into the raw_reviews table.
  ```
  python ingest_data.py
  ```

  Step 2: Analyze Sentiment -> Extracts data, applies VADER analysis and classification logic, and loads results into analyzed_reviews.
  ```
  python sentimental_analysis.py
  ```

  Step 3: Export Data -> Queries the SQL View final_dashboard and generates the uber_analytics.csv file for Tableau.
  ```
  python to_csv.py
  ```

## Project Structure

  `ingest_data.py:` Handles database connection and initial ingestion of raw data.
  
  `sentimental_analysis.py:` Core logic script. performs NLP analysis, classification, and database updates.
  
  `to_csv.py:` Utility script to export the processed SQL view to a CSV file.
  
  `requirements.txt:` List of required Python packages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Developed by Omar Reyes as part of a Data Engineering & Analytics portfolio.
