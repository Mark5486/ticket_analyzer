from src.models import Ticket, Priority
from src.analyzer import filter_urgent, summarize


def test_filter_urgent_returns_only_urgent():
    tickets = [
        Ticket(title="A", priority=Priority.URGENT),
        Ticket(title="B", priority=Priority.NORMAL),
    ]

    urgent = filter_urgent(tickets)

    assert urgent[0].title == "A"


def test_summarize_counts_priorities():
    tickets = [
        Ticket(title="A", priority=Priority.URGENT),
        Ticket(title="B", priority=Priority.NORMAL),
        Ticket(title="C", priority=Priority.URGENT),
    ]

    summary = summarize(tickets)

    assert summary == {
        "urgent": 2,
        "normal": 1,
    }