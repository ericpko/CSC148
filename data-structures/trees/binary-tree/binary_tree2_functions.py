"""Binary tree functions

=== CSC148 Winter 2018 ===
Department of Computer Science,
University of Toronto
__author__ = 'Eric K'

=== Module Description ===
This module contains some functions for the binary_tree2.py implementation.
Note that some of these could be modified into methods.
"""
from binary_tree2 import BinaryTree
from typing import Union, Optional, Callable, Any


def contains(node: Union[BinaryTree, None], value: object) -> bool:
    """
    Return whether tree rooted at self contains value.

    >>> t = BinaryTree(5, BinaryTree(7), BinaryTree(9))
    >>> contains(t,5)
    True
    >>> contains(t,2)
    False
    >>> t1 = BinaryTree(5, BinaryTree(7,BinaryTree(3)), None)
    >>> contains(t1,1)
    False
    """
    if node is None or node.value is None:
        return False
    elif node.value == value:
        return True
    else:
        return any([node.left is not None and value in node.left,
                    node.right is not None and value in node.right])

    # Version 2
    # if node is None or node.value is None:
    #     return False
    # elif node.value == value:
    #     return True
    # else:
    #     return any([node.left is not None and contains(node.left, value),
    #                 node.right is not None and contains(node.right, value)])

    # Version 3
    # if node is None or node.value is None:
    #     return False
    # elif node.value == value:
    #     return True
    # else:
    #     return any([contains(node.left, value), contains(node.right, value)])


def height(node: Union[BinaryTree, None]) -> int:
    """
    Return heigh of Binary tree.

    >>> t = BinaryTree(5, BinaryTree(7), None)
    >>> height(t)
    2
    """
    if node is None or node.value is None:
        return 0
    elif node.left is None and node.right is None:
        return 1
    else:
        return 1 + max([height(node.left), height(node.left)])


def evaluate(b: BinaryTree) -> Union[float, object]:
    """
    Evaluate the expression rooted at b.  If b is a leaf,
    return its float value.  Otherwise, evaluate b.left and
    b.right and combine them with b.value.

    Assume:  -- b is a non-empty binary tree
             -- interior nodes contain value in {"+", "-", "*", "/"}
             -- interior nodes always have two children
             -- leaves contain float value

    >>> b = BinaryTree(3.0)
    >>> evaluate(b)
    3.0
    >>> b = BinaryTree("*", BinaryTree(3.0), BinaryTree(4.0))
    >>> evaluate(b)
    12.0
    """
    b.value: int
    b.left: BinaryTree

    if b is None or b.value is None:
        return 0.0
    elif b.left is None and b.right is None:
        return float(b.value)
    else:
        return eval("{} {} {}".format(evaluate(b.left),
                                      b.value,
                                      evaluate(b.right)))


def find(node: Optional['BinaryTree'], data: object) -> Optional['BinaryTree']:
    """
    Return BinaryTree containing data or else None.

    >>> find(None,15) is None
    True
    >>> bt = BinaryTree(5, BinaryTree(4),BinaryTree(3))
    >>> find(bt,7) is None
    True
    >>> find(bt,4)
    BinaryTree(4)
    >>> find(bt,3)
    BinaryTree(3)
    """
    if node is None or node.value is None:
        pass
    elif node.value == data:
        return node
    else:
        left = find(node.left, data)
        if left is not None:
            return left
        # else:
        return find(node.right, data)

        # or
        # return left if left else find(node.right, data)


def prune_btree(t: BinaryTree,
                predicate: Callable[[object], bool]) -> Optional[BinaryTree]:
    """ Return a new tree with the same values as t, except it
    prunes (omits) all paths of t that start with nodes where
    predicate(node.value) == False. If predicate(t.value) == False,
    then prune returns None.
    Assume that all values in t are ints, and that predicate
    always takes an int and returns a bool.

    >>> v: int
    >>> t1 = BinaryTree(6, BinaryTree(8), BinaryTree(9))
    >>> t3 = BinaryTree(7, BinaryTree(3), BinaryTree(12))
    >>> t = BinaryTree(5, t1, t3)
    >>> t3_pruned = BinaryTree(7, None, BinaryTree(12))
    >>> def predicate (v) : return v > 4
    >>> prune_btree(t, predicate) == BinaryTree(5, t1, t3_pruned)
    True
    """
    if t is None or t.value is None:
        pass
    elif predicate(t.value) is False:
        pass
    else:
        new_t = BinaryTree(t.value)
        new_t.left = prune_btree(t.left, predicate)
        new_t.right = prune_btree(t.right, predicate)

        return new_t

    # Version 2
    # if t is None or t.value is None:
    #     return BinaryTree(None)
    # elif not predicate(t.value):
    #     return BinaryTree(None)
    # else:
    #     new_t = BinaryTree(t.value)
    #     subs = [prune_btree(t.left, predicate),
    #             prune_btree(t.right, predicate)]
    #     new_t.left = subs[0] if subs[0].value is not None else None
    #     new_t.right = subs[1] if subs[1].value is not None else None
    #     return new_t

    # Version 3
    # if t is None or t.value is None:
    #     pass
    # elif not predicate(t.value):
    #     pass
    # else:
    #     new_t = BinaryTree(t.value)
    #     children = [prune_btree(t.left, predicate),
    #                 prune_btree(t.right, predicate)]
    #     new_t.left = children[0]
    #     new_t.right = children[1]
    #     return new_t


# TODO: fix
# def pathlength_sets_b(t: BinaryTree) -> None:
#     """
#     Replace the value of each node in Tree t by a set containing all
#     path lengths from that node to any leaf. A path's length is the
#     number of edges it contains.
#
#     >>> t = BinaryTree(5)
#     >>> pathlength_sets_b(t)
#     >>> print(t)
#     {0}
#     >>> t.left = BinaryTree(17)
#     >>> t.right = BinaryTree(13, BinaryTree(11), None)
#     >>> pathlength_sets_b(t)
#     >>> print(t)
#     {1, 2}
#        {0}
#        {1}
#           {0}
#     """
#     if t is None or t.value is None:
#         pass
#     elif t.left is None and t.right is None:
#         t.value = {0}
#     else:
#         t.value = set()
#         pathlength_sets_b(t.left) if t.left is not None else None
#         pathlength_sets_b(t.right) if t.right is not None else None
#         t.value.union(t.left.value)
#         t.value.union(t.right.value)
#         t.value = set([e + 1 for e in t.value])


def path_to_max(bt: BinaryTree) -> list:
    """
    Return a list of the values in a path from the root of a bt
    to a leaf with the max value.

    >>> b1 = BinaryTree(7)
    >>> b2 = BinaryTree(3, BinaryTree(2), None)
    >>> b3 = BinaryTree(5, b2, b1)
    >>> path_to_max(b3)
    [5, 7]
    """
    bt.left: BinaryTree

    if bt is None or bt.value is None:
        return []
    elif bt.left is None and bt.right is None:
        return [bt.value]
    else:
        left = [bt.value] + path_to_max(bt.left)
        right = [bt.value] + path_to_max(bt.right)
        if left[-1] > right[-1]:
            return left
        return right

    # Sol 2
    # if not bt:
    #     pass
    # elif not bt.left and not bt.right:
    #     return [bt.value]
    # else:
    #     left = path_to_max(bt.left)
    #     right = path_to_max(bt.right)
    #     if left and right:
    #         return [bt.value] + left \
    #             if left[-1] > right[-1] \
    #             else [bt.value] + right
    #     elif left:
    #         return [bt.value] + left
    #     else:
    #         return [bt.value] + right


if __name__ == '__main__':
    import doctest
    doctest.testmod()
