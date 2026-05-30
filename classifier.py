from training_data import training_examples
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib


def load_or_train_classifier():
    try:
        model = joblib.load("error_classifier_model.pkl")
        vectorizer = joblib.load("tfidf_vectorizer.pkl")
    except FileNotFoundError:
        texts = [ex["text"] for ex in training_examples]
        labels = [ex["label"] for ex in training_examples]
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(texts)
        model = LogisticRegression()
        model.fit(X, labels)
        joblib.dump(model, "error_classifier_model.pkl")
        joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
    return model, vectorizer


model, vectorizer = load_or_train_classifier()


def classify(error_text: str) -> dict:
    vector = vectorizer.transform([error_text])
    prediction = model.predict(vector)[0]
    probabilities = model.predict_proba(vector)[0]
    confidence = max(probabilities)
    return {
        "category": prediction,
        "confidence": float(confidence)
    }