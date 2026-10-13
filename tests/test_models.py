
from src.models import Ticket, Priority, User, TicketStatus
from src.analyzer import filter_urgent, summarize, top_words


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


def test_top_words_returns_most_common_words():
    result = top_words("python python dart python dart flutter")

    assert result == ["python", "dart", "flutter"]


def test_ticket_can_have_a_creator():
    user = User(name="Mark", email="mark@example.com")

    ticket = Ticket(title="Fix login", creator=user)

    assert ticket.creator == user
    assert ticket.creator.name == "Mark"
    assert ticket.creator.email == "mark@example.com"


def test_ticket_default_status_is_open():
    ticket = Ticket(title="Fix login")

    assert ticket.status == TicketStatus.OPEN
