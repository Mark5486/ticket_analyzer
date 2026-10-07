from src.models import Priority, TicketType
from src.analyzer import detect_priority, classify_type, parse_ticket


def test_detect_priority_urgent():
    result = detect_priority("Server is URGENT")

    assert result == Priority.URGENT


def test_detect_priority_default():
    result = detect_priority("Please update my profile")

    assert result == Priority.NORMAL


def test_classify_bug_wins():
    result = classify_type("why does it crash")

    assert result == TicketType.BUG


def test_parse_empty_text():
    ticket = parse_ticket("")

    assert ticket.title == ""
    assert ticket.priority == Priority.NORMAL
    assert ticket.category == TicketType.FEATURE


def test_classify_feature():
    result = classify_type("Please add dark mode")

    assert result == TicketType.FEATURE