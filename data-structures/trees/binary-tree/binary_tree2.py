"""Binary tree

=== CSC148 Winter 2018 ===
University of Toronto,
Department of Computer Science
__author__ = 'Eric K'

=== Module Description ===
This module contains a binary tree implementation
"""
from typing import Union, Optional


class BinaryTree:
    """
    A Binary Tree, i.e. arity 2.
    """
    value: object
    left: Optional['BinaryTree']
    right: Optional['BinaryTree']

    def __init__(self, value: object, left: Optional['BinaryTree'] = None,
                 right: Optional['BinaryTree'] = None) -> None:
        """
        Create BinaryTree self with value and children left and right.

        """
        self.value, self.left, self.right = value, left, right

    def __eq__(self, other: Union['BinaryTree', object]) -> bool:
        """
        Return whether BinaryTree self is equivalent to other.

        >>> BinaryTree(7).__eq__("seven")
        False
        >>> b1 = BinaryTree(7, BinaryTree(5))
        >>> b1.__eq__(BinaryTree(7, BinaryTree(5), None))
        True
        >>> b1.__eq__(BinaryTree(7, BinaryTree(5,BinaryTree(2)), None))
        False
        """
        return (type(self) is type(other) and
                self.value == other.value and
                self.left == other.left and
                self.right == other.right)

    def __repr__(self) -> str:
        """
        Represent BinaryTree (self) as a string that can be evaluated to
        produce an equivalent BinaryTree.

        >>> BinaryTree(1, BinaryTree(2), BinaryTree(3))
        BinaryTree(1, BinaryTree(2), BinaryTree(3))
        """
        if self.value is None:
            return ''
        elif self.left is None and self.right is None:
            return f'BinaryTree({self.value})'
        else:
            return "BinaryTree({}, {}, {})".format(repr(self.value),
                                                   repr(self.left),
                                                   repr(self.right))

    def __str__(self, level: str = '') -> str:
        """
        Return a user-friendly string representing BinaryTree (self)
        inorder. Indent by indent.

        >>> b = BinaryTree(1, BinaryTree(2, BinaryTree(3)), BinaryTree(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        if self.value is None:
            return ''
        else:
            right = self.right.__str__(level + '    ') if self.right else ''
            left = self.left.__str__(level + '    ') if self.left else ''
            s = right + "{}{}\n".format(level, str(self.value)) + left
            return s

    def __contains__(self, value: object) -> bool:
        """
        Return whether tree rooted at self contains value.

        >>> t = BinaryTree(5, BinaryTree(7), BinaryTree(9))
        >>> 7 in t
        True
        >>> t = BinaryTree(5, BinaryTree(7), None)
        >>> 3 in t
        False
        """
        # Can also use: self.left.__contains__(value) rather than in
        # Version 1
        if self.value is None:
            return False
        elif value == self.value:
            return True
        else:
            return any([self.left is not None and value in self.left,
                        self.right is not None and value in self.right])

        # Version 2
        # if self.value is None:
        #     return False
        # else:
        #     return any([self.value == value,
        #                 self.left is not None and value in self.left,
        #                 self.right is not None and value in self.right])

        # Version 3
        # if self.value is None:
        #     return False
        # elif value == self.value:
        #     return True
        # else:
        #     return any([value in self.left if self.left else False,
        #                 value in self.right if self.right else False])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
