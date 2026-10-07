from dataclasses import dataclass
from enum import Enum


class Priority(Enum):
    URGENT = "urgent"
    NORMAL = "normal"


class TicketType(Enum):
    BUG = "bug"
    QUESTION = "question"
    FEATURE = "feature"


@dataclass
class Ticket:
    title: str
    priority: Priority = Priority.NORMAL
    status: str = "open"
    creator: str = ""
    category: TicketType = TicketType.QUESTION

    def is_urgent(self) -> bool:
        return self.priority == Priority.URGENT


@dataclass
class User:
    name: str
    email: str