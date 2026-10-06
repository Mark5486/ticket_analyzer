from .models import Ticket


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