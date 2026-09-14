import os
import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils.class_weight import compute_sample_weight
from xgboost import XGBClassifier


MODEL_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models"
)

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "severity_xgboost.pkl"
)

VECTORIZER_PATH = os.path.join(
    MODEL_DIR,
    "severity_tfidf.pkl"
)

LABELS_PATH = os.path.join(
    MODEL_DIR,
    "severity_labels.pkl"
)


def train_severity_model():

    train_df = pd.read_csv("data/train.csv")
    test_df = pd.read_csv("data/test.csv")

    X_train_text = train_df["Complaint_Description"].astype(str)
    X_test_text = test_df["Complaint_Description"].astype(str)

    y_train = train_df["Severity"]
    y_test = test_df["Severity"]

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2),
        max_features=2000,
        sublinear_tf=True
    )

    X_train = vectorizer.fit_transform(X_train_text)
    X_test = vectorizer.transform(X_test_text)

    labels = sorted(y_train.unique())

    label_to_number = {
        label: i
        for i, label in enumerate(labels)
    }

    number_to_label = {
        i: label
        for label, i in label_to_number.items()
    }

    y_train_encoded = y_train.map(label_to_number)
    y_test_encoded = y_test.map(label_to_number)

    sample_weights = compute_sample_weight(
        class_weight="balanced",
        y=y_train_encoded
    )

    model = XGBClassifier(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="multi:softmax",
        num_class=len(labels),
        eval_metric="mlogloss",
        tree_method="hist",
        n_jobs=2,
        random_state=42
    )

    print("Training XGBoost severity classifier...")

    model.fit(
        X_train,
        y_train_encoded,
        sample_weight=sample_weights
    )

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test_encoded,
        predictions
    )

    print("\n" + "=" * 55)
    print("CAMPUSFIX AI - SEVERITY CLASSIFIER")
    print("=" * 55)

    print(f"\nAccuracy: {accuracy:.2%}")

    print("\nClassification Report:")

    print(
        classification_report(
            y_test_encoded,
            predictions,
            labels=list(range(len(labels))),
            target_names=labels,
            zero_division=0
        )
    )

    os.makedirs(MODEL_DIR, exist_ok=True)

    joblib.dump(
        model,
        MODEL_PATH
    )

    joblib.dump(
        vectorizer,
        VECTORIZER_PATH
    )

    joblib.dump(
        number_to_label,
        LABELS_PATH
    )

    print("\nSaved:")
    print("✓ models/severity_xgboost.pkl")
    print("✓ models/severity_tfidf.pkl")
    print("✓ models/severity_labels.pkl")


def predict_severity(complaint):
    """
    Predict the severity of a new complaint
    using the trained XGBoost model.
    """

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    labels = joblib.load(LABELS_PATH)

    text_vector = vectorizer.transform(
        [str(complaint)]
    )

    prediction = model.predict(
        text_vector
    )[0]

    return labels[int(prediction)]


if __name__ == "__main__":
    train_severity_model()