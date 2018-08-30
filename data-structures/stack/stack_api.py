"""Stack ADT

=== CSC148 Winter 2018 ===
Department of Computer Science,
University of Toronto
__author__ = 'Eric Koehli'

=== Module description ===
This module contains a Stack ADT implementation.
"""
from container_api import *
from typing import List
from timer import Timer


class EmptyStackError(EmptyContainerError):
    """Exception raised when an error occurs."""
    pass


class Stack(Container):
    """A last-in-first-out (LIFO) stack of items.

    Stores data in a first-in, last-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.
    """
    # === Private Attributes ===
    # _items:
    #     The items stored in the stack. The end of the list represents
    #     the top of the stack.
    _items: List[T]

    def __init__(self) -> None:
        """Initialize a new empty stack.

        >>> s = Stack()
        """
        Container.__init__(self)
        self._items = []

    def __iter__(self) -> T:
        """Iterate through the items in the stack from top
        to bottom.

        >>> s = Stack()
        >>> s.add(1)
        >>> s.add(2)
        >>> s.add(3)
        >>> x: int
        >>> [3, 2, 1] == [x for x in s]
        True
        """
        for i in range(len(self._items) - 1, -1, -1):
            yield self._items[i]

    def __str__(self) -> str:
        """Return a string representation of a Stack.

        >>> res = Stack()
        >>> res.add("blast off")
        >>> res.add(1)
        >>> res.add(2)
        >>> res.add(3)
        >>> print(res)
        *** top of stack ***
        3
        2
        1
        blast off
        *** bottom of stack ***
        """
        res = '*** top of stack ***\n'

        # iterate through the stack.
        # Note: we are using our __iter__ method here
        for element in self:
            res += str(element) + '\n'
        res += '*** bottom of stack ***'
        return res

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.add('hello')
        >>> s.is_empty()
        False
        """
        return self._size == 0
        # return self._items == []
        # Note: self._items == [] is faster than len(self._items) == 0
        # in general. Why?
        # Think about what happens when len(self._items) is called
        # on a list of 100,000 items.

    def add(self, obj: T) -> None:
        """Add (add) a new element to the top of this stack.

        >>> s = Stack()
        >>> s.add(7)
        >>> s.is_empty()
        False
        >>> len(s)
        1
        """
        self._items.append(obj)
        self._size += 1

    def remove(self) -> T:
        """Remove (remove) and return the element at the top of this stack.

        Raise an EmptyStackError if the stack is empty.
        >>> s = Stack()
        >>> s.add('hello')
        >>> s.add('goodbye')
        >>> s.remove()
        'goodbye'
        """
        if self.is_empty():
            raise EmptyStackError
        else:
            self._size -= 1
            return self._items.pop()

    def peek(self) -> T:
        """Returns the top element in the stack.

        Raise an EmptyStackError if the stack is empty.
        >>> s = Stack()
        >>> s.add(7)
        >>> s.add("top")
        >>> s.peek() == "top"
        True
        >>> len(s)
        2
        """
        if self.is_empty():
            raise EmptyStackError
        else:
            return self._items[len(self) - 1]

    def clear(self) -> None:
        """Removes all elements from the stack.
        """
        self._items = []
        self._size = 0


# some functions to mess around
def list_stack(list_: List[T], st: Stack) -> None:
    """Add elements of <list_> to <st>, and then print all
    the non-list elements.

    Assume <st> is empty.
    >>> lst1 = [1, 2, 3, 4, 5, 6, "hi", "bye", "end"]
    >>> lst2 = ["first", lst1, "last"]
    >>> stk = Stack()
    >>> list_stack(lst2, stk)
    last
    end
    bye
    hi
    6
    5
    4
    3
    2
    1
    first
    """
    for i in list_:
        st.add(i)
    while not st.is_empty():
        el = st.remove()
        if isinstance(el, list):
            for j in el:
                st.add(j)
        else:
            print(el)


def list_stack_rec(lst: list, stk: Stack) -> None:
    """Add each element from <lst> to <stk>, then remove the top element
    from <stk>.

    >>> lst1 = [1, 2, 3, 4, 5, 6, "hi", "bye", "end"]
    >>> lst2 = ["first", lst1, "last"]
    >>> stk = Stack()
    >>> list_stack_rec(lst2, stk)
    last
    end
    bye
    hi
    6
    5
    4
    3
    2
    1
    first
    """
    for element in lst:
        stk.add(element)

    while not stk.is_empty():               # while the stack is not empty
        top_item = stk.remove()
        if isinstance(top_item, list):
            list_stack_rec(top_item, stk)   # recursive call
        else:
            print(top_item)


# May be useful if your stack doesn't have a size attribute!
def size(stk: Stack) -> int:
    """Return the number of items in stk.

    Do not mutate stk.

    >>> stk = Stack()
    >>> size(stk)
    0
    >>> stk.add('hi')
    >>> stk.add('more')
    >>> stk.add('stuff')
    >>> size(stk)
    3
    """
    side_stack = Stack()
    count = 0
    # Pop everything off <stk> and onto <side_stack>, counting as we go.
    while not stk.is_empty():
        side_stack.add(stk.remove())
        count += 1
    # Now remove everything off <side_stack> and back onto <stk>.
    while not side_stack.is_empty():
        stk.add(side_stack.remove())
    # <stk> is restored to its state at the start of the function call.
    # We consider that it was not mutated.
    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Time how long it takes to perform stack operations on
    # stacks of various sizes. Try other stack implementations
    # and compare runtimes!
    for stack_size in [1000, 10000, 100000, 1000000]:
        # Uncomment out the stack implementation that we want
        # to time.
        stack = Stack()
        # stack = Stack2()      # eg) implement Stack2 with a linked list

        # Bypass the Stack interface to create a stack of
        # size <stack_size>.  We know this is cheating!
        stack._items = list(range(stack_size))

        # Create a Timer that will report how long it takes
        # to add and remove 1000 times on our stack. What
        # value we add should make no difference to the time
        # required, so we arbitrarily add 1.
        with Timer(f'Stack add/remove [size {stack_size}]'):
            for _ in range(1000):
                stack.add(1)
                stack.remove()

    # mess around example
    # s = Stack()
    # stopped = False
    # while not stopped:
    #     item = input('Enter a string or type \'end\' to exit: ')
    #     s.add(item)
    #     if item == 'end':
    #         stopped = True
    #
    # print("Your string stack contains:")
    # while not s.is_empty():
    #     item = s.remove()
    #     print(item)

    # Check out the iterator!
    s = Stack()
    s.add(1)
    s.add(2)
    s.add(3)
    for item in s:
        print(item)
