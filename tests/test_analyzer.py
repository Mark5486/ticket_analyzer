
from src.models import Priority, TicketType
from src.analyzer import (
    detect_priority,
    classify_type,
    parse_ticket,
    clean_words,
)


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


def test_download_is_not_urgent():
    assert detect_priority(
        "Please fix the download button"
    ) == Priority.NORMAL


def test_clean_words_removes_punctuation():
    result = clean_words("Server is DOWN!!")

    assert result == {"server", "is", "down"}


def test_clean_words_removes_arabic_punctuation():
    result = clean_words("عاجل، السيرفر واقع!")

    assert result == {"عاجل", "السيرفر", "واقع"}
