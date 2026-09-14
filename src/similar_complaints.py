import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_complaints(file_path="data/train.csv"):
    """Load previous campus complaints."""
    df = pd.read_csv(file_path)

    df["Complaint_Description"] = (
        df["Complaint_Description"]
        .fillna("")
        .astype(str)
    )

    return df


def find_similar_complaints(
    complaint,
    file_path="data/train.csv",
    threshold=0.25,
    top_k=3
):
    """
    Find previous complaints similar to a new complaint.

    Returns the most similar complaints above the
    similarity threshold.
    """

    df = load_complaints(file_path)

    complaints = df["Complaint_Description"].tolist()

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2)
    )

    vectors = vectorizer.fit_transform(
        complaints + [complaint]
    )

    new_vector = vectors[-1]
    previous_vectors = vectors[:-1]

    similarities = cosine_similarity(
        new_vector,
        previous_vectors
    )[0]

    df["similarity"] = similarities

    similar = (
        df[df["similarity"] >= threshold]
        .sort_values("similarity", ascending=False)
        .head(top_k)
    )

    return similar[
        [
            "Complaint_Description",
            "Category",
            "Severity",
            "Primary_Department",
            "similarity"
        ]
    ]


if __name__ == "__main__":

    complaint = input(
        "Enter a new complaint: "
    )

    results = find_similar_complaints(complaint)

    print("\n" + "=" * 60)
    print("CAMPUSFIX AI - SIMILAR COMPLAINT DETECTION")
    print("=" * 60)

    if results.empty:

        print("\nNo similar complaints found.")

    else:

        print(
            f"\n{len(results)} similar complaint(s) found:\n"
        )

        for _, row in results.iterrows():

            print(
                f"Similarity : {row['similarity']:.2%}"
            )
            print(
                f"Category   : {row['Category']}"
            )
            print(
                f"Severity   : {row['Severity']}"
            )
            print(
                f"Department : {row['Primary_Department']}"
            )
            print(
                f"Complaint  : {row['Complaint_Description']}"
            )
            print("-" * 60)