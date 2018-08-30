"""Linked list practice

=== CSC148 Winter 2018 ===
University of Toronto,
Computer Science
__author__ = 'Eric Koehli'

=== Module description ===
This module contains some linked list problems of varying difficulty taken
from midterms and finals at UofT.
"""
from my_linked_list_v2 import *
from typing import Any, Tuple


# Heap 2017 Midterm 2
def reverse_list(list_: LinkedList) -> None:
    """
    Reverse the order of the nodes in list_.

    >>> lnk = LinkedList()
    >>> lnk.prepend(1)
    >>> lnk.prepend(3)
    >>> lnk.prepend(5)
    >>> print(lnk)
    5 -> 3 -> 1 ->| Size: 3
    >>> reverse_list(lnk)
    >>> print(lnk)
    1 -> 3 -> 5 ->| Size: 3
    """
    front, back = list_.front, list_.back
    curr, prev = list_.front, None
    while curr is not None:
        curr.next_, prev, curr = prev, curr, curr.next_

    list_.front, list_.back = back, front

    # *** The swap ***
    # next_ = curr.next_
    # curr.next_ = prev
    # prev = curr
    # curr = next_

    # Heap solution:
    # curr = list_.front
    # prev = None
    # tail = list_.front
    # while curr is not None:
    #     curr.next_, curr, prev = prev, curr.next_, curr
    # list_.front, list_.back = prev, tail


def reverse_list_to_value(list_: LinkedList, value: object) -> None:
    """ Does not update size, discards other nodes.
    Reverse the list up to <value>

    >>> lnk = LinkedList()
    >>> lnk.prepend(1)
    >>> lnk.prepend(3)
    >>> lnk.prepend(5)
    >>> print(lnk)
    5 -> 3 -> 1 ->| Size: 3
    >>> reverse_list(lnk)
    >>> print(lnk)
    1 -> 3 -> 5 ->| Size: 3
    >>> lnk.append(6)
    >>> lnk.append(7)
    >>> print(lnk)
    1 -> 3 -> 5 -> 6 -> 7 ->| Size: 5
    >>> reverse_list_to_value(lnk, 5)
    >>> print(lnk)
    5 -> 3 -> 1 ->| Size: 5
    """
    front, back = list_.front, list_.back
    curr, prev = list_.front, None

    while curr is not None and (prev is None or prev.value != value):
        curr.next_, prev, curr = prev, curr, curr.next_

    list_.front, list_.back = prev, front

    # Heap
    # current = list_.front
    # prev = None
    # tail = list_.front
    # while current and (prev is None or prev.value != value):
    #     next_ = current.next_
    #     current.next_ = prev
    #     prev = current
    #     current = next_
    # # Or in one line:
    # # current.next_, current, prev = prev, current.next_, current
    # list_.front, list_.back = prev, tail

    # Mine
    # if list_.size < 2:
    #     pass
    #
    # tail, list_.size = list_.front, 1
    # pre_prev, prev, curr = None, list_.front, list_.front
    # while curr is not None and prev.value != value:
    #     curr.next_, curr, prev = prev, curr.next_, curr
    #     list_.size += 1
    #
    # list_.front, list_.back = prev, tail


def reverse_list_after_value(list_: LinkedList, value: object):
    """ Does not update size, discards other nodes.

    >>> lnk = LinkedList()
    >>> lnk.prepend(1)
    >>> lnk.prepend(3)
    >>> lnk.prepend(5)
    >>> print(lnk)
    5 -> 3 -> 1 ->| Size: 3
    >>> reverse_list(lnk)
    >>> print(lnk)
    1 -> 3 -> 5 ->| Size: 3
    >>> lnk.append(6)
    >>> lnk.append(7)
    >>> print(lnk)
    1 -> 3 -> 5 -> 6 -> 7 ->| Size: 5
    >>> reverse_list_after_value(lnk, 5)
    >>> print(lnk)
    7 -> 6 -> 5 ->| Size: 5
    """
    # if list_.size < 2:
    #     return
    #
    # tail = list_.front
    # prev, curr = None, list_.front
    # while curr is not None and curr.value != value:
    #     prev, curr = curr, curr.next_
    #
    # if curr is None:
    #     return
    #
    # while curr is not None:
    #     prev, curr, curr.next_ = curr, curr.next_, prev
    #
    # list_.front, list_.back = prev, tail

    # Solutin 2
    # curr = list_.front
    # while curr is not None and curr.value != value:
    #     curr = curr.next_
    #
    # if curr is not None:
    #     # WARNING Can't use that if: use if curr is not None:
    #     # if curr.value == value:
    #     prev, tail = None, curr
    #
    #     while curr is not None:  # continue rest of LL
    #         curr.next_, prev, curr = prev, curr, curr.next_
    #     list_.front, list_.back = prev, tail

    # Heap solution
    current = list_.front
    while current and current.value != value:
        current = current.next_
    if current:
        prev = None
        tail = current
        while current:
            next_ = current.next_
            current.next_ = prev
            prev = current
            current = next_
            # Or in one line:
            # current.next_, current, prev = prev, current.next_, current
        list_.front, list_.back = prev, tail


def merge(lst1: LinkedList, lst2: LinkedList) -> None:
    """
    Merge l i s t l and l i s t 2 by placing l i s t 2 ; s nodes into the
    correct position in l i s t l to preserve ordering. When
    complete l i s t l will contain a l l the values from both l i s t s,
    in order, and l i s t 2 will be empty.

    Assume l i s t l and l i s t 2 contain comparable values in nondecreasing
    order

    >>> lst1 = LinkedList()
    >>> lst1.append(1)
    >>> lst1.append(3)
    >>> lst1.append(5)
    >>> lst2 = LinkedList()
    >>> lst2.append(2)
    >>> lst2.append(6)
    >>> merge(lst1, lst2)
    >>> print(lst1.front)
    1 -> 2 -> 3 -> 5 -> 6 ->|
    """
    if lst1.size == 0 or lst2.size == 0:
        pass

    new_ll = LinkedList()

    curr1, curr2 = lst1.front, lst2.front
    while curr1 and curr2:

        if curr1.value <= curr2.value:
            new_ll.append(curr1.value)
            curr1 = curr1.next_
        else:
            new_ll.append(curr2.value)
            curr2 = curr2.next_

    remaining = curr1
    if remaining is None:
        remaining = curr2

    while remaining:
        new_ll.append(remaining.value)
        remaining = remaining.next_

    lst1.front, lst1.back, lst1.size = new_ll.front, new_ll.back, new_ll.size
    lst2.front, lst2.back, lst2.size = None, None, 0


def repeat_items(ll: LinkedList) -> None:
    """
    Repeats all items in ll.

    >>> lnk = LinkedList()
    >>> lnk.append(1)
    >>> lnk.append(2)
    >>> lnk.append(3)
    >>> repeat_items(lnk)
    >>> print(lnk)
    1 -> 1 -> 2 -> 2 -> 3 -> 3 ->| Size: 6
    """
    prev, curr = None, ll.front
    while curr:
        prev, curr = curr, curr.next_
        new = LinkedListNode(prev.value)

        if curr is not None:
            new.next_, prev.next_ = curr, new
        else:
            prev.next_, ll.back = new, new

    ll.size *= 2

    # if ll.size == 0:
    #     pass
    #
    # curr = ll.front
    # while curr is not None:
    #     new_node = LinkedListNode(curr.value)
    #     if curr.next_ is not None:
    #         new_node.next_ = curr.next_
    #         curr.next_ = new_node
    #         curr = new_node.next_
    #     else:
    #         curr.next_, ll.back = new_node, new_node
    #         curr = None
    # ll.size *= 2

    # Sol 2
    # if ll.size == 0:
    #     return None
    # curr = ll.front
    # while curr is not None:
    #     if not curr.next_:
    #         curr.next_ = LinkedListNode(curr.value)
    #         curr = None
    #     else:
    #         nxt = curr.next_
    #         curr.next_ = LinkedListNode(curr.value)
    #         curr.next_.next_ = nxt
    #         curr = nxt


# *** Linked List Skip ***
class LinkedListNodeSkip:
    """ Node to be used in linked list
    """
    value: object
    nxt: 'LinkedListNodeSkip'
    skip: 'LinkedListNodeSkip'

    def __init__(self, value: object, nxt=None) -> None:
        """ Create LinkedListNode self with data value and successor nxt.
        Oparam LinkedListNode self : this LinkedListNode
        Oparam int value: data of this linked list node
        @param LinkedListNodeI None nxt: successor to this LinkedListNode.
        Srtype: None
        """
        self.value, self.nxt = value, nxt
        if nxt is not None:
            self.skip = nxt.nxt
        else:
            self.skip = None

    def __str__(self) -> str:
        """
        Oparam LinkedListNode self : this LinkedListNode
        Ortype: str

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print (n)
        5 -> 7 ->|
        """
        s = "{} ->" .format(self .value)
        curr = self
        while curr is not None:
            if curr.nxt is None:
                s += "|"
            else:
                s += " {} ->".format(curr.nxt.value)
                curr = curr.nxt
        return s


class LinkedListSkip:
    """ Collection of LinkedListNodes

    === Attributes ==
    Qparam: LinkedListNode front: first node of this LinkedList
    Oparam LinkedListNode back: last node of this LinkedList
    Qparam int size: number of nodes in this LinkedList a non-negative integer
    """

    def __init__(self) -> None:
        """
        create an empty linked list.
        Sparam LinkedList self: this LinkedList
        Ortype: None
        """
        self.front, self.back = None, None
        self.size = 0

    def __str__(self) -> str:
        """

        """
        return str(self.front)

    def precursors(self, value: int) -> Tuple[Any, Any]:
        """
        Returns a tuple containing the two list nodes with the two highest
        values which are less than the method argument 'value'.

        >>> lnk = LinkedListSkip()
        >>> lnk.precursors(3)
        (None, None)
        >>> a = LinkedListNodeSkip(3)
        >>> lnk.front, lnk.back, lnk.size = a, a, 1
        >>> lnk.precursors(1)
        (None, None)
        >>> b = LinkedListNodeSkip(1, a)
        >>> lnk.front, lnk.size = b, 2
        >>> pre1 = lnk.precursors(5)[0]
        >>> pre2 = lnk.precursors(5)[1]
        >>> pre1.value, pre2.value
        (1, 3)
        """
        if self.size < 2:
            return (None, None)

        pre_prev, prev, curr = None, None, self.front
        while curr is not None and curr.value != value:
            pre_prev, prev, curr = prev, curr, curr.nxt

        return pre_prev, prev

        # if self.size < 2:
        #     return (None, None)
        #
        # curr, prev, pre_prev = self.front, None, None
        # while curr is not None and curr.value != value:
        #     pre_prev = prev
        #     prev = curr
        #     curr = curr.nxt
        #
        # # WARNING: You cannot do this if condition because curr could be None
        # # if curr.value == value:
        # if curr is not None:
        #     return (pre_prev, prev)
        # else:
        #     # value isn't in the LL, so apparently just return the last two
        #     return (pre_prev, prev)

    def insert(self, value: int, prev: LinkedListNodeSkip,
               curr: LinkedListNodeSkip) -> None:
        """
        Inserts a new node with value after node cur.
        Updates all links correctly. This is a method of class LinkedList.

        >>> lnk = LinkedListSkip()
        >>> lnk.insert(3, lnk.precursors(3)[0], lnk.precursors(3)[1])
        >>> lnk.insert(0, lnk.precursors(0)[0], lnk.precursors(0)[1])
        >>> lnk.insert(2, lnk.precursors(2) [0], lnk.precursors(2)[1])
        >>> lnk.insert(1, lnk.precursors(1)[0], lnk.precursors(1)[1])
        >>> print(lnk.front)
        0 -> 1 -> 2 -> 3 ->|
        >>> print(lnk.back)
        3 ->|
        >>> lnk.size
        4
        >>> print(lnk.front.skip)
        2 —> 3 —>|
        >>> print(lnk.front.nxt.skip)
        3 ->|
        """
        new = LinkedListNodeSkip(value)

        # Deal with the front
        if curr is None:
            self.front, self.back = new, new
        elif prev is None:
            self.front, self.back, curr.nxt = curr, new, new
        # Deal with the back
        elif curr.nxt is None:
            prev.skip, curr.nxt, self.back = new, new, new
        elif curr.skip is None:
            new.nxt, prev.skip, curr.nxt, curr.skip = curr.nxt, new, new, \
                                                      curr.nxt
        # Middle
        else:
            new.nxt, new.skip, prev.skip, curr.nxt, curr.skip = curr.nxt, \
                                                                curr.nxt.nxt, \
                                                                new, new, \
                                                                curr.nxt
        # update size
        self.size += 1

        # Don't think there is enough updates in this solution
        # new_node = LinkedListNodeSkip(value)
        #
        # if prev is None:
        #     self.front, self.back = new_node, new_node
        #
        # elif curr is None:
        #     self.front, self.back = prev, new_node
        #
        # elif curr.nxt is None:
        #     # Then we are inserting at the end of the list.
        #     # new_node.nxt, new_node.skip = None, None     by default
        #     prev.skip, curr.nxt = new_node, new_node
        #     self.back = new_node
        #
        # elif curr.skip is None:
        #     # Then we are inserting in the second last position
        #     new_node.nxt, new_node.skip = curr.nxt, None
        #     prev.skip, curr.nxt, curr.skip = new_node, new_node, curr.nxt
        #
        # else:
        #     new_node.nxt, new_node.skip = curr.nxt, curr.nxt.nxt
        #     prev.skip, curr.nxt, curr.skip = new_node, new_node, curr.nxt
        #
        # self.size += 1

        # Old sol
        # if curr is None:
        #     new_node = LinkedListNodeSkip(value)
        #     if prev is None:
        #         self.front, self.back, self.size = new_node, new_node, 1
        #     else:
        #         self.front, self.back, self.size = prev, new_node, 2
        # else:
        #     new_node = LinkedListNodeSkip(value, curr.nxt)
        #     new_node.skip = curr.nxt
        #     curr.nxt, curr.skip = new_node, curr.nxt
        #     prev.skip = new_node
        #     self.size += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
