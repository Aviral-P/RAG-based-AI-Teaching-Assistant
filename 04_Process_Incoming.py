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

def inference(prompt):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen3:8b",
            "prompt": prompt,
            "stream": False
        }
    )
    response = r.json()
    print(response)
    return response

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

prompt = f'''
Here are video subtitle chunks containing video title,
video number, start time in seconds, end time in seconds,
the text at that time :

{new_df[["title","number","start","end","text"]].to_json(orient="records")}

--------------------

"{incoming_query}"

User asked this question related to the video chunks,
you have to answer in human way(don't mention the above format,
its just for you) where and how much content is mentioned in which
video (in which video and at what timestamp) and guide the user
to go to that particular video.

If user askes unrelated question, tell him that you can only
answer questions related to the data.
'''

with open("prompt.txt", "w") as f:
    f.write(prompt)
    
    
response = inference(prompt)["response"]
print(response)


with open("response.txt", "w") as f:
    f.write(response)