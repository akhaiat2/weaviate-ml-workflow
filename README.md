# Weaviate Machine Learning Workflow

This project demonstrates a simple machine learning workflow that integrates with Weaviate. The workflow involves preprocessing text data, training a logistic regression model, and using the model to predict ratings for user input.

## Project Structure

```plaintext
weaviate-ml-workflow/
├── .next/
├── components/
│   └── Search.js
├── data/
│   ├── embeddings.csv
│   ├── embeddings.pkl
│   ├── processed_reviews.csv
│   ├── Raw_Reviews.csv
├── model_directory/
│   ├── logistic_regression_model.pkl
│   └── tfidf_vectorizer.pkl
├── node_modules/
├── pages/
│   ├── api/
│   │   ├── getRating.js
│   │   ├── search.js
│   ├── _app.js
│   ├── index.js
├── scripts/
│   ├── embedding_and_model.py
│   ├── weaviate_integration.py
├── styles/
│   └── globals.css
├── .gitignore
├── package.json
├── package-lock.json
├── postcss.config.js
├── README.md
├── requirements.txt
├── tailwind.config.js

Steps to start:
1. To clone the repo: git clone https://github.com/yourusername/weaviate-ml-workflow.git
cd weaviate-ml-workflow
2. Install Node.js dependencies: npm install
3. Install Python dependencies: pip install -r requirements.txt
4. Run project: npm run dev
5. Launch on http://localhost:3000

