import pandas as pd


def load_data(file_path="data/train.csv"):
    """Load campus complaint data."""
    return pd.read_csv(file_path)


def get_category_summary(df):
    """Return complaint count by category."""
    return df["Category"].value_counts()


def get_severity_summary(df):
    """Return complaint count by severity."""
    return df["Severity"].value_counts()


def get_department_summary(df):
    """Return complaint count by department."""
    return df["Primary_Department"].value_counts()


def get_aspect_summary(df):
    """Return most common complaint aspects."""
    return df["Aspects"].value_counts().head(10)


def show_analytics():
    """Display campus complaint analytics."""

    df = load_data()

    print("\n" + "=" * 55)
    print("CAMPUSFIX AI - CAMPUS ANALYTICS")
    print("=" * 55)

    print("\nTotal Complaints:", len(df))

    print("\n--- Complaints by Category ---")
    print(get_category_summary(df).to_string())

    print("\n--- Complaints by Severity ---")
    print(get_severity_summary(df).to_string())

    print("\n--- Complaints by Department ---")
    print(get_department_summary(df).to_string())

    print("\n--- Top Complaint Aspects ---")
    print(get_aspect_summary(df).to_string())


if __name__ == "__main__":
    show_analytics()