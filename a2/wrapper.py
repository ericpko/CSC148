""" A Tree-like ADT

=== CSC148 Winter 2018 ===
University of Toronto,
Computer Science
Assignment 2
__author__ = 'Eric Koehli'

=== Module Description ===
This module contains a simple Tree-like data structure to be used
for assignment 2.
Note: Of course, I didn't need to implement all these methods, but who
doesn't like more practice with trees!
"""
from typing import List, Any, Optional


class Wrapper:
    """
    A bare-bones Wrapper ADT that identifies the root with the entire Wrapper.

    === Public attributes ===
    state:
         This is the root/node of the Wrapper and contains a game state.
         Type contract left as object, to be more general.
    children:
         This is a list of the children of the Wrapper.
    score:
         A score of either 1 or -1 to be used for games
    move:
         The move that was applied to get to this game state.
    """
    state: object
    children: List['Wrapper']
    score: Optional[int]
    move: Optional[str]

    def __init__(self, state: object = None, children: List['Wrapper'] = None,
                 score: int = None, move: str = None) -> None:
        """
        Create Wrapper self with content state and 0 or more children
        """
        self.state, self.score, self.move = state, score, move
        self.children = children[:] if children is not None else []
        assert self.children == [] if state is None else True

    def is_empty(self) -> bool:
        """
        Return true iff <self> Wrapper is empty.
        """
        return self.state is None

    def __repr__(self) -> str:
        """
        Return representation of Wrapper (self) as string that
        can be evaluated into an equivalent Wrapper.

        >>> t1 = Wrapper(5)
        >>> t1
        Wrapper(5)
        >>> t2 = Wrapper(7, [t1])
        >>> t2
        Wrapper(7, [Wrapper(5)])
        """
        # Our __repr__ is recursive, because it can also be called
        # via repr...!
        if self.state is None:
            return ''
        elif self.children == []:
            return 'Wrapper({})'.format(repr(self.state))

        return 'Wrapper({}, {})'.format(repr(self.state), repr(self.children))

    def __eq__(self, other: Any) -> bool:
        """
        Return whether this Wrapper is equivalent to other.
        >>> t1 = Wrapper(5)
        >>> t2 = Wrapper(5, [])
        >>> t1 == t2
        True
        >>> t3 = Wrapper(5, [t1])
        >>> t2 == t3
        False
        """
        return (type(self) is type(other) and
                self.state == other.state and
                self.children == other.children)

    def __str__(self, indent: int = 0) -> str:
        """
        Produce a user-friendly string representation of Wrapper self,
        indenting each level as a visual clue.

        >>> t = Wrapper(17)
        >>> print(t)
        17
        >>> t1 = Wrapper(19, [t, Wrapper(23)])
        >>> print(t1)
        19
           17
           23
        >>> t3 = Wrapper(29, [Wrapper(31), t1])
        >>> print(t3)
        29
           31
           19
              17
              23
        """
        root_str = indent * ' ' + str(self.state)
        return '\n'.join([root_str] +
                         [s.__str__(indent + 3) for s in self.children])

    def __len__(self) -> int:
        """Return the number of nodes contained in this Wrapper.

        >>> t1 = Wrapper(None, [])
        >>> len(t1)
        0
        >>> t2 = Wrapper(3, [Wrapper(4, []), Wrapper(1, [])])
        >>> len(t2)
        3
        >>> t3 = Wrapper(18, [Wrapper(55, []), \
                        Wrapper(3, [Wrapper(4, []), Wrapper(1, [])])])
        >>> t3.__len__()
        5
        """
        if self.state is None:
            return 0
        # we don't need to distinguish between a leaf or a middle node.
        return 1 + sum(s.__len__() for s in self.children)

    def __contains__(self, item: object) -> bool:
        """Return whether <item> is in this Wrapper.

        >>> t = Wrapper(1, [Wrapper(2, []), Wrapper(5, [])])
        >>> 1 in t  # Same as t.__contains__(1)
        True
        >>> 5 in t
        True
        >>> 4 in t
        False
        >>> t2 = Wrapper(4, [t])
        >>> 5 in t2
        True
        >>> 4 in t2
        True
        >>> 3 in t2
        False
        """
        if self.is_empty():
            return False
        else:
            # Don't need to distinguish between leafs and internal nodes.
            if self.state == item:
                return True

            return any(s.__contains__(item) for s in self.children)

    def height(self) -> int:
        """Return the height of this Wrapper.

        >>> t1 = Wrapper(None, [])
        >>> t1.height()
        0
        >>> t2 = Wrapper(3, [Wrapper(4, []), Wrapper(1, [])])
        >>> t2.height()
        2
        >>> t3 = Wrapper(18, [Wrapper(55, []), \
                        Wrapper(3, [Wrapper(4, []), Wrapper(1, [])])])
        >>> t3.height()
        3
        """
        if self.is_empty():
            return 0
        elif self.children == []:
            # Then we are at a leaf -> or it's a Wrapper with a single root.
            return 1

        # There is a list of subtrees, but we still need to count the
        # root's value as well, so add 1 + max
        return 1 + max(s.height() for s in self.children)

    def count(self, item: object) -> int:
        """Return the number of occurrences of <item> in this Wrapper.

        >>> t = Wrapper(3, [Wrapper(4, []), Wrapper(1, [])])
        >>> t.count(3)
        1
        >>> t.count(100)
        0
        >>> bigger = Wrapper(19, [ \
                Wrapper(3, [Wrapper(4, []), Wrapper(1, [])]), \
                Wrapper(3, [Wrapper(4, []), Wrapper(4, [])]) \
                ])
        >>> bigger.count(4)
        3
        """
        if self.state is None:
            return 0

        # Don't need to distinguish leafs from internal nodes.
        if self.state == item:
            return 1

        return sum(s.count(item) for s in self.children)

    def leaves(self) -> list:
        """Return a list of all of the leaf items in the Wrapper.

        >>> Wrapper(None, []).leaves()
        []
        >>> t = Wrapper(1, [Wrapper(2, []), Wrapper(5, [])])
        >>> t.leaves()
        [2, 5]
        >>> lt = Wrapper(2, [Wrapper(4, []), Wrapper(5, [])])
        >>> rt = Wrapper(3, [Wrapper(6, []), Wrapper(7, [])])
        >>> t = Wrapper(1, [lt, rt])
        >>> t.leaves()
        [4, 5, 6, 7]
        """
        if self.state is None:
            return []
        elif self.children == []:
            # Then we're at a leaf!
            return [self.state]

        return sum([s.leaves() for s in self.children], [])

    def leaf_count(self) -> int:
        """Return the number of leaves in this Wrapper.

        >>> Wrapper(None, []).leaf_count()
        0
        >>> t = Wrapper(1, [Wrapper(2, []), Wrapper(5, [])])
        >>> t.leaf_count()
        2
        >>> lt = Wrapper(2, [Wrapper(4, []), Wrapper(5, [])])
        >>> rt = Wrapper(3, [Wrapper(6, []), Wrapper(7, [])])
        >>> t = Wrapper(1, [lt, rt])
        >>> t.leaf_count()
        4
        """
        if self.state is None:
            return 0
        elif self.children == []:
            # Then we're at a leaf.
            return 1

        # We are at an internal node
        return sum(s.leaf_count() for s in self.children)

    def arity(self) -> int:
        """Return the maximum branching factor (arity) of Wrapper t.

        >>> Wrapper().arity()
        0
        >>> t = Wrapper(23)
        >>> t.arity()
        0
        >>> tn2 = Wrapper(2, [Wrapper(4), Wrapper(4.5), Wrapper(5), \
Wrapper(5.75)])
        >>> tn3 = Wrapper(3, [Wrapper(6), Wrapper(7)])
        >>> tn1 = Wrapper(1, [tn2, tn3])
        >>> tn1.arity()
        4
        """
        if self.is_empty():
            return 0
        elif self.children == []:
            # Then we're at a leaf -> or a Wrapper with a single root.
            return 0

        return max(len(self.children), max(s.arity() for s in self.children))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
