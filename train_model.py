import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

# Sample dataset
data = {
    'text': [
        'I love this product', 'This is a great service',
        'I hate this', 'This is bad', 'I am very happy',
        'I am disappointed', 'Not good', 'Very enjoyable experience',
        'Worst experience', 'Amazing job'
    ],
    'label': ['positive', 'positive', 'negative', 'negative', 'positive',
              'negative', 'negative', 'positive', 'negative', 'positive']
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

model = MultinomialNB()
model.fit(X, y)

os.makedirs('model', exist_ok=True)
pickle.dump(model, open('model/sentiment_model.pkl', 'wb'))
pickle.dump(vectorizer, open('model/vectorizer.pkl', 'wb'))
