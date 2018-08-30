"""Linked List

=== CSC148 Winter 2018 ===
University of Toronto,
Computer Science
__author__ = 'Eric Koehli'

=== Module Description ===
This module contains code for a linked list implementation with two classes,
LinkedList and _Node. This code was made by combining professor David Liu's
implementation with professor Danny Heap's implemenetation.
Note: Removing items from the front of the linked list runs in constant time
and removing items from the back of the linked list runs in linear time
because we have to iterate to the back of the linked list. A solution to this
problem is to implement a doubly linked list.
"""
from typing import Optional, Generic, TypeVar, List, Any

T = TypeVar('T')


class _Node(Generic[T]):
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next_:
        The next node in the list, or None if there are no more nodes.
    """
    item: T
    next_: Optional['_Node']

    def __init__(self, item: T, next_: Optional['_Node']=None) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next_ = next_  # Initially pointing to nothing

    def __str__(self) -> str:
        """
        Return a user-friendly representation of this _Node.

        >>> n = _Node(5, _Node(7))
        >>> print(n)
        5 -> 7 -> |
        """
        curr_node = self
        result = ''
        while curr_node is not None:
            result += f'{curr_node.item} -> '
            curr_node = curr_node.next_
        return result + '|'

    def __eq__(self, other: Any) -> bool:
        """
        Return whether _Node self is equivalent to other.

        >>> _Node(5).__eq__(5)
        False
        >>> n1 = _Node(5, _Node(7))
        >>> n2 = _Node(5, _Node(7, None))
        >>> n1.__eq__(n2)
        True
        """
        left_node = self
        right_node = other
        while (left_node is not None and right_node is not None
               and type(left_node) == type(right_node)
               and left_node.item == right_node.item):
            left_node = left_node.next_
            right_node = right_node.next_
        return right_node is None and left_node is None


class EmptyLinkedListError(Exception):
    """Exception raised when an error occurs."""


# ------------------------------------------------------------------------
# A very useful loop pattern:
#
# curr = ll._first
# while curr is not None:
#    ... do something with curr.item ...
#    curr = curr.next_
# ------------------------------------------------------------------------


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    # _last:
    #     The last node in the linked list, or None if the list is empty.
    # _size:
    #     The size of the linked list. Zero if the list is empty.
    _first: Optional[_Node]
    _last: Optional[_Node]
    _size: int

    def __init__(self, items: Optional[List[T]]=None) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if items == [] or items is None:  # No items, and an empty list!
            self._first, self._last, self._size = None, None, 0
        else:
            self._first, self._last, self._size = _Node(items[0]), \
                                                  _Node(items[-1]), len(items)
            current_node = self._first
            for item in items[1:]:
                current_node.next_ = _Node(item)
                current_node = current_node.next_

        # Initialize a node for the iterator
        self._iter_node = None

    # ------------------------------------------------------------------------
    # Non-mutating methods: these methods do not change the list
    # ------------------------------------------------------------------------
    def is_empty(self) -> bool:
        """Return whether this linked list is empty.

        >>> LinkedList([]).is_empty()
        True
        >>> LinkedList([1, 2, 3]).is_empty()
        False
        """
        return self._first is None

    def __str__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> str(LinkedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        >>> str(LinkedList([]))
        '[]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next_
        return '[' + ' -> '.join(items) + ']'

    # This version uses a handy str method called join.
    # It joins together a list of strings, using the
    # provided string as a separator:
    # >>> " -> ".join(['P', 'Q', 'R'])
    # 'P -> Q -> R'
    # You can use any string as a separator:
    # >>> "::".join(['P', 'Q', 'R'])
    # 'P::Q::R'

    def __str_v2__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> str(LinkedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        >>> str(LinkedList([]))
        '[]'
        """
        answer = '['
        curr = self._first
        while curr is not None:
            # Concatenate curr.item to the answer
            answer += str(curr.item)
            curr = curr.next
            if curr is not None:
                answer += ' -> '
        return answer + ']'

    # A third str method since we also defined the __str__ method in
    # class _Node. This version essentially passes the first _Node
    # and uses class _Node's __str__ method.
    def __str_v3__(self) -> str:
        """
        Return a human-friendly string representation of
        LinkedList self.

        >>> lnk = LinkedList([0, 1, 2, 3, 4, 5])
        >>> print(lnk)
        [0 -> 1 -> 2 -> 3 -> 4 -> 5]
        """
        return str(self._first)

    def __eq__(self, other: Any) -> bool:
        """Returns true iff all values stored in <self> are equivalent
        to all values stored in <other>

        >>> LinkedList().__eq__(None)
        False
        >>> lnk1 = LinkedList([1, 2, 3, 4, 5, 6])
        >>> lnk2 = LinkedList([1, 2, 3, 4, 5, 6])
        >>> lnk3 = LinkedList([1, 2, 3, 4])
        >>> lnk1 == lnk2
        True
        >>> lnk1 is lnk2
        False
        >>> lnk1 == lnk3
        False
        >>> LinkedList() == LinkedList()
        True
        """
        # Note: This works because we are implicitly calling the __eq__
        # method from class _Node (self._first == other._first) which checks
        # that the values are equivalent.
        return type(self) == type(other) and self._first == other._first

        # Alternatively... we could make use of our __iter__ method.
        # return (type(self) == type(other)
        #         and [a for a in self] == [b for b in other])

    # This version allows you to use negative indices like a
    # Python list.
    def __getitem__(self, index: int) -> T:
        """
        Return the value at LinkedList self's position index,
        which must be a valid position in LinkedList self.

        >>> lnk = LinkedList([0, 1, 2])
        >>> lnk.__getitem__(1)
        1
        >>> lnk[0]
        0
        >>> lnk[2]
        2
        >>> lnk[-1]
        2
        >>> lnk[-2]
        1
        >>> lnk[-3]
        0
        """
        # If the given index is negative, convert it to it's equivalent
        # positive index.
        if index < 0:
            index += self._size

        # Check if the index is valid.
        if index >= self._size or self._size == 0 or index < 0:
            raise IndexError('Index is out of bounds')

        # The given index is good, so find the item.
        curr = self._first
        for _ in range(index):
            curr = curr.next_
            # assert current is not None, 'reached invalid index'
        return curr.item

    # When reasoning about the design of this method:
    # (1) Under what conditions do we want the loop
    #     to stop?
    # (2) Therefore, under what conditions should
    #     it continue?  This determined the while
    #     condition.
    # (3) What can we conclude is true when the loop
    #     stops?  This lead us to the final steps
    #     of the method.
    # Note: This method is not as efficient as the above because it
    # iterates through the entire linked list even if the given index
    # is out of range. Use the above __getitem__
    def __getitem_v2__(self, index: int) -> T:
        """Return the item at position <index> in this list.

        Raise IndexError if <index> is >= the length of this list.

        >>> linky = LinkedList([100, 4, -50, 13])
        >>> linky.__getitem_v2__(0)
        100
        >>> linky.__getitem_v2__(2)
        -50
        >>> linky.__getitem_v2__(300)
        Traceback (most recent call last):
        IndexError: Index is out of bounds
        """
        if index < 0:
            index += self._size
        # Iterate to (index)-th node
        # Note: the two STOPPING conditions are
        # (1) curr is None (gone past the end of the list)
        # (2) curr_index == index (reached the correct node)
        # The loops stops when (1) or (2) is true,
        # so it *continues* when both are false.
        curr = self._first
        curr_index = 0
        while curr is not None and curr_index < index:
            curr = curr.next_
            curr_index += 1

        assert curr is None or curr_index == index  # for testing

        if curr is None:
            raise IndexError('Index is out of bounds')
        else:
            return curr.item

    def __contains__(self, item: T) -> bool:
        """
        Return whether LinkedList self contains <item>.

        This method allows you to use the 'in' syntax sugar.

        >>> lnk = LinkedList([2, 1, 0])
        >>> lnk.__contains__(1)
        True
        >>> lnk.__contains__(3)
        False
        >>> 2 in lnk
        True
        >>> 3 in lnk
        False
        """
        curr = self._first
        while curr is not None:
            if curr.item == item:
                return True
            curr = curr.next_
        return False

    def __len__(self) -> int:
        """Return the length of this Linked List.

        >>> lnk = LinkedList([0, 1, 2, 3, 4])
        >>> len(lnk)
        5
        """
        return self._size

    def __iter__(self) -> T:
        """Iterate over the linked list.
        Note: most methods do not use __iter__ to practice the
        standard loop pattern shown at line 81

        >>> lnk = LinkedList([0, 1, 2, 3, 4])
        >>> x: int
        >>> [0, 1, 2, 3, 4] == [x for x in lnk]
        True
        """
        curr = self._first
        while curr is not None:
            yield curr.item
            curr = curr.next_

    def __add__(self, other: 'LinkedList') -> 'LinkedList':
        """Return a new list by concatenating self to other. Leave
        both self and other unchanged.

        >>> lnk1 = LinkedList([4, 8])
        >>> lnk2 = LinkedList([3, 7])
        >>> print(lnk1 + lnk2)
        [4 -> 8 -> 3 -> 7]
        >>> print(lnk1)
        [4 -> 8]
        >>> lnk3 = lnk1 + lnk2
        >>> len(lnk3) == len(lnk1) + len(lnk2)
        True
        """
        new_ll = LinkedList()
        curr_node = self._first
        while curr_node is not None:
            new_ll.append(curr_node.item)
            curr_node = curr_node.next_
        curr_node = other._first
        while curr_node is not None:
            new_ll.append(curr_node.item)
            curr_node = curr_node.next_
        # Append updates the size of the new LL.
        return new_ll

    def copy(self) -> 'LinkedList':
        """
        Return a copy of LinkedList self.  The copy should have
        different nodes, but equivalent values, from self.

        >>> lnk = LinkedList([5, 7])
        >>> print(lnk.copy())
        [5 -> 7]
        >>> lnk_copy = lnk.copy()
        >>> len(lnk_copy)
        2
        """
        return LinkedList([x for x in self])

        # Alternatively
        # new_ll = LinkedList()
        # curr = self._first
        # while curr is not None:
        #     new_ll.append(curr.item)
        #     curr = curr.next_
        # # Don't need to update size because append updates the size.
        # return new_ll

    def _is_valid_index(self, index: int) -> bool:
        """Return true iff the given <index> is a valid index
        in the linked list.

        >>> link1 = LinkedList([0, 1, 2, 3, 4])
        >>> link2 = LinkedList()
        >>> link1._is_valid_index(2)
        True
        >>> link1._is_valid_index(-2)
        True
        >>> link2._is_valid_index(2)
        False
        """
        if index < 0:
            index += self._size
        # Check if the index is valid.
        if index >= self._size or self._size == 0 or index < 0:
            return False
        return True

    # ------------------------------------------------------------------------
    # Mutating methods: these methods change the list
    # ------------------------------------------------------------------------
    def pop(self, index: int) -> T:
        """Remove and return the item at position <index>.

        Raise IndexError if index >= len(self).

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.pop(1)
        2
        >>> lst.pop(2)
        200
        >>> lst.pop(0)
        1
        >>> len(lst)
        1
        >>> lst.pop(148)
        Traceback (most recent call last):
        IndexError: Index out of range
        """
        if self.is_empty():
            raise EmptyLinkedListError
        elif index < 0:
            index += self._size
        # Check the index before iterating
        if not self._is_valid_index(index):
            raise IndexError("Index out of range")

        # Case 1: Index is at the front of the linked list
        if index == 0:
            return self.pop_front()

        # Case 2: we want to remove the last item
        elif index == self._size - 1:
            return self.pop_back()

        # Case 3: 0 < index < self._size - 1
        else:
            curr = self._first
            for _ in range(index - 1):      # iterate with confidence!
                curr = curr.next_
            # update the link to skip the index-th node
            item, curr.next_ = curr.next_.item, curr.next_.next_
            self._size -= 1
            return item

        # alternate loop
        # else:
        #     # Iterate to (index-1)-th node.
        #     curr, curr_index = self._first, 0
        #     while curr is not None and curr_index < index - 1:
        #         curr = curr.next_
        #         curr_index += 1
        #
        #     if curr is None or curr.next_ is None:
        #         raise IndexError
        #     else:
        #         # Update link to skip over i-th node
        #         item, curr.next_ = curr.next_.item, curr.next_.next_
        #         self._size -= 1
        #         return item

    def insert(self, index: int, item: T) -> None:
        """Insert a new node containing item at position <index>.

        Raise IndexError if index > len(self).
        Note that adding to the end of a linked list is okay.

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.insert(2, 300)
        >>> str(lst)
        '[1 -> 2 -> 300 -> 10 -> 200]'
        >>> lst.insert(5, -1)
        >>> str(lst)
        '[1 -> 2 -> 300 -> 10 -> 200 -> -1]'
        >>> lst.insert(100, 2)
        Traceback (most recent call last):
        IndexError: Index out of range
        >>> lst.insert(0, 999)
        >>> str(lst)
        '[999 -> 1 -> 2 -> 300 -> 10 -> 200 -> -1]'
        """
        # Create new node containing the item
        new_node = _Node(item)

        # Check the index before wasting time iterating
        if index < 0:
            index += self._size
        if index > self._size or index < 0:
            # Note: index strictly greater than self._size
            raise IndexError("Index out of range")

        # Case 1: index is at the front of the list
        if index == 0:
            # insert at the front
            self._first, new_node.next_ = new_node, self._first
        # Case 2: 0 < index <= self._size
        else:
            curr = self._first
            for _ in range(index - 1):
                curr = curr.next_
            # update links to insert new node
            curr.next_, new_node.next_ = new_node, curr.next_
        self._size += 1

        # alternative if you don't have a size attribute:
        # if index == 0:
        #     # Insert at the front.
        #     self._first, new_node.next_ = new_node, self._first
        # else:
        #     # Iterate to (index-1)-th node.
        #     curr = self._first
        #     curr_index = 0
        #     while curr is not None and curr_index < index - 1:
        #         curr = curr.next_
        #         curr_index += 1
        #         # We know that either
        #         #    (a) curr is None or
        #         #    (b) curr_index == index - 1
        #
        #     if curr is None:
        #         # The index was too big.
        #         raise IndexError
        #     else:
        #         # Update links to insert new node
        #         curr.next_, new_node.next_ = new_node, curr.next_

    def remove(self, item: T) -> None:
        """Remove the FIRST occurrence of <item> in this list.

        Do nothing if this list does not contain <item>.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.remove(2)
        >>> str(lst)
        '[1 -> 3]'
        >>> lst.remove(2)
        >>> str(lst)
        '[1 -> 3]'
        >>> lst.remove(3)
        >>> str(lst)
        '[1]'
        >>> lst.remove(1)
        >>> str(lst)
        '[]'
        >>> lst.remove(1)
        >>> str(lst)
        '[]'
        """
        # Find the node.
        prev, curr = None, self._first
        while curr is not None and curr.item != item:
            prev, curr = curr, curr.next_

        # Delete the node, carefully.
        if curr is not None:
            if prev is not None:
                prev.next_ = curr.next_
            else:
                # <item> is the first element in the linked list.
                self._first = curr.next_
            # Don't forget to decrease the size!
            self._size -= 1

    def append(self, item: T) -> None:
        """
        Insert a new LinkedListNode with value after self._last

        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> len(lnk)
        1
        >>> print(lnk)
        [5]
        >>> lnk.append(6)
        >>> len(lnk)
        2
        >>> print(lnk)
        [5 -> 6]
        >>> len(lnk)
        2
        """
        new_node = _Node(item)
        # Case 1
        if self._size == 0:
            self._last, self._first = new_node, new_node
        # Case 2
        else:
            self._last.next_, self._last = new_node, new_node
        self._size += 1

        # Note: this isn't as efficient because we have to iterate to the back
        # self.insert(self._size, item)

    def prepend(self, item: T) -> None:
        """
        Insert <item> before LinkedList self.front.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> str(lnk)
        '[2 -> 1 -> 0]'
        >>> len(lnk)
        3
        """
        new_node = _Node(item)
        if self._size == 0:
            self._first, self._last = new_node, new_node
        else:
            new_node.next_ = self._first
            self._first = new_node
        self._size += 1

        # Alternatively we could do the following, and note that the runtime
        # would be the same in this case.
        # self.insert(0, item)

    def delete_first(self) -> None:
        """
        Delete the first item from the list.

        >>> lnk = LinkedList([2, 1, 0])
        >>> lnk.delete_first()
        >>> str(lnk)
        '[1 -> 0]'
        >>> len(lnk)
        2
        >>> lnk.delete_first()
        >>> lnk.delete_first()
        >>> str(lnk)
        '[]'
        """
        if self._size == 0:
            raise IndexError
        elif self._size == 1:
            self._first, self._last = None, None
        else:
            self._first = self._first.next_
        self._size -= 1

    def pop_front(self) -> T:
        """
        Remove the first element and return its value.

        >>> lnk = LinkedList([0, 1])
        >>> lnk.pop_front()
        0
        >>> len(lnk)
        1
        """
        if self._size == 0:
            raise EmptyLinkedListError
        item = self._first.item
        self.delete_first()
        return item

    def delete_last(self) -> None:
        """ Delete the last item of the linked list.

        >>> lnk = LinkedList([0, 1])
        >>> lnk.delete_last()
        >>> print(lnk)
        [0]
        >>> len(lnk)
        1
        """
        if self._size == 0:
            raise EmptyLinkedListError

        # Case 1: only one item in the list
        if self._size == 1:
            self._first, self._last = None, None

        # Case 2: self._size > 1
        else:
            prev_node, curr_node = None, self._first
            while curr_node != self._last:
                prev_node = curr_node
                curr_node = curr_node.next_
            self._last = prev_node
            prev_node.next_ = None
        self._size -= 1

    def pop_back(self) -> T:
        """Remove the last item in the linked list and
        return it's value.

        Raise EmptyLinkedListError if the list is empty

        >>> lnk = LinkedList([0, 1, 2, 3, 6, 7])
        >>> lnk.pop_back()
        7
        >>> lnk.pop_back()
        6
        >>> print(lnk)
        [0 -> 1 -> 2 -> 3]
        >>> len(lnk)
        4
        """
        if self._size == 0:
            raise EmptyLinkedListError
        item = self._last.item
        self.delete_last()
        return item


# Exam questions - Midterm 1 fall 2017
def swap(lst: LinkedList, i: int, j: int) -> None:
    """Swap the values stored at indexes <i> and <j> in the
    given linked list.

    Precondition: i and j are >= 0.
    Raise an IndexError if i or j (or both) are too large
    (out of bounds for this list).
    NOTE: You don't need to create new nodes or change
    any "next" attributes. You can implement this method
    simply by assigning to the "item" attribute of existing nodes.

    >>> linky = LinkedList([10, 20, 30, 40, 50])
    >>> swap(linky, 0, 3)
    >>> print(linky)
    [40 -> 20 -> 30 -> 10 -> 50]
    """
    # Go to the node at index i.
    curr_i = lst._first
    curr_index = 0
    while curr_i is not None and curr_index < i:
        curr_i = curr_i.next_
        curr_index += 1

    # Go to the node at index j.
    curr_j = lst._first
    curr_index = 0
    while curr_j is not None and curr_index < j:
        curr_j = curr_j.next_
        curr_index += 1

    if curr_i is None or curr_j is None:
        # At least one of i and j is out of bounds
        raise IndexError
    else:
        # Both nodes are in bounds; swap their items.
        curr_i.item, curr_j.item = curr_j.item, curr_i.item

    # Verion 3
    # curr_i, index = lst.front, 0
    # while curr_i is not None and index < i:
    #     curr_i = curr_i.next_
    #
    # curr_j, index = lst.front, 0
    # while curr_j is not None and index < j:
    #     curr_j = curr_j.next_
    #
    # if curr_i is None or curr_j is None:
    #     raise IndexError('Out of range')
    #
    # curr_i.value, curr_j.value = curr_j.value, curr_i.value

    # Version 2:
    # curr_node_i, curr_i, curr_node_j, curr_j = lst.front, 0, lst.front, 0
    #
    # # Go to index i
    # while curr_node_i is not None and curr_i < i:
    #     curr_node_i = curr_node_i.next_
    #     curr_i += 1
    #
    # # Go to index j
    # while curr_node_j is not None and curr_j < j:
    #     curr_node_j = curr_node_j.next_
    #     curr_j += 1
    #
    # # Swap values
    # if curr_node_i is None or curr_node_j is None:
    #     raise IndexError('Out of range.')
    # else:
    #     curr_node_i.value, curr_node_j.value = curr_node_j.value, \
    #                                            curr_node_i.value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
