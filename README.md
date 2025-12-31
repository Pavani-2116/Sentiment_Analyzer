# Sentiment Analyzer

A Python-based Machine Learning and Natural Language Processing (NLP) application that classifies input text into **Positive**, **Negative**, or **Neutral** sentiment. This project demonstrates an end-to-end ML workflow including data preprocessing, feature extraction, model training, evaluation, and prediction.

---

## Project Overview

Sentiment analysis is widely used to understand opinions and emotions expressed in text data such as reviews, feedback, and social media posts.  
This project processes raw text data, extracts meaningful features using TF-IDF vectorization, and applies supervised machine learning algorithms to predict sentiment accurately.

---

## Objectives

- Learn text preprocessing techniques in NLP  
- Implement TF-IDF based feature extraction  
- Train and evaluate a supervised ML model  
- Build a scalable and reusable sentiment analysis system  
- Gain hands-on experience with real-world ML pipelines  

---

## Features

- Text preprocessing and cleaning  
- TF-IDF feature extraction  
- Supervised sentiment classification  
- Supports Positive, Negative, and Neutral labels  
- Modular and easy-to-understand code structure  

---

## Workflow

1. Input text is provided by the user  
2. Text is cleaned and preprocessed  
3. TF-IDF converts text into numerical features  
4. Machine learning model predicts sentiment  
5. Output sentiment is displayed  

---

## Technologies Used

### Programming Language
- Python

### Libraries
- scikit-learn  
- NLTK  
- Pandas  
- NumPy  

### Optional (UI / Deployment)
- Flask / Streamlit  

---

## Project Structure

Sentiment_Analyzer/
│
├── app.py # Main application file
├── train_model.py # Model training script
├── model/ # Saved trained models
├── data/ # Dataset files
├── static/ # Static assets (if applicable)
├── templates/ # HTML templates (if Flask)
├── requirements.txt # Project dependencies
└── README.md # Project documentation


---

## Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/Pavani-2116/Sentiment_Analyzer.git
cd Sentiment_Analyzer
Install Dependencies
pip install -r requirements.txt

Run the Application
python app.py

Example Predictions
Input Text	Sentiment
I love this product	Positive
This is the worst experience	Negative
The service was average	Neutral
Model Information

Feature Extraction: TF-IDF Vectorization

Learning Type: Supervised Machine Learning

Evaluation Metrics: Accuracy, Precision, Recall, F1-score

Key Learnings

Natural Language Processing fundamentals

Feature engineering using TF-IDF

Training and evaluating ML classification models

Writing clean and maintainable Python code

Understanding end-to-end ML workflows

Future Enhancements

Deploy application using Streamlit or Flask

Improve accuracy using advanced preprocessing

Add deep learning models (LSTM / Transformers)

Support multilingual sentiment analysis

Add visual analytics dashboard

Author

Pavani Mada
GitHub: https://github.com/Pavani-2116

LinkedIn: https://linkedin.com/in/pavani-mada

License

This project is created for educational and portfolio purposes.
