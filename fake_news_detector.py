# fake_news_detector_ui.py
from flask import Flask, request, render_template_string
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# -----------------------------
# Load and preprocess dataset
# -----------------------------
fake_df = pd.read_csv('Fake.csv')
true_df = pd.read_csv('True.csv')

fake_df['label'] = 'FAKE'
true_df['label'] = 'REAL'

df = pd.concat([fake_df[['title', 'label']], true_df[['title', 'label']]], ignore_index=True)

X_train, X_test, y_train, y_test = train_test_split(df['title'], df['label'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

# -----------------------------
# HTML Template with Bootstrap
# -----------------------------
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fake News Detector</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f8f9fa; }
        .container { max-width: 700px; margin-top: 50px; }
        textarea { resize: none; }
        .result { margin-top: 20px; font-size: 1.3rem; font-weight: bold; }
        .progress { height: 30px; }
    </style>
</head>
<body>
<div class="container">
    <h1 class="text-center mb-4">Fake News Detector</h1>
    <form method="POST">
        <div class="mb-3">
            <textarea class="form-control" name="news" placeholder="Enter news title here..." rows="5">{{ news_text }}</textarea>
        </div>
        <div class="d-grid">
            <button type="submit" class="btn btn-primary btn-lg">Check News</button>
        </div>
    </form>

    {% if result %}
    <div class="result text-center mt-4">
        Result: <span class="{{ 'text-danger' if result=='FAKE' else 'text-success' }}">{{ result }}</span>
    </div>
    <div class="progress mt-2">
        <div class="progress-bar {{ 'bg-danger' if result=='FAKE' else 'bg-success' }}" role="progressbar" style="width: {{ probability }}%;" aria-valuenow="{{ probability }}" aria-valuemin="0" aria-valuemax="100">{{ probability }}%</div>
    </div>
    {% endif %}
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

# -----------------------------
# Flask Route
# -----------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    probability = ''
    news_text = ''
    if request.method == 'POST':
        news_text = request.form['news']
        if news_text.strip():
            news_vec = vectorizer.transform([news_text])
            prediction = model.predict(news_vec)[0]
            prob = model.predict_proba(news_vec).max() * 100
            result = prediction
            probability = f"{prob:.2f}"
    return render_template_string(html_template, result=result, probability=probability, news_text=news_text)

# -----------------------------
# Run App
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
