from flask import Flask, render_template, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download once if not already done
nltk.download('vader_lexicon')

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.05:
        sentiment = '😊 Positive'
    elif compound <= -0.05:
        sentiment = '😠 Negative'
    else:
        sentiment = '😐 Neutral'
    return jsonify({'result': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
