import pandas as pd
import os
import psycopg2 as pg
from sqlalchemy import create_engine

url = '../dataset/uber_reviews_without_reviewid.csv'
db_name = "proj_data_analysis"
user = "postgres"
raw_name = "raw_reviews"

def connect_to_db(db_name, user, password="", host='localhost', port='5432'):
    """
    Establish a connection to the PostgreSQL database.

    Parameters:
    db_name (str): The name of the database.
    user (str): The database user.
    password (str): The password for the database user.
    host (str): The host of the database. Default is 'localhost'.
    port (str): The port of the database. Default is '5432'.

    Returns:
    connection: A connection object to the PostgreSQL database.
    """
    try:
        engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}")
        print("Connection to PostgreSQL established successfully.")
        return engine
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None

def ingest_data(file_path):
    """
    Ingest data from a CSV file and return a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The ingested data as a DataFrame.
    """
    print(f"Ingesting data from {file_path}...")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    try:
        data = pd.read_csv(file_path)
        print(f"Data ingested successfully from {file_path}.")
        return data
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the CSV file: {e}")


def raw_to_db(data, engine, sql_table, if_case="replace"):
    data.to_sql(sql_table, engine, if_exists=if_case, index=False)
    return

def main():
    engine = connect_to_db(db_name, user)
    data = ingest_data(url)
    raw_to_db(data, engine, raw_name)

if __name__ == "__main__":
    main()