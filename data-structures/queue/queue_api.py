"""Queue ADT

=== CSC148 Winter 2018 ===
Computer Science,
University of Toronto
__author__ = 'Eric Koehli'

=== Module Description ===
An implementation of a queue ADT. Should change add and remove to enqueue and
dequeue.
"""
from container_api import *
from my_linked_list import LinkedList


class EmptyQueueError(EmptyContainerError):
    """Exception raised when an error occurs."""
    pass


class Queue(Container):
    """A first-in, first-out (FIFO) queue of items.

    Stores data in a first-in, first-out order. When removing an item from the
    queue, the 'first' item is removed.
    """
    # === Private attributes ===
    # _items:
    #     The items stored in the queue. The back of the linked list
    #     represents the most-recently added item (back of queue).
    # Note:
    #     We are storing the items in a LinkedList rather than a python
    #     list for better runtime when removing an item.
    _items: LinkedList

    def __init__(self) -> None:
        """Initialize a new empty Queue.

        >>> q = Queue()
        """
        super().__init__()
        self._items = LinkedList()

    def __str__(self) -> str:
        """Return a string representation of a Queue ADT.

        >>> q = Queue()
        >>> q.add(1)
        >>> q.add(2)
        >>> q.add(3)
        >>> str(q)
        '[3 -> 2 -> 1]'
        """
        items = []
        for item in self:
            items.append(str(item))
        return '[' + ' -> '.join(items) + ']'

    def add(self, obj: T) -> None:
        """
        Add (enqueue) object to the back of Queue self.

        >>> q = Queue()
        >>> q.add(7)
        """
        self._items.append(obj)     # add to the back of the linked list
        self._size += 1

    def remove(self) -> T:
        """
        Remove (dequeue) and return front object from Queue self.

        Raise an EmpytyQueueError if the Queue <self> is empty.
        >>> q = Queue()
        >>> q.add(3)
        >>> q.add(5)
        >>> q.remove()
        3
        """
        if self.is_empty():
            raise EmptyQueueError('The Queue must not be empty')
        else:
            # remove from the front of the linked list for faster runtime!
            self._size -= 1
            return self._items.pop_front()

    def is_empty(self) -> bool:
        """
        Return whether Queue self is empty

        >>> q = Queue()
        >>> q.add(5)
        >>> q.is_empty()
        False
        >>> q.remove()
        5
        >>> q.is_empty()
        True
        """
        return self._items.is_empty()

    def peek(self) -> T:
        """Return the item at the front of the queue.

        >>> q = Queue()
        >>> q.add(1)
        >>> q.add(2)
        >>> q.add(3)
        >>> q.peek()
        1
        >>> len(q)
        3
        """
        front = self._items.pop_front()
        self._items.prepend(front)
        return front

    def __iter__(self) -> T:
        """Iterate through the queue from the first item added to the last.
        """
        for i in range(len(self._items) - 1, -1, -1):
            yield self._items[i]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
