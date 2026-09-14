import os
import sys

# Add the src folder to Python's import path
SRC_PATH = os.path.join(
    os.path.dirname(__file__),
    "src"
)

sys.path.insert(0, SRC_PATH)

from preprocessing import clean_text
from issue_classifier import predict_category
from severity_engine import predict_severity
from priority_engine import calculate_priority, get_priority_level
from routing_engine import route_complaint
from similar_complaints import find_similar_complaints


def analyze_complaint(complaint):
    """Run the complete CampusFix AI analysis pipeline."""

    # Step 1: Clean complaint text
    cleaned_complaint = clean_text(complaint)

    # Step 2: Predict category
    category = predict_category(cleaned_complaint)

    # Step 3: Predict severity
    severity = predict_severity(cleaned_complaint)

    # Step 4: Calculate priority
    priority_score = calculate_priority(
        severity,
        category
    )

    priority_level = get_priority_level(
        priority_score
    )

    # Step 5: Find similar complaints
    similar = find_similar_complaints(
        complaint
    )

    # Step 6: Route complaint
    department = route_complaint(
        category
    )

    return {
        "category": category,
        "severity": severity,
        "priority_score": priority_score,
        "priority_level": priority_level,
        "department": department,
        "similar": similar
    }


def main():
    """Main CampusFix AI application."""

    print("=" * 55)
    print("                 CAMPUSFIX AI")
    print("     Intelligent Campus Complaint System")
    print("=" * 55)

    while True:

        print("\n1. Analyze New Complaint")
        print("2. Campus Analytics")
        print("3. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":

            complaint = input(
                "\nEnter your complaint:\n> "
            ).strip()

            if not complaint:
                print(
                    "\nError: Complaint cannot be empty."
                )
                continue

            try:

                result = analyze_complaint(
                    complaint
                )

                print("\n" + "-" * 55)
                print("                 AI ANALYSIS")
                print("-" * 55)

                print(
                    f"Category       : "
                    f"{result['category']}"
                )

                print(
                    f"Severity       : "
                    f"{result['severity']}"
                )

                print(
                    f"Priority       : "
                    f"{result['priority_score']}/100 "
                    f"({result['priority_level']})"
                )

                print(
                    f"Department     : "
                    f"{result['department']}"
                )

                print("\nSimilar Issues:")

                similar = result["similar"]

                if similar.empty:

                    print(
                        "No similar complaints detected."
                    )

                else:

                    print(
                        f"{len(similar)} "
                        f"similar complaint(s) found."
                    )

                    for _, row in similar.iterrows():

                        print(
                            f"\n- {row['Complaint_Description']}"
                        )

                print("-" * 55)

            except Exception as error:

                print(
                    "\nError while analyzing complaint:"
                )
                print(error)

        elif choice == "2":

            from analytics import show_analytics

            show_analytics()

        elif choice == "3":

            print(
                "\nThank you for using CampusFix AI."
            )
            break

        else:

            print(
                "\nInvalid choice. "
                "Please enter 1, 2, or 3."
            )


if __name__ == "__main__":
    main()
    