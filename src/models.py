# ==========================================
# Day 5 — Models
# ==========================================

# Dart → Python
#
# Dart:
# class Ticket { }
#
# Python:
# class Ticket:
#
# Dart constructor:
# Ticket(this.title)
#
# Python:
# def __init__(self, title):
#
# Dart:
# this.title
#
# Python:
# self.title
#
# Dart:
# new Ticket(...)
#
# Python:
# Ticket(...)
#
# Dart private by convention:
# _name
#
# Python:
# _name
#
# Dart @override toString()
#
# Python:
# __str__
#
# My opinion:
# The weirdest difference from Dart is that Python uses special methods
# like __init__, __str__, and __eq__ instead of Dart-style overrides.

from dataclasses import dataclass
from enum import Enum


class Priority(Enum):
    URGENT = "urgent"
    NORMAL = "normal"


@dataclass
class Ticket:
    title: str
    priority: Priority = Priority.NORMAL
    status: str = "open"
    creator: str = ""

    def is_urgent(self) -> bool:
        return self.priority == Priority.URGENT


@dataclass
class User:
    name: str
    email: str
    
