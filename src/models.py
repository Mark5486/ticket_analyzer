
from dataclasses import dataclass
from enum import Enum


class Priority(Enum):
    URGENT = "urgent"
    NORMAL = "normal"


class TicketType(Enum):
    BUG = "bug"
    QUESTION = "question"
    FEATURE = "feature"


class TicketStatus(Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"


@dataclass
class User:
    name: str
    email: str


@dataclass
class Ticket:
    title: str
    priority: Priority = Priority.NORMAL
    status: TicketStatus = TicketStatus.OPEN
    creator: User | None = None
    # Keep the default consistent with classify_type().
    category: TicketType = TicketType.FEATURE

    def is_urgent(self) -> bool:
        return self.priority == Priority.URGENT
