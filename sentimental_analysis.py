from ingest_data import connect_to_db
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import nltk

db_name = "proj_data_analysis"
user = "postgres"
table_name = "analyzed_reviews"

kw_app = [word.lower() for word in ["app", "helpful", "user friendly", "facilities", "application", "supportive", "Customer", "location", "rates", "promos", "loggin"]]
kw_finance = [word.lower() for word in ["charged", "pay", "payment", "money", "extra money", "price", "inflated", "pricing", "extortion", "paying", "expensive", "cheap", "charge"]]
kw_trip = [word.lower() for word in ["service", "trip", "excelent", "safest", "waiting", "driver", "ride", "pickup", "travel", "car", "bike", "services"]]

def main(db_name, user):
    engine = connect_to_db(db_name, user)
    sql_query = "SELECT review_id, content FROM raw_reviews"
    try:
        df_to_analyze = pd.read_sql(sql_query, engine)
        return df_to_analyze, engine
    except Exception as e:
        print(f"An error occurred while processing the query: {e}")

def vader(df):
    sia = SentimentIntensityAnalyzer()
    df["confidence"] = df["content"].apply(lambda review: sia.polarity_scores(review)['compound'])
    return df

def classify_reviews(text):
    text = text.lower()    

    if set(text.split()) & set(kw_app):
        return "App/Technical"
    elif set(text.split()) & set(kw_finance):
        return "Finances"
    elif set(text.split()) & set(kw_trip):
        return "Trip"
    else:
        return "General"

def classify_sentiment(df):
    bins = [-1.0, -0.9, -0.4, 0.4, 0.9, 1.0]
    labels = ["Very Unsatisfied", "Unsatisfied", "Neutral", "Satisfied", "Very Satisfied"]
    df["sentiment"] = pd.cut(df["confidence"], bins=bins, labels=labels)
    return df

def send_to_db(df, engine, sql_table, if_case="replace"):
    df.to_sql(sql_table, engine, if_exists=if_case, index=False)
    return

if __name__ == "__main__":
    df_to_analyze, engine = main(db_name, user)
    df = vader(df_to_analyze)
    df_to_analyze["category"] = df_to_analyze["content"].apply(lambda x: classify_reviews(x))
    df = classify_sentiment(df)
    send_to_db(df[["review_id", "sentiment", "confidence", "category"]], engine, table_name)
