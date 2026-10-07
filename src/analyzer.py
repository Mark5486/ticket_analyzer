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

    return [word for word, freq in top]


def detect_priority(text: str) -> Priority:
    text = text.lower()

    for keyword in URGENT_KEYWORDS:
        if keyword in text:
            return Priority.URGENT

    return Priority.NORMAL


def classify_type(text: str) -> TicketType:
    text = text.lower()

    # BUG wins because a real problem is more important than the question format.
    for keyword in BUG_KEYWORDS:
        if keyword in text:
            return TicketType.BUG

    for keyword in QUESTION_KEYWORDS:
        if keyword in text:
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