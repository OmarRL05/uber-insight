import pandas as pd
import os
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

data = ingest_data('../dataset/uber_reviews_without_reviewid.csv')
df = pd.DataFrame(data)
print(df.head())  # Display the first few rows of the DataFrame