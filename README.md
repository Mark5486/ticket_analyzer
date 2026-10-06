# Ticket Analyzer

A small Python project for analyzing support tickets.

## Features

- Filter urgent tickets
- Summarize ticket priorities
- Find the most common words

## Project Structure

```text
ticket_analyzer/
├── src/
│   ├── models.py
│   └── analyzer.py
├── tests/
│   └── test_models.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Usage

```python
from src.models import Ticket, Priority
from src.analyzer import filter_urgent

tickets = [
    Ticket(title="Server is down", priority=Priority.URGENT),
    Ticket(title="Update profile", priority=Priority.NORMAL),
]

urgent_tickets = filter_urgent(tickets)

for ticket in urgent_tickets:
    print(ticket.title)
```