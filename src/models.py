
from enum import Enum

from pydantic import BaseModel


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


class User(BaseModel):
    name: str
    email: str


class Ticket(BaseModel):
    title: str
    priority: Priority = Priority.NORMAL
    status: TicketStatus = TicketStatus.OPEN
    creator: User | None = None
    # Keep the default consistent with classify_type().
    category: TicketType = TicketType.FEATURE

    def is_urgent(self) -> bool:
        return self.priority == Priority.URGENT
