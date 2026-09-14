import pandas as pd
import re


def load_data(file_path):
    """Load complaint dataset from CSV."""
    return pd.read_csv(file_path)


def clean_text(text):
    """Clean complaint text for NLP processing."""
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def prepare_data(file_path):
    """Load and prepare complaint data."""
    df = load_data(file_path)

    # Clean complaint descriptions
    df["clean_complaint"] = df["Complaint_Description"].apply(clean_text)

    return df


if __name__ == "__main__":
    data = prepare_data("data/train.csv")

    print("CampusFix AI - Data Preprocessing")
    print("=" * 40)
    print("Dataset shape:", data.shape)
    print("\nColumns:")
    print(data.columns.tolist())

    print("\nSample cleaned complaints:")
    print(data[["Complaint_Description", "clean_complaint"]].head(5).to_string(index=False))
