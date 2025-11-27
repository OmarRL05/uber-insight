from ingest_data import connect_to_db
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import nltk

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

def vader(df):
    sia = SentimentIntensityAnalyzer()
    df["sentimental_rate"] = df["content"].apply(lambda review: sia.polarity_scores(review)['compound'])
    return df

def classify_reviews(text):
    kw_app = [word.lower() for word in ["app", "helpful", "user friendly", "facilities", "application", "supportive"]]
    kw_finance = [word.lower() for word in ["charged", "pay", "payment", "money", "extra money"]]
    kw_trip = [word.lower() for word in ["service", "trip", "excelent", "safest", "waiting", "driver", "ride", "pickup"]]
    
    text = text.lower()    

    if set(text.split()) & set(kw_app):
        return "App/Technical"
    elif set(text.split()) & set(kw_finance):
        return "Finances"
    elif set(text.split()) & set(kw_trip):
        return "Trip"
    else:
        return "General"

def classify_sentiment(score):
    if (score >= 0.9) :
        return "Very Satisfied"
    elif (score >= 0.04):
        return "Satisfied"
    elif (score <= (-0.9)):
        return "Very Unsatisfied"
    elif (score <= (-0.4)):
        return "Unsatisfied"
    else:
        return "Neutral"

if __name__ == "__main__":
    df_to_analyze = main(db_name, user)
    df = vader(df_to_analyze)
    df["category"] = df["content"].apply(lambda x: classify_reviews(x))
    df["Sentiment"] = df["sentimental_rate"].apply(lambda x: classify_sentiment(x))
    print(df)