from training_data import training_examples
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib


# =========================
# STEP 1: EXTRACT TEXTS
# =========================

texts = [example["text"] for example in training_examples]


# =========================
# STEP 2: EXTRACT LABELS
# =========================

labels = [example["label"] for example in training_examples]


# =========================
# STEP 3: CREATE TF-IDF VECTORIZER
# =========================

vectorizer = TfidfVectorizer()

# Convert text into vectors
X = vectorizer.fit_transform(texts)


# =========================
# STEP 4: TRAIN MODEL
# =========================

model = LogisticRegression()

model.fit(X, labels)


# =========================
# SAVE MODEL + VECTORIZER
# =========================

joblib.dump(model, "error_classifier_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("Model and vectorizer saved successfully.\n")


# =========================
# LOAD SAVED MODEL ONCE
# =========================

model = joblib.load("error_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


# =========================
# CLASSIFY FUNCTION
# =========================

def classify(error_text: str) -> dict:
    # Convert input text to vector
    vector = vectorizer.transform([error_text])

    # Predict category
    prediction = model.predict(vector)[0]

    # Get confidence score
    probabilities = model.predict_proba(vector)[0]
    confidence = max(probabilities)

    # Return result
    return {
        "category": prediction,
        "confidence": float(confidence)
    }


# =========================
# TEST classify()
# =========================

result = classify("ZeroDivisionError: division by zero")

print(f"Category: {result['category']}")
print(f"Confidence: {result['confidence']}")