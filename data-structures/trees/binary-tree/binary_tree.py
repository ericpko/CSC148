""" A simple BinaryTree class

=== University of Toronto ===
Department of Computer Science
__author__ = 'Eric K'

=== Module Description ===
This module contains a simple BinaryTree implementation.
"""
from typing import Optional, Any


class EmptyBinaryTreeError(Exception):
    """
    Raises an exception when a binary tree is empty.
    """


#  TODO: implement other methods from the Tree class
class BinaryTree:
    """
    A class representing a binary tree.

    A binary tree is either empty, or a root connected to
    a *left* binary tree and a *right* binary tree (which could be empty).
    """
    # === Private Attributes ===
    _root: Optional[object]
    _left: Optional['BinaryTree']
    _right: Optional['BinaryTree']

    # === Representation Invariants ===
    # _root, _left, _right are either ALL None, or none of them are None.
    #   If they are all None, this represents an empty BinaryTree.

    # === Traversal Template ===
    # if self._root is None:
    #   # Then we're at a leaf in a binary tree
    #   ...
    # else:
    #   # We are at an internal node:
    #   # recursive call on self._left, self._right
    #   ...

    def __init__(self, root: Optional[object], left: Optional['BinaryTree'],
                 right: Optional['BinaryTree']) -> None:
        """Initialise a new binary tree with the given values.

        If <root> is None, this represents an empty BinaryTree
        (<left> and <right> are ignored in this case).

        Precondition: if <root> is not None, then neither <left> nor <right>
                      are None.
        """
        if root is None:
            # Store an empty binary tree.
            self._root, self._left, self._right = None, None, None
        else:
            self._root = root
            self._left, self._right = left, right

    def is_empty(self) -> bool:
        """Return True if this binary tree is empty.

        Note that only empty binary trees can have left and right
        attributes set to None.
        """
        return self._root is None

    def value(self) -> object:
        """Return the object at <self._root>.

        """
        return self._root

    def left_btree(self) -> 'BinaryTree':
        """Return the left BinaryTree.

        """
        if not self.is_empty():
            return self._left
        raise EmptyBinaryTreeError

    def right_btree(self) -> 'BinaryTree':
        """Return the right BinaryTree.

        """
        if not self.is_empty():
            return self._right
        raise EmptyBinaryTreeError

    # TODO: fix __eq__ method
    def __eq__(self, other: Any) -> bool:
        """
        Return true iff this BinaryTree is equivalent to <other>.

        >>> t0 = BinaryTree(None, None, None)
        >>> t = BinaryTree(1, BinaryTree(2, t0, t0), BinaryTree(3, t0, t0))
        >>> t2 = BinaryTree(4, BinaryTree(5, t0, t0), BinaryTree(6, t0, t0))
        >>> t3 = BinaryTree(7, t, t2)
        >>> t4 = BinaryTree(99, t3, t)
        >>> t == t3
        False
        >>> t4 == t4
        True
        >>> t2.__eq__(t3)
        False
        """
        return (type(self) == type(other) and
                self._root == other.value() and
                self._left == other.left_btree() and
                self._right == other.right_btree())

    def __repr__(self) -> str:
        """
        Represent the binary tree <self> as a string that can be
        evaluated to produce an equivalent binary tree.

        >>> t0 = BinaryTree(None, None, None)
        >>> t = BinaryTree(1, BinaryTree(2, t0, t0), BinaryTree(3, t0, t0))
        >>> t2 = BinaryTree(4, BinaryTree(5, t0, t0), BinaryTree(6, t0, t0))
        >>> t3 = BinaryTree(7, t, t2)
        >>> t4 = BinaryTree(99, t3, t)
        >>> t
        BinaryTree(1, BinaryTree(2, BinaryTree(None, None, None), \
BinaryTree(None, None, None)), BinaryTree(3, BinaryTree(None, None, None), \
BinaryTree(None, None, None)))
        """
        return "BinaryTree({}, {}, {})".format(repr(self._root),
                                               repr(self._left),
                                               repr(self._right))

    # TODO: Try to impove __str__ (look at bst2.py)
    def __str__(self, depth: str = '') -> str:
        """
        Return a str containing all of the items in this BST, using
        indentation to show depth.

        >>> t0 = BinaryTree(None, None, None)
        >>> t = BinaryTree(1, BinaryTree(2, t0, t0), BinaryTree(3, t0, t0))
        >>> t2 = BinaryTree(4, BinaryTree(5, t0, t0), BinaryTree(6, t0, t0))
        >>> t3 = BinaryTree(7, t, t2)
        >>> t4 = BinaryTree(99, t3, t)
        >>> print(t)
           3
        1
           2
        <BLANKLINE>
        >>> print(t4)
              3
           1
              2
        99
                 6
              4
                 5
           7
                 3
              1
                 2
        <BLANKLINE>
        """
        if self.is_empty():
            return ''
        else:
            # Note: recursive call on right tree first for str method.
            right_tree = self._right.__str__(depth + '   ')
            left_tree = self._left.__str__(depth + '   ')
            return (right_tree + "{}{}\n".format(depth, str(self._root)) +
                    left_tree)

    def __contains__(self, value: object) -> bool:
        """
        Return whether tree rooted at self contains value.

        >>> t0 = BinaryTree(None, None, None)
        >>> t = BinaryTree(1, BinaryTree(2, t0, t0), BinaryTree(3, t0, t0))
        >>> t2 = BinaryTree(4, BinaryTree(5, t0, t0), BinaryTree(6, t0, t0))
        >>> t3 = BinaryTree(7, t, t2)
        >>> t4 = BinaryTree(99, t3, t)
        >>> 99 in t4
        True
        >>> 'Google' in t4
        False
        >>> t4.__contains__(None)
        False
        >>> t4.__contains__(2)
        True
        """
        if self._root is None:
            return False
        else:
            # We don't care if we're at a leaf.
            return any([self._root == value, self._left.__contains__(value),
                       self._right.__contains__(value)])

    def height(self) -> int:
        """Return the height of this binary tree <self>.

        """
        pass


#############################################################################
#                              Traversal
#############################################################################
    def preorder(self) -> list:
        """Return a list of this tree's items using a *preorder* traversal.

        >>> t0 = BinaryTree(None, None, None)
        >>> t = BinaryTree(200, BinaryTree(201, t0, t0), BinaryTree(202, t0, \
t0))
        >>> t1 = BinaryTree(19, BinaryTree(100, t0, t0), BinaryTree(101, t0, \
t0))
        >>> t3 = BinaryTree(29, t, t1)
        >>> t4 = BinaryTree(500, t3, t1)
        >>> t.preorder()
        [200, 201, 202]
        >>> t3.preorder()
        [29, 200, 201, 202, 19, 100, 101]
        >>> t4.preorder()
        [500, 29, 200, 201, 202, 19, 100, 101, 19, 100, 101]
        """
        if self.is_empty():
            return []
        else:
            return [self._root] + sum([self._left.preorder(),
                                       self._right.preorder()], [])

    def inorder(self) -> list:
        """Return a list of this tree's items using an *inorder* traversal.

        >>> t0 = BinaryTree(None, None, None)
        >>> t = BinaryTree(1, BinaryTree(2, t0, t0), BinaryTree(3, t0, t0))
        >>> t2 = BinaryTree(4, BinaryTree(5, t0, t0), BinaryTree(6, t0, t0))
        >>> t3 = BinaryTree(7, t, t2)
        >>> t.inorder()
        [2, 1, 3]
        >>> t3.inorder()
        [2, 1, 3, 7, 5, 4, 6]
        >>> t4 = BinaryTree(99, t3, t)
        >>> t4.inorder()
        [2, 1, 3, 7, 5, 4, 6, 99, 2, 1, 3]
        """
        if self._root is None:
            return []
        else:
            return sum([self._left.inorder(), [self._root],
                        self._right.inorder()], [])

    def postorder(self) -> list:
        """Return a list of this tree's items using a *postorder* traversal.

        >>> t0 = BinaryTree(None, None, None)
        >>> t = BinaryTree(1, BinaryTree(2, t0, t0), BinaryTree(3, t0, t0))
        >>> t2 = BinaryTree(4, BinaryTree(5, t0, t0), BinaryTree(6, t0, t0))
        >>> t3 = BinaryTree(7, t, t2)
        >>> t.postorder()
        [2, 3, 1]
        >>> t3.postorder()
        [2, 3, 1, 5, 6, 4, 7]
        >>> t4 = BinaryTree(99, t3, t)
        >>> t4.postorder()
        [2, 3, 1, 5, 6, 4, 7, 2, 3, 1, 99]
        """
        if self._root is None:
            return []
        else:
            return sum([self._left.postorder(), self._right.postorder(),
                        [self._root]], [])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
