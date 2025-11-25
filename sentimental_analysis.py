import pandas as pd
from ingest_data import connect_to_db

db_name = "proj_data_analysis"
user = "postgres"

def main(db_name, user):
    engine = connect_to_db(db_name, user)
    sql_query = "SELECT review_id, content FROM raw_reviews"
    try:
        df_to_analyze = pd.read_sql(sql_query, engine)
        print(df_to_analyze)
        return df_to_analyze
    except Exception as e:
        print(f"An error occurred while processing the query: {e}")

if __name__ == "__main__":
    main(db_name, user)