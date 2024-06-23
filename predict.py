import sys
import joblib
import json

def load_model_and_vectorizer(model_path, vectorizer_path):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer

def predict(query, model, vectorizer):
    X = vectorizer.transform([query])
    prediction = model.predict(X)
    # Convert numpy int64 to Python int
    return int(prediction[0])  

if __name__ == "__main__":
    model_path = "model_directory/logistic_regression_model.pkl"
    vectorizer_path = "model_directory/tfidf_vectorizer.pkl"
    query = sys.argv[1]
    
    model, vectorizer = load_model_and_vectorizer(model_path, vectorizer_path)
    prediction = predict(query, model, vectorizer)
    
    result = {"rating": prediction}
    print(json.dumps(result))
