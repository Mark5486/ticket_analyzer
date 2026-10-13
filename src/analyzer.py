
import string

from .models import Ticket, Priority, TicketType


URGENT_KEYWORDS = {
    "down",
    "urgent",
    "asap",
    "crash",
    "عاجل",
    "فوراً",
}

BUG_KEYWORDS = {
    "error",
    "bug",
    "crash",
    "failing",
    "بيباظ",
    "down",
}

QUESTION_KEYWORDS = {
    "how",
    "why",
    "when",
    "ازاي",
    "ليه",
    "امتى",
}


def clean_words(text: str) -> set[str]:
    arabic_punctuation = "،؛؟"
    punctuation = string.punctuation + arabic_punctuation

    words = text.lower().split()

    return {
        word.strip(punctuation)
        for word in words
        if word.strip(punctuation)
    }


def filter_urgent(tickets: list[Ticket]) -> list[Ticket]:
    return [ticket for ticket in tickets if ticket.is_urgent()]


def summarize(tickets: list[Ticket]) -> dict[str, int]:
    result = {}

    for ticket in tickets:
        priority = ticket.priority.value
        result[priority] = result.get(priority, 0) + 1

    return result


def top_words(text: str, count: int = 3) -> list[str]:
    words = text.lower().split()

    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    items = counts.items()

    sorted_items = sorted(
        items,
        key=lambda item: item[1],
        reverse=True,
    )

    top = sorted_items[:count]

    return [word for word, _ in top]


def detect_priority(text: str) -> Priority:
    words = clean_words(text)

    if words & URGENT_KEYWORDS:
        return Priority.URGENT

    return Priority.NORMAL


def classify_type(text: str) -> TicketType:
    words = clean_words(text)

    # BUG wins because a real problem is more important than the question format.
    if words & BUG_KEYWORDS:
        return TicketType.BUG

    if words & QUESTION_KEYWORDS:
        return TicketType.QUESTION

    return TicketType.FEATURE


def parse_ticket(text: str) -> Ticket:
    priority = detect_priority(text)
    category = classify_type(text)

    return Ticket(
        title=text,
        priority=priority,
        category=category,
    )


def build_report(tickets: list[Ticket]) -> str:
    lines = []

    for index, ticket in enumerate(tickets, start=1):
        line = (
            f"{index}. {ticket.title} - "
            f"{ticket.priority.value} - "
            f"{ticket.category.value}"
        )
        lines.append(line)

    summary = summarize(tickets)

    lines.append("Summary:")

    for priority, count in summary.items():
        lines.append(f"{priority}: {count}")

    return "\n".join(lines)
