"""Choices of status."""
from enum import Enum


class Genre(Enum):
    """Status of getting DB dump file."""

    pop = "pop"
    classical = "classical"
    instrumental = "instrumental"

    @staticmethod
    def choices():
        """Options for Django dropdowns."""
        return (
            (Genre.pop.value, "pop"),
            (Genre.classical.value, "classical"),
            (Genre.instrumental.value, "instrumental")
        )
