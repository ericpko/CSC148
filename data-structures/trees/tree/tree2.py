"""Tree

=== CSC148 Winter 2018 ===
Department of Computer Science,
University of Toronto
__author__ = 'Eric K'

=== Module Description ===
This module contains a simple tree implementation as well some related
tree functions.
"""
from typing import Any, List
from queue_api import Queue


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.

    === Public attributes ===
    value: This is the root/node of the tree and has a value.
    children: This is a list of the subtrees of the tree.
    """
    value: Any
    children: List['Tree']

    def __init__(self, value: object = None,
                 children: List['Tree'] = None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        self.children = children[:] if children is not None else []
        if self.value is None:
            assert self.children == []

    def is_empty(self) -> bool:
        """
        Return true iff <self> Tree is empty.
        """
        return self.value is None

    def __repr__(self) -> str:
        """
        Return a representation of Tree <self> as string that
        can be evaluated into an equivalent Tree.

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        # Our __repr__ is recursive because it can also be called via repr...!
        if self.value is None:
            return ''
        elif self.children == []:
            return f'Tree({self.value})'
        else:
            return f'Tree({repr(self.value)}, {repr(self.children)})'

        # or with 'Tree({}, {})'.format(...)
        # if self.value is None:
        #     return ''
        # elif len(self.children) == 0:
        #     return 'Tree({})'.format(repr(self.value))
        # else:
        #     return 'Tree({}, {})'.format(repr(self.value),
        #                                  repr(self.children))

    def __eq__(self, other: Any) -> bool:
        """
        Return whether this Tree is equivalent to other.
        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        """
        return (type(self) is type(other) and
                self.value == other.value and
                self.children == other.children)

    # def __str__(self, indent: int=0) -> str:
    #     """
    #     Produce a user-friendly string representation of Tree self,
    #     indenting each level as a visual clue.
    #
    #     >>> t = Tree(17)
    #     >>> print(t)
    #     17
    #     >>> t1 = Tree(19, [t, Tree(23)])
    #     >>> print(t1)
    #        23
    #     19
    #        17
    #     >>> t3 = Tree(29, [Tree(31), t1])
    #     >>> print(t3)
    #           23
    #        19
    #           17
    #     29
    #        31
    #     """
    #     root_str = indent * ' ' + str(self.value)
    #     mid = len(self.list_internal_trees()) // 2
    #     left_str = [c.__str__(indent + 3)
    #                 for c in self.list_internal_trees()][:mid]
    #     right_str = [c.__str__(indent + 3)
    #                  for c in self.list_internal_trees()][mid:]
    #     return '\n'.join(right_str + [root_str] + left_str)

    def list_internal_trees(self) -> List['Tree']:
        """ Return a list of Tree self's non-None children.
        These are all internal nodes.

        """
        if self.value is None:
            return []
        elif self.children == []:
            return []
        else:
            return [self] + sum([s.list_internal_trees()
                                 for s in self.children], [])

    def __str__(self, indent: int=0) -> str:
        """
        Produce a simple user-friendly string representation of Tree self,
        indenting each level as a visual clue.

        >>> t = Tree(17)
        >>> print(t)
        17
        >>> t1 = Tree(19, [t, Tree(23)])
        >>> print(t1)
        19
           17
           23
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
        29
           31
           19
              17
              23
        """
        root_str = indent * ' ' + str(self.value)
        return '\n'.join([root_str] +
                         [s.__str__(indent + 3) for s in self.children])

    def is_leaf(self) -> bool:
        """Return whether Tree self is a leaf

        >>> Tree(5).is_leaf()
        True
        >>> Tree(5,[Tree(7)]).is_leaf()
        False
        """
        if self.value is None:
            return False
        return self.children == []

        # or...
        # if self.value is None:
        #     return False
        # elif self.children == []:
        #     return True
        # else:
        #     return False

    def __contains__(self, value: object) -> bool:
        """
        Return whether Tree self contains v.

        >>> t = Tree(17)
        >>> t.__contains__(17)
        True
        >>> t = descendants_from_list(Tree(19), [1, 2, 3, 4, 5, 6, 7], 3)
        >>> t.__contains__(3)
        True
        >>> t.__contains__(18)
        False
        >>> t.__contains__(19)
        True
        """
        if self.value is None:
            return False
        elif self.value == value:
            return True
        else:
            return any(s.__contains__(value) for s in self.children)

        # if self.value is None:
        #     return False
        # else:
        #     return True if self.value == value else any(s.__contains__(value)
        #                                                for s in self.children)

    def height(self) -> int:
        """
        Return length of longest path, + 1, in tree rooted at self.

        >>> t = Tree(5)
        >>> t.height()
        1
        >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
        >>> t.height()
        3
        """
        if self.value is None:
            return 0
        elif self.children == []:
            return 1
        else:
            return 1 + max(s.height() for s in self.children)

    def flatten(self) -> list:
        """ Return a list of all values in tree rooted at self.

        >>> t = Tree(5)
        >>> t.flatten()
        [5]
        >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
        >>> L = t.flatten()
        >>> L
        [7, 0, 5, 7, 9, 1, 11, 13, 3]
        >>> L.sort()
        >>> L == [0, 1, 3, 5, 7, 7, 9, 11, 13]
        True
        """
        if self.value is None:
            return []
        else:
            return [self.value] + sum([s.flatten() for s in self.children], [])


# Helper function for doctests
def descendants_from_list(t: Tree, list_: list, branching: int) -> Tree:
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to arity children per node.
    Then return t.

    This is a helper function for doctests

    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()

    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        new_t: Tree
        for _ in range(0, branching):
            if len(list_) == 0:
                return t  # our work here is done
            else:
                new_t_child = Tree(list_.pop(0))
                new_t.children.append(new_t_child)
                q.add(new_t_child)
    return t


if __name__ == '__main__':
    import doctest
    doctest.testmod()
