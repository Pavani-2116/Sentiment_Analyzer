function analyzeSentiment() {
    const text = document.getElementById('textInput').value;
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = "Prediction: " + data.prediction;
    })
    .catch(error => {
        document.getElementById('result').innerText = "Error analyzing sentiment.";
    });
}
