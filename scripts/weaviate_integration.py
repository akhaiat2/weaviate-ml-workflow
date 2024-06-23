import os
import weaviate
import pandas as pd
import joblib
import numpy as np

def connect_weaviate():
    return weaviate.Client("http://localhost:8080")

def load_data(file_path):
    return pd.read_csv(file_path)

def load_embeddings(file_path):
    return joblib.load(file_path)

def store_data(client, data, embeddings):
    for text, embedding in zip(data, embeddings):
        # Handle NaN values in embeddings
        embedding_array = embedding.toarray().flatten()
        if np.isnan(embedding_array).any():
            embedding_array = np.nan_to_num(embedding_array)  # Replace NaN with zero

        properties = {
            "text": text,
            "embedding": embedding_array.tolist()  # Convert to list of floats
        }
        try:
            client.data_object.create(properties, "Article")
        except Exception as e:
            print(f"Error storing data: {e}")
            continue

if __name__ == "__main__":
    client = connect_weaviate()
    data = load_data('/Users/anthonykhaiat/Desktop/Weaviate/weaviate-ml-workflow/data/processed_reviews.csv')['Processed_Review']
    embeddings = load_embeddings('/Users/anthonykhaiat/Desktop/Weaviate/weaviate-ml-workflow/data/embeddings.pkl')
    
    store_data(client, data, embeddings)
    
    print("Data and embeddings stored in Weaviate")
