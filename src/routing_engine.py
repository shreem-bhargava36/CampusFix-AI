def route_complaint(category, aspect=None):
    """
    Determine the most appropriate department
    for a campus complaint.
    """

    category_routes = {
        "Infrastructure": "Maintenance",
        "Technical": "IT",
        "Academic": "Department Head",
        "Finance": "Finance",
        "Administrative": "Registrar"
    }

    aspect_routes = {
        "WiFi": "IT",
        "Lab Equipment": "IT",
        "Projector": "IT",
        "Water Supply": "Maintenance",
        "Washroom": "Maintenance",
        "Electrical/AC": "Maintenance",
        "Parking": "Transport & Parking",
        "Fee/Payment": "Finance",
        "Library": "Library",
        "Faculty": "Department Head"
    }

    # Aspect-specific routing gets priority
    if aspect:
        for key, department in aspect_routes.items():
            if key.lower() in aspect.lower():
                return department

    # Otherwise use category
    return category_routes.get(category, "Student Welfare")


if __name__ == "__main__":

    test_cases = [
        ("Technical", "WiFi"),
        ("Infrastructure", "Water Supply"),
        ("Finance", "Fee/Payment"),
        ("Academic", "Faculty"),
        ("Administrative", None)
    ]

    print("CAMPUSFIX AI - ROUTING ENGINE")
    print("=" * 45)

    for category, aspect in test_cases:

        department = route_complaint(category, aspect)

        print(
            f"Category: {category:15} "
            f"| Aspect: {str(aspect):15} "
            f"| Department: {department}"
        )
        