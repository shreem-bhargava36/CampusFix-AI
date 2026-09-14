from src.priority_engine import calculate_priority, get_priority_level
from src.routing_engine import route_complaint
from src.preprocessing import clean_text


def test_clean_text():
    result = clean_text("  WiFi IS NOT Working!  ")
    assert result == "wifi is not working"


def test_priority_calculation():
    score = calculate_priority("Urgent", "Technical")
    assert score == 98


def test_priority_level():
    assert get_priority_level(98) == "Critical"
    assert get_priority_level(75) == "High"
    assert get_priority_level(50) == "Medium"
    assert get_priority_level(25) == "Low"


def test_routing():
    assert route_complaint("Technical") == "IT"
    assert route_complaint("Infrastructure") == "Maintenance"
    assert route_complaint("Finance") == "Finance"
    assert route_complaint("Academic") == "Department Head"