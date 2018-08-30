"""Binary search tree

=== CSC148 Winter 2018 ===
University of Toronto,
Department of Computer Science
__author__ = 'Eric K'

=== Module Description ===
This module contains a binary search tree implementation.
"""
from typing import Optional, Any


class BTNode:
    """
    Binary Tree node.
    This is basically a Binary Tree
    """

    def __init__(self, data: object, left: Optional['BTNode'] = None,
                 right: Optional['BTNode'] = None) -> None:
        """
        Create BTNode (self) with data and children left and right.
        """
        self.data, self.left, self.right = data, left, right

    def __eq__(self, other: Any) -> bool:
        """
        Return whether BTNode (self) is equivalent to other.

        >>> BTNode(7).__eq__('seven')
        False
        >>> b1 = BTNode(7, BTNode(5))
        >>> b1.__eq__(BTNode(7, BTNode(5), None))
        True
        """
        return (type(self) is type(other) and
                self.data == other.data and
                self.left == other.left and
                self.right == other.right)

    def __repr__(self) -> str:
        """ (BTNode) -> str

        Represent BTNode (self) as a string that can be evaluated to
        produce an equivalent BTNode.

        >>> BTNode(1, BTNode(2), BTNode(3))
        BTNode(1, BTNode(2), BTNode(3))
        """
        if self.data is None:
            return ''
        elif self.left is None and self.right is None:
            return f'BTNode({self.data})'
        else:
            return "BTNode({}, {}, {})".format(repr(self.data),
                                               repr(self.left),
                                               repr(self.right))

    def __str__(self, indent: str = '') -> str:
        """
        Return a user-friendly string representing BTNode (self) inorder.
        Indent by indent.

        >>> b = BTNode(1, BTNode(2, BTNode(3)), BTNode(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        if self.data is None:
            return ''

        right = self.right.__str__(indent + '    ') if self.right else ''
        left = self.left.__str__(indent + '    ') if self.left else ''
        s = right + '{}{}\n'.format(indent, self.data) + left
        return s

    def __contains__(self, data: Optional[object]) -> bool:
        """

        Return whether tree rooted at node contains value.

        >>> t = BTNode(5, BTNode(7), BTNode(9))
        >>> t.__contains__(7)
        True
        >>> 9 in t
        True
        >>> 11 in t
        False
        """
        if self.data is None:
            return False
        elif self.data == data:
            return True
        else:
            return any([self.left is not None and data in self.left,
                        self.right is not None and data in self.right])


class BST:
    """
    Manages a binary search tree, even when the root is None or changes.

    root - root of binary search tree

    Assumptions:
        -- all data in root.left is less than root.data
        -- all data in root.right is more than root.data
        -- None indicates an empty tree
    """
    root: BTNode

    def __init__(self, root: BTNode = None) -> None:
        """
        Create BST with BTNode root.
        """
        self.root = root

    def __repr__(self):
        """ (BST) -> str

        Represent BST (self) as a string that can be evaluated
        to an equivalent BST.

        >>> b = BST(BTNode(5))
        >>> b
        BST(BTNode(5))
        """
        return "BST({})".format(BTNode.__repr__(self.root))

    def __str__(self):
        """ (BST) -> str

        Return a user-friendly string representation of BST (self).

        >>> b = BST(BTNode(5, BTNode(4), BTNode(6)))
        >>> print(b)
            6
        5
            4
        <BLANKLINE>
        """
        return BTNode.__str__(self.root)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
