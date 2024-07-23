import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import resample
import joblib

app = Flask(__name__)

# Load and preprocess data
data = pd.read_csv('amazon_reviews.csv')

# Remove any rows with NaN values in 'reviews.text' or 'reviews.rating'
data = data.dropna(subset=['reviews.text', 'reviews.rating'])

# Convert ratings to sentiment
data['sentiment'] = (data['reviews.rating'] > 3).astype(int)

# Separate majority and minority classes
data_majority = data[data['sentiment'] == 1]
data_minority = data[data['sentiment'] == 0]

# Upsample minority class
data_minority_upsampled = resample(data_minority, 
                                   replace=True,     # sample with replacement
                                   n_samples=len(data_majority),    # to match majority class
                                   random_state=42)  # reproducible results

# Combine majority class with upsampled minority class
data_balanced = pd.concat([data_majority, data_minority_upsampled])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    data_balanced['reviews.text'], 
    data_balanced['sentiment'], 
    test_size=0.2, 
    random_state=42,
    stratify=data_balanced['sentiment']
)

# Create and train the model
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

classifier = MultinomialNB(alpha=0.1)  # Lowering alpha for less smoothing
classifier.fit(X_train_vectorized, y_train)

# Save the model and vectorizer
joblib.dump(classifier, 'sentiment_model.joblib')
joblib.dump(vectorizer, 'vectorizer.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    vectorized_review = vectorizer.transform([review])
    prediction = classifier.predict(vectorized_review)
    probabilities = classifier.predict_proba(vectorized_review)[0]
    confidence = max(probabilities)
    sentiment = 'Positive' if prediction[0] == 1 else 'Negative'
    return jsonify({'sentiment': sentiment, 'confidence': float(confidence)})

@app.route('/evaluate')
def evaluate():
    y_pred = classifier.predict(X_test_vectorized)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return jsonify({'accuracy': accuracy, 'report': report})

if __name__ == '__main__':
    app.run(debug=True)