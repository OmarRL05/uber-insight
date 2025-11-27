from ingest_data import connect_to_db
import pandas as pd

engine = connect_to_db("proj_data_analysis", "postgres")
query = "SELECT * FROM final_dashboard"
df = pd.read_sql(query, engine)
df.to_csv("uber_analytics.csv", index=False)