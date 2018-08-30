"""Linked List v2

=== CSC148 Winter 2018 ===
University of Toronto,
Computer Science
__author__ = 'Eric Koehli'

=== Module Description ===
This module contains a linked list implementation. Note that the size can be
reduced by using multiple assignment statements. This module was made for lab 4.
"""
from typing import Optional, Any, Callable


class LinkedListException(Exception):
    """
    Raise a linked list exception.
    """


class LinkedListNode:
    """
    A Node to be used in linked list

    === Attributes ===
    next_:
           Successor to this LinkedListNode
    value:
           Data this LinkedListNode represents
    """
    next_: Optional['LinkedListNode']
    value: Any

    def __init__(self, value: Any,
                 next_: Optional['LinkedListNode'] = None) -> None:
        """
        Create LinkedListNode self with data value and successor next_.
        """
        self.value, self.next_ = value, next_

    def __str__(self) -> str:
        """
        Return a user-friendly representation of this LinkedListNode.

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """
        # start with a string s to represent current node.
        s = "{} ->".format(self.value)
        # create a reference to "walk" along the list
        current_node = self.next_
        # for each subsequent node in the list, build s
        while current_node is not None:
            s += " {} ->".format(current_node.value)
            current_node = current_node.next_
        # add "|" at the end of the list
        assert current_node is None, "unexpected non_None!!!"
        s += "|"
        return s

        # or...
        # curr_node = self
        # s = ''
        # while curr_node is not None:
        #     s += f'{curr_node.value} -> '
        #     curr_node = curr_node.next_
        # return s[:-1] + '|'

    def __eq__(self, other: Any) -> bool:
        """
        Return whether LinkedListNode self is equivalent to other.

        >>> LinkedListNode(5).__eq__(5)
        False
        >>> n1 = LinkedListNode(5, LinkedListNode(7))
        >>> n2 = LinkedListNode(5, LinkedListNode(7, None))
        >>> n1.__eq__(n2)
        True
        """
        left_node, right_node = self, other
        while (left_node is not None and right_node is not None
               and type(left_node) == type(right_node)
               and right_node.value == left_node.value):
            right_node, left_node = right_node.next_, left_node.next_
        return right_node is None and left_node is None


class LinkedList:
    """
    A collection of LinkedListNodes

    === Attributes ==
    front - first node of this LinkedList
    back - last node of this LinkedList
    size - number of nodes in this LinkedList, >= 0
    """
    front: Optional[LinkedListNode]
    back: Optional[LinkedListNode]
    size: int

    def __init__(self, items: Optional[list]=None) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if items == [] or items is None:  # No items, and an empty list!
            self.front, self.back, self.size = None, None, 0
        else:
            self.front, self.back, self.size = LinkedListNode(items[0]), \
                                                  LinkedListNode(items[-1]), \
                                                  len(items)
            current_node = self.front
            for item in items[1:]:
                current_node.next_ = LinkedListNode(item)
                current_node = current_node.next_

        # Initialize a node for the iterator
        self._iter_node = None

    def __str__(self) -> str:
        """
        Return a human-friendly string representation of
        LinkedList self.
        Note: this method uses the __str__ method implemented
        in the LinkedListNode class.

        >>> lnk = LinkedList()
        >>> print(lnk)
        Empty!
        >>> lnk.prepend(5)
        >>> print(lnk)
        5 ->| Size: 1
        """
        # deal with the case where this list is empty
        if self.front is None:
            assert self.back is None and self.size is 0, "ooooops!"
            return "Empty!"
        # use front.__str__() if this list isn't empty
        return str(self.front) + " Size: {}".format(self.size)

        # or...
        # if self.front is None:
        #     return 'Empty!'
        # else:
        #     return f'{self.front} Size: {self.size}'

    def __eq__(self, other: Any) -> bool:
        """
        Return whether LinkedList self is equivalent to
        other.

        >>> LinkedList().__eq__(None)
        False
        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(5)
        >>> lnk.__eq__(lnk2)
        True
        """
        # Note this calls LinkedListNode's __eq__ method.
        return type(self) == type(other) and self.front == other.front

    def delete_after(self, value: object) -> None:
        """
        Remove the node following the first occurrence of value, if
        possible, otherwise leave self unchanged.

        >>> lnk = LinkedList()
        >>> lnk.append(2)
        >>> lnk.append(3)
        >>> lnk.append(4)
        >>> lnk.append(5)
        >>> lnk.append(6)
        >>> lnk.delete_after(3)
        >>> print(lnk)
        2 -> 3 -> 5 -> 6 ->| Size: 4
        >>> lnk.delete_after(6)
        >>> print(lnk)
        2 -> 3 -> 5 -> 6 ->| Size: 4
        >>> lnk.delete_after(5)
        >>> print(lnk)
        2 -> 3 -> 5 ->| Size: 3
        >>> lnk.size == 3
        True
        """
        curr_node = self.front
        while curr_node is not None and curr_node.value != value:
            curr_node = curr_node.next_
        if curr_node.value == value and curr_node.next_ is not None:
            curr_node.next_ = curr_node.next_.next_
            self.size -= 1

        # alternatively...
        # if self.size < 2:
        #     self.front, self.back, self.size = None, None, 0
        #     return
        #
        # curr = self.front
        # while curr is not None and curr.value != value:
        #     curr = curr.next_
        #
        # if curr is not None:
        #     # curr.value == value
        #     if curr.next_ is None:
        #         return
        #     elif curr.next_.next_ is None:
        #         curr.next_, self.back = None, curr.next_
        #     else:
        #         curr.next_ = curr.next_.next_
        #     self.size -= 1

    def append(self, value: object) -> None:
        """
        Insert a new LinkedListNode with value after self.back.

        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> lnk.size
        1
        >>> print(lnk.front)
        5 ->|
        >>> lnk.append(6)
        >>> lnk.size
        2
        >>> print(lnk.front)
        5 -> 6 ->|
        """
        # create the new node
        new_node = LinkedListNode(value)
        # if the list is empty, the new node is front and back
        if self.size == 0:
            assert self.back is None and self.front is None, "ooops"
            self.front = self.back = new_node
        # if the list isn't empty, front stays the same
        else:
            # change *old* self.back.next_ first!!!!
            self.back.next_ = new_node
            self.back = new_node
        # remember to increase the size
        self.size += 1

        # alternatively...
        # new_node = LinkedListNode(value)
        #
        # if self.size == 0:
        #     self.front, self.back = new_node, new_node
        # else:
        #     self.back.next_ = new_node
        #     self.back = new_node
        #
        # self.size += 1

    def prepend(self, value: object) -> None:
        """
        Insert value before LinkedList self.front.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> str(lnk.front)
        '2 -> 1 -> 0 ->|'
        >>> lnk.size
        3
        """
        # Remember to change 3 things: front, back, and size
        # Create new node with next_ referring to front
        new_node = LinkedListNode(value, self.front)
        # change front
        self.front = new_node
        # if the list was empty, change back
        if self.size == 0:
            self.back = new_node
        # update size
        self.size += 1

        # alternatively...
        # new_node = LinkedListNode(value)
        # if self.size == 0:
        #     self.front, self.back = new_node, new_node
        # else:
        #     new_node.next_ = self.front
        #     self.front = new_node
        # self.size += 1

    def delete_front(self) -> None:
        """
        Delete LinkedListNode self.front from self.

        Assume self.front is not None

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.delete_front()
        >>> str(lnk.front)
        '1 -> 0 ->|'
        >>> lnk.size
        2
        >>> lnk.delete_front()
        >>> lnk.delete_front()
        >>> str(lnk.front)
        'None'
        >>> lnk.front is None
        True
        >>> lnk.back is None
        True
        >>> lnk.size == 0
        True
        >>>
        """
        assert self.front is not None, "unexpected None!"
        # if back == front, set it to None. (The size is 1)
        if self.front == self.back:
            self.back = None
        # set front to its successor
        self.front = self.front.next_
        # decrease size
        self.size -= 1

        # alternatively...
        # if self.front is None:
        #     raise IndexError('None!')
        #
        # if self.size == 1:
        #     self.front, self.back = None, None
        # else:
        #     self.front = self.front.next_
        #
        # self.size -= 1

    def __setitem__(self, index: int, value: object) -> None:
        """
        Set the value of list at position index to value. Raise IndexError
        if index >= self.size or index < -self.size

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> print(lnk)
        5 ->| Size: 1
        >>> lnk[0] = 7
        >>> print(lnk)
        7 ->| Size: 1
        >>> lnk.append(1)
        >>> lnk.append(1)
        >>> lnk[1] = 8
        >>> lnk[2] = 9
        >>> print(lnk)
        7 -> 8 -> 9 ->| Size: 3
        """
        if index < 0:
            index += self.size
        if index < 0 or index >= self.size or self.size == 0:
            raise IndexError('Index out of range.')
        # In some situations, it is stronger to use remove's while condition in
        # my_linked_list.py
        curr_node = self.front
        curr_index = 0
        while curr_node is not None and curr_index != index:
            curr_node = curr_node.next_
            curr_index += 1
        assert curr_node is not None, 'Problem'
        curr_node.value = value

        # alternatively...
        # if index < 0:
        #     index += self.size
        # if index < 0 or index >= self.size or self.size == 0:
        #     raise IndexError('Not in range.')
        #
        # curr_node = self.front
        # curr_i = 0
        # while curr_node is not None and curr_i < index:
        #     #  for _ in range(index) will also work.
        #     curr_node = curr_node.next_
        #     curr_i += 1
        #
        # # curr_node should not be None here from our if cases
        # assert curr_node is not None
        # if curr_i == index:  # This isn't really needed.
        #     curr_node.value = value

    def __add__(self, other: 'LinkedList') -> 'LinkedList':
        """
        Return a new list by concatenating self to other.  Leave
        both self and other unchanged.

        >>> lnk1 = LinkedList()
        >>> lnk1.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(7)
        >>> print(lnk1 + lnk2)
        5 -> 7 ->| Size: 2
        >>> print(lnk1)
        5 ->| Size: 1
        >>> lnk3 = lnk1 + lnk2
        >>> lnk3.size == lnk1.size + lnk2.size
        True
        """
        new_ll = LinkedList()
        curr_node = self.front
        while curr_node is not None:
            new_ll.append(curr_node.value)
            curr_node = curr_node.next_
        curr_node = other.front
        while curr_node is not None:
            new_ll.append(curr_node.value)
            curr_node = curr_node.next_
        # Append updates the size of the new LL.
        return new_ll

    def insert_before(self, value1: object, value2: object) -> None:
        """
        Insert value1 into LinkedList self before the first occurrence
        of value2, if it exists.  Otherwise leave self unchanged.

        >>> lnk1 = LinkedList()
        >>> lnk1.append(1)
        >>> lnk1.append(2)
        >>> lnk1.append(3)
        >>> lnk1.append(4)
        >>> lnk1.insert_before(9999999, 3)
        >>> print(lnk1)
        1 -> 2 -> 9999999 -> 3 -> 4 ->| Size: 5
        """
        new_node = LinkedListNode(value1)
        prev_node = curr_node = self.front
        while curr_node is not None and curr_node.value != value2:
            prev_node = curr_node
            curr_node = curr_node.next_
        if curr_node.value == value2:
            new_node.next_ = curr_node
            prev_node.next_ = new_node
            self.size += 1

    def copy(self) -> 'LinkedList':
        """
        Return a copy of LinkedList self.  The copy should have
        different nodes, but equivalent values, from self.

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk.prepend(7)
        >>> print(lnk.copy())
        7 -> 5 ->| Size: 2
        """
        new_ll = LinkedList()
        curr_node = self.front
        while curr_node is not None:
            new_ll.append(curr_node.value)
            curr_node = curr_node.next_
        # Don't need to update size because append updates the size.
        return new_ll

    def __len__(self) -> int:
        """
        Return the number of nodes in LinkedList self.

        >>> lnk = LinkedList()
        >>> lnk.append(1)
        >>> lnk.append(2)
        >>> lnk.append(3)
        >>> len(lnk)
        3
        >>> lnk.delete_front()
        >>> len(lnk) == 2
        True
        """
        return self.size

    def __getitem__(self, index: int) -> object:
        """
        Return the value at LinkedList self's position index.

        See __getitem__ in my_linked_list.py

        >>> lnk = LinkedList()
        >>> lnk.append(1)
        >>> lnk.append(0)
        >>> lnk.__getitem__(1)
        0
        >>> lnk[-1]
        0
        >>> lnk[0]
        1
        >>> lnk.append(99)
        >>> lnk[2]
        99
        """
        # deal with a negative index by adding self.size
        if -self.size > index or index > self.size:
            raise IndexError("out of range!")
        elif index < 0:
            index += self.size
        current_node = self.front
        # walk index steps along from 0 to retrieve element
        for _ in range(index):
            assert current_node is not None, "unexpected None!"
            current_node = current_node.next_
        # return the value at position index
        return current_node.value

        # alternatively...
        # if index < 0:
        #     index += self.size
        # if index < 0 or index >= self.size or self.size == 0:
        #     raise IndexError('Index out of range.')
        #
        # curr_node = self.front
        # curr_i = 0
        # # for _ in range(index):
        # while curr_node is not None and curr_i < index:
        #     curr_node = curr_node.next_
        #     curr_i += 1
        #
        # #  curr_node should not be None here bc of if blocks
        # assert curr_node is not None
        # return curr_node.value

    def __contains__(self, value: object) -> bool:
        """
        Return whether LinkedList self contains value.

        >>> lnk = LinkedList()
        >>> lnk.append(0)
        >>> lnk.append(1)
        >>> lnk.append(2)
        >>> 2 in lnk
        True
        >>> lnk.__contains__(3)
        False
        """
        current_node = self.front
        # "walk" the linked list
        while current_node is not None:
            # if any node has a value == value, return True
            if current_node.value == value:
                return True
            current_node = current_node.next_
        # if you get to the end without finding value,
        # return False
        return False

        # alternatively...
        # curr_node = self.front
        # while curr_node is not None and curr_node.value != value:
        #     curr_node = curr_node.next_
        #
        # if curr_node is not None:
        #     return curr_node.value == value  # return True
        # return False

    def pop(self, index: int) -> object:
        """Remove and return the item at position <index>.

        Raise IndexError if index >= len(self) or index < 0.

        >>> lst = LinkedList()
        >>> lst.append(1)
        >>> lst.append(2)
        >>> lst.append(10)
        >>> lst.append(200)
        >>> lst.pop(1)
        2
        >>> lst.pop(2)
        200
        >>> lst.pop(148)
        Traceback (most recent call last):
        IndexError
        >>> lst.pop(0)
        1
        """
        # What if you popped the first item, or the the last in the LL??
        # have to change the front and back
        if index < 0:
            index += self.size
        if index < 0 or index >= self.size or self.size == 0:
            raise IndexError

        if index == 0:
            value = self.front.value
            self.delete_front()
            return value
        elif index == self.size - 1:
            value = self.back.value
            self.delete_back()
            return value

        curr_node = self.front
        prev_node = self.front
        curr_i = 0
        while curr_node is not None and curr_i < index:
            prev_node = curr_node
            curr_node = curr_node.next_
            curr_i += 1

        assert curr_node is not None
        if curr_i == index:  # Not necessary
            value = curr_node.value
            prev_node.next_ = curr_node.next_  # or prev_node.next_.next_
            self.size -= 1
            return value

    def insert(self, index: int, item: object) -> None:
        """Insert a new node containing item at position <index>.

        Raise IndexError if index > len(self) or index < 0.
        Note that adding to the end of a linked list is okay.

        >>> lst = LinkedList()
        >>> lst.append(1)
        >>> lst.append(2)
        >>> lst.append(10)
        >>> lst.append(200)
        >>> lst.insert(2, 300)
        >>> str(lst)
        '1 -> 2 -> 300 -> 10 -> 200 ->| Size: 5'
        >>> lst.insert(5, -1)
        >>> str(lst)
        '1 -> 2 -> 300 -> 10 -> 200 -> -1 ->| Size: 6'
        >>> lst.insert(100, 2)
        Traceback (most recent call last):
        IndexError: Index out of range.
        """
        new_node = LinkedListNode(item)
        if index < 0:
            index += self.size
        if index < 0 or index > self.size:
            raise IndexError('Index out of range.')

        if index == 0:
            self.prepend(item)
            return
        elif index == self.size:
            self.append(item)
            return

        curr_node, prev_node = self.front, self.front
        curr_i = 0
        while curr_node is not None and curr_i < index:
            prev_node = curr_node
            curr_node = curr_node.next_
            curr_i += 1

        assert curr_node is not None
        new_node.next_ = curr_node
        prev_node.next_ = new_node
        self.size += 1

    def remove(self, item: object) -> None:
        """Remove the FIRST occurrence of <item> in this list.

        Do nothing if this list does not contain <item>.

        >>> lst = LinkedList()
        >>> lst.append(1)
        >>> lst.append(2)
        >>> lst.append(10)
        >>> lst.append(200)
        >>> lst.remove(1)
        >>> lst.remove(2)
        >>> print(lst)
        10 -> 200 ->| Size: 2
        >>> lst.remove(0)
        >>> print(lst)
        10 -> 200 ->| Size: 2
        """
        if self.size == 0:
            return
        if self.front.value == item:
            self.delete_front()
            return
        elif self.back.value == item:
            self.delete_back()
            return

        curr_node, prev_node = self.front, self.front
        while curr_node is not None and curr_node.value != item:
            prev_node = curr_node
            curr_node = curr_node.next_

        if curr_node is None:
            return

        else:
            prev_node.next_ = curr_node.next_
            self.size -= 1

    def pop_front(self):
        """
        Remove self.front and return its value. Assume
        self.size >= 1

        >>> lnk = LinkedList()
        >>> lnk.append(0)
        >>> lnk.append(1)
        >>> lnk.pop_front()
        0
        """
        value = self.front.value
        self.delete_front()
        return value

    def delete_back(self) -> None:
        """ Delete the last item of the linked list.
        """
        if self.size == 0:
            raise IndexError('Index out of range.')
        elif self.size == 1:
            self.front, self.back, self.size = None, None, 0

        curr_node, prev_node = self.front, self.front
        while curr_node is not None:
            prev_node = curr_node
            curr_node = curr_node.next_

        assert curr_node is None
        self.back = prev_node
        prev_node.next_ = None
        self.size -= 1

    def extend(self, items: list) -> None:
        """Extend this list by appending elements from <items>.

        >>> lst = LinkedList()
        >>> lst.append(1)
        >>> lst.append(2)
        >>> lst.append(3)
        >>> str(lst)
        '1 -> 2 -> 3 ->| Size: 3'
        >>> lst.extend([4, 5, 6, 7])
        >>> str(lst)
        '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 ->| Size: 7'
        """
        curr_node = self.front
        prev_node = curr_node
        while curr_node is not None:
            prev_node = curr_node
            curr_node = curr_node.next_

        assert curr_node is None
        for item in items:
            prev_node.next_ = LinkedListNode(item)
            prev_node = prev_node.next_
        self.back = prev_node
        self.size += len(items)

    def map(self, f: Callable[[object], object]) -> 'LinkedList':
        """Return a new LinkedList whose nodes store items that are
        obtained by applying f to each item in this linked list.

        Do not change this linked list.

        For extra practice, do not store items in a Python list; instead,
        use only the LinkedList and _Node classes.

        >>> func = str.upper
        >>> func('hi')
        'HI'
        >>> lst = LinkedList()
        >>> lst.append('Hello')
        >>> lst.append('Goodbye')
        >>> str(lst.map(func))
        'HELLO -> GOODBYE ->| Size: 2'
        >>> str(lst.map(len))
        '5 -> 7 ->| Size: 2'
        """
        new_ll = LinkedList()
        curr = self.front
        while curr is not None:
            val = f(curr.value)
            new_ll.append(val)
            curr = curr.next_
        return new_ll

    def filter(self, f: Callable[[object], bool]) -> 'LinkedList':
        """Return a new LinkedList whose nodes store the items in this
        linked list that make f return True.

        Do not change this linked list.

        For extra practice, do not store items in a Python list; instead,
        use only the LinkedList and _Node classes.

        >>> func = str.islower
        >>> func('hi')
        True
        >>> func('Hi')
        False
        >>> lst = LinkedList(['Hello', 'goodbye', 'see you later'])
        >>> str(lst.filter(func))
        'goodbye -> see you later ->| Size: 2'
        """
        new_ll = LinkedList()

        curr = self.front
        while curr is not None:
            if f(curr.value):
                val = curr.value
                new_ll.append(val)
            curr = curr.next_

        return new_ll

    def clear(self) -> None:
        """Remove all items from this list.

        >>> lst = LinkedList([1, 2, 3])
        >>> str(lst)
        '1 -> 2 -> 3 ->| Size: 3'
        >>> lst.clear()
        >>> str(lst)
        'Empty!'
        """
        self.front, self.back, self.size = None, None, 0

    # Midterm 1 2018 Heap
    def sum(self) -> int:
        """ Return sum of int values in LinkedList self.
        Raise LinkedListException if any value is not an int.

        >>> lnk1 = LinkedList()
        >>> lnk1.prepend(1)
        >>> isinstance(lnk1.front.value, int)
        True
        >>> lnk1.prepend(2)
        >>> lnk1.sum()
        3
        """
        count = 0
        curr = self.front
        while curr is not None:
            if not isinstance(curr.value, int):
                raise LinkedListException
            count += curr.value
            curr = curr.next_

        return count

    def concat(self, other: "LinkedList") -> None:
        """ Concatenates other into self and sets other to contain no values.
        (that is, other should have its .front attribute None)
        Raise exception if other starts empty.

        >>> lnk1 = LinkedList()
        >>> lnk1.prepend(2)
        >>> lnk1.prepend(1)
        >>> lnk1.prepend(0)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(5)
        >>> lnk2.prepend(4)
        >>> lnk2.prepend(3)
        >>> lnk1.concat(lnk2)
        >>> print(lnk1.front)
        0 -> 1 -> 2 -> 3 -> 4 -> 5 ->|
        >>> print(lnk2.front)
        None
        """
        # if other.front is None:
        #     raise LinkedListException
        #
        # if self.size == 0:
        #     self.front = other.front
        # else:
        #     self.back.next_ = other.front
        #
        # self.back = other.back
        # self.size += other.size
        # other.front, other.back, other.size = None, None, 0

        # Version 2
        if other.front is None:
            raise LinkedListException

        if self.size == 0:
            self.front = other.front
            self.back = other.back
            self.size += other.size
        else:
            self.back.next_ = other.front
            self.back = other.back
            self.size += other.size

        other.front, other.back, other.size = None, None, 0

    def swap(self, other: 'LinkedList') -> None:
        """ Swaps the values of two Linked Lists, leaving node ids intact.
        Raise LinkedListException if lists are different sizes.

        >>> lnk1 = LinkedList()
        >>> lnk1.prepend(0)
        >>> lnk1.prepend(1)
        >>> lnk1.prepend(2)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(3)
        >>> lnk2.prepend(4)
        >>> lnk2.prepend(5)
        >>> lnk1.swap(lnk2)
        >>> print(lnk1.front)
        5 -> 4 -> 3 ->|
        >>> print(lnk2.front)
        2 -> 1 -> 0 ->|
        """
        if self.size != other.size:
            raise LinkedListException('Not the same size!')

        # General case
        curr_s, curr_o = self.front, other.front
        while curr_s is not None and curr_o is not None:
            # Swap the values
            curr_s.value, curr_o.value = curr_o.value, curr_s.value
            # Next
            curr_s, curr_o = curr_s.next_, curr_o.next_

    # Midterm 2 Heap
    def remove_first_double(self) -> None:
        """
        Remove second of two adjacent nodes with duplicate values.
        If there is no such node, leave self as is. No need
        to deal with subsequent adjacent duplicate values.
        @param LinkedList self: this linked list
        @rtype: None

        >>> list_ = LinkedList()
        >>> list_.append(3)
        >>> list_.append(2)
        >>> list_.append(2)
        >>> list_.append(3)
        >>> list_.append(3)
        >>> print(list_.front)
        3 -> 2 -> 2 -> 3 -> 3 ->|
        >>> list_.remove_first_double()
        >>> print(list_.front)
        3 -> 2 -> 3 -> 3 ->|
        """
        if self.size < 2:
            pass

        prev, curr = None, self.front
        while curr is not None:
            prev, curr = curr, curr.next_

            if prev.value == curr.value:
                if curr is None or curr.next_ is None:
                    prev.next_, self.back = None, prev
                else:
                    prev.next_ = curr.next_

                self.size -= 1
                break

        # Heap's solution
        # if self.size < 2:
        #     # no room for doubles
        #     return None
        #
        # curr = self.front
        # while curr.next_ and curr.value != curr.next_.value:
        #     curr = curr.next_
        #
        # if curr.next_ is not None:      # We are in the middle
        #     # if curr.value == curr.next_.value:
        #     curr.next_ = curr.next_.next_
        #
        # else:                         # if curr.next_ is None: we are at back
        #     self.back = curr
        # self.size -= 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
