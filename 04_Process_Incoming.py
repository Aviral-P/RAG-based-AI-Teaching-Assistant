import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import requests

def create_embedding(text_list):
    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "bge-m3",
            "input": text_list
        }
    )
    embedding = r.json()["embeddings"]
    return embedding




df = joblib.load("embeddings.joblib")

incoming_query = input("Ask a question: ")

question_embedding = create_embedding([incoming_query])[0]

similarities = cosine_similarity(
    np.vstack(df["embeddings"]),
    [question_embedding]
).flatten()

top_results = 5

max_index = similarities.argsort()[::-1][0:top_results]

new_df = df.loc[max_index]
