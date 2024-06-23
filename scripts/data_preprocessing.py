import pandas as pd
import nltk as ltk
from nltk.stem import WordNetLemmatizer
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Download necessary NLTK data
ltk.download('wordnet')
ltk.download('vader_lexicon')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = ' '.join([word for word in text.split() if word not in ENGLISH_STOP_WORDS])
    lemmatizer = WordNetLemmatizer()
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
    return text

def load_and_preprocess_data(file_path):
    reviews_data = pd.read_csv(file_path)
    reviews_data['Processed_Review'] = reviews_data['Text_Review'].astype(str).apply(preprocess_text)
    reviews_data.fillna({'Title': 'No Title', 'Text_Review': '', 'Processed_Review': ''}, inplace=True)
    return reviews_data

if __name__ == "__main__":
    file_path = '/Users/anthonykhaiat/Desktop/Weaviate/weaviate-ml-workflow/data/Raw_Reviews.csv'  # Path to your CSV file
    output_path = '/Users/anthonykhaiat/Desktop/Weaviate/weaviate-ml-workflow/data/processed_reviews.csv'
    reviews_data = load_and_preprocess_data(file_path)
    reviews_data.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")
