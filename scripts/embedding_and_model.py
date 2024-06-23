# scripts/embedding_and_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train_logistic_regression_model(data_path, model_dir):
    reviews_data = pd.read_csv(data_path)

    # Ensure there are no NaN values
    reviews_data['Processed_Review'] = reviews_data['Processed_Review'].fillna('')

    # Split Data 80/20
    X_train, X_test, y_train, y_test = train_test_split(
        reviews_data['Processed_Review'], reviews_data['Rating'], test_size=0.2, random_state=42)

    # Vectorization and TF-IDF
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Model initialization and training
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train_tfidf, y_train)

    # Save model and vectorizer
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(model, os.path.join(model_dir, 'logistic_regression_model.pkl'))
    joblib.dump(vectorizer, os.path.join(model_dir, 'tfidf_vectorizer.pkl'))

    # Ensure the data directory exists
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)

    # Save embeddings in binary format
    joblib.dump(X_train_tfidf, os.path.join(data_dir, 'embeddings.pkl'))

    # Evaluate model
    y_pred = model.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    print(f"Model Accuracy: {accuracy}")
    print("Classification Report:\n", report)

if __name__ == "__main__":
    data_path = '/Users/anthonykhaiat/Desktop/Weaviate/weaviate-ml-workflow/data/processed_reviews.csv'
    model_dir = './model_directory'
    train_logistic_regression_model(data_path, model_dir)
