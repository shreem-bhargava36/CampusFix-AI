def calculate_priority(severity, category):
    """
    Calculate complaint priority score from 0 to 100.
    """

    severity_scores = {
        "Low": 25,
        "Medium": 50,
        "High": 75,
        "Urgent": 95
    }

    category_bonus = {
        "Technical": 3,
        "Infrastructure": 3,
        "Academic": 2,
        "Finance": 1,
        "Administrative": 1
    }

    base_score = severity_scores.get(severity, 50)
    bonus = category_bonus.get(category, 0)

    priority = min(base_score + bonus, 100)

    return priority


def get_priority_level(score):
    """Convert numeric score into priority level."""

    if score >= 85:
        return "Critical"
    elif score >= 65:
        return "High"
    elif score >= 40:
        return "Medium"
    else:
        return "Low"


if __name__ == "__main__":

    test_cases = [
        ("Urgent", "Technical"),
        ("High", "Infrastructure"),
        ("Medium", "Academic"),
        ("Low", "Administrative")
    ]

    print("CAMPUSFIX AI - PRIORITY ENGINE")
    print("=" * 40)

    for severity, category in test_cases:

        score = calculate_priority(severity, category)
        level = get_priority_level(score)

        print(
            f"{category:15} | "
            f"{severity:8} | "
            f"{score:3}/100 | "
            f"{level}"
        )