"""Interface for future server-side grading strategies."""

from typing import Protocol


class GameEngine(Protocol):
    def grade(self, answer: object, expected: object) -> bool: ...
