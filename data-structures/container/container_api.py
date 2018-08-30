"""Container ADT

=== CSC148 Winter 2018 ===
University of Toronto,
Computer Science
__author__ = 'Eric Koehli'

=== Module Description ===
This module contains an ADT container as an asbtract class for other ADT's.
"""
from typing import Generic, TypeVar

# This is used to facilitate PyCharm's typechecking.
T = TypeVar('T')


class EmptyContainerError(Exception):
    """Exception raised when an error occurs."""
    pass


class Container(Generic[T]):
    """A super class ADT Container for other ADT desendents.

    This is an abstract class and should not be instantiated directly.
    """
    # === Private Attributes ===
    # _size:
    #     The number of items stored in this container.
    _size: int

    def __init__(self) -> None:
        """Initialize a new container.

        This should not be instantitated directly.
        """
        self._size = 0

    def __len__(self):
        """Returns the number of items in this container.
        """
        return self._size

    def __str__(self) -> str:
        """Return a string representation of a container.
        """
        raise NotImplementedError

    def add(self, obj: T) -> None:
        """Add an item to the container.
        """
        raise NotImplementedError

    def remove(self) -> T:
        """Remove an object from the container.
        """
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return true iff the container is empty.
        """
        raise NotImplementedError

    def peek(self) -> T:
        """Return the next element in the container without modifying.
        """
        raise NotImplementedError

    def __iter__(self) -> T:
        """Return an iterator over a container.
        """
        raise NotImplementedError


if __name__ == '__main__':
    import doctest
    doctest.testmod()
