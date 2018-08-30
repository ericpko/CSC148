"""BST functions

=== CSC148 Winter 2018 ===
Department of Computer Science,
University of Toronto
__author__ = 'Eric K'

=== Module Description ===
This module contains some functions for the bst2.py implementation. Note that
some of these could be modified into methods.
"""
from bst2 import *
from typing import Optional, Union, Tuple


def evaluate_v3(b: BTNode) -> float:
    """
    Evaluate the expression rooted at b.  If b is a leaf,
    return its float data.  Otherwise, evaluate b.left and
    b.right and combine them with b.data.

    Assume:  -- b is a binary tree
             -- interior nodes contain data in {'+', '-', '*', '/'}
             -- interior nodes always have two children
             -- leaves contain float data

    >>> b = BTNode(3.0)
    >>> evaluate_v3(b)
    3.0
    >>> b = BTNode('*', BTNode(3.0), BTNode(4.0))
    >>> evaluate_v3(b)
    12.0
    """
    b.data: int
    b.left: BTNode
    if b is None or b.data is None:
        return 0.0
    elif b.left is None and b.right is None:
        return float(b.data)
    else:
        return eval("{} {} {}".format(evaluate_v3(b.left),
                                      b.data,
                                      evaluate_v3(b.right)))


def parenthesize(b: BTNode) -> Union[str, float]:
    """
    Parenthesize the expression rooted at b, so that float data is
    not parenthesized, but each pair of expressions
    joined by an operator are parenthesized.

    Assume:  -- b is a binary tree
             -- interior nodes contain data in {'+', '-', '*', '/'}
             -- interior nodes always have two children
             -- leaves contain float data

    >>> b = BTNode(3.0)
    >>> print(parenthesize(b))
    3.0
    >>> b = BTNode('+', BTNode('*', BTNode(3.0), BTNode(4.0)), BTNode(7.0))
    >>> print(parenthesize(b))
    ((3.0 * 4.0) + 7.0)
    """
    b.data: int
    b.left: BTNode
    if b is None or b.data is None:
        return ''
    elif b.left is None and b.right is None:
        return float(b.data)
    else:
        return "({} {} {})".format(parenthesize(b.left),
                                   b.data,
                                   parenthesize(b.right))


def is_leaf(node: BTNode) -> bool:
    """
    Return whether node is a leaf.

    >>> b = BTNode(1, BTNode(2))
    >>> is_leaf(b)
    False
    >>> is_leaf(b.left)
    True
    """
    return node.left is None and node.right is None


def find_max(node: BTNode) -> BTNode:
    """
    Find and return node with maximum data, assume node is not None.

    Assumption: node is the root of a binary search tree.

    >>> find_max(BTNode(5, BTNode(3), BTNode(7)))
    BTNode(7)
    """
    if node is None or node.data is None:
        pass
    elif node.right is None:
        return node
    else:
        return find_max(node.right)

    # if node is None or node.data is None:
    #     pass
    #
    # return find_max(node.right) if node.right is not None else node


def list_longest_path(node: Union[BTNode, None]) -> list:
    """ List the data in a longest path of node.

    >>> list_longest_path(None)
    []
    >>> list_longest_path(BTNode(5))
    [5]
    >>> b1 = BTNode(7)
    >>> b2 = BTNode(3, BTNode(2), None)
    >>> b3 = BTNode(5, b2, b1)
    >>> list_longest_path(b3)
    [5, 3, 2]
    """
    # if node is None or node.data is None:
    #     return []
    # else:
    #     left = [node.data] + sum([list_longest_path(node.left)], [])
    #     right = [node.data] + sum([list_longest_path(node.right)], [])
    #     return left if len(left) > len(right) else right

    if node is None or node.data is None:
        return []
    else:
        left = [node.data] + list_longest_path(node.left)
        right = [node.data] + list_longest_path(node.right)
        if len(left) > len(right):
            return left
        return right

    # if node is None or node.data is None:
    #     return []
    # elif node.left is None and node.right is None:
    #     return [node.data]
    # elif node.right is None:
    #     return [node.data] + sum([list_longest_path(node.left)], [])
    # elif node.left is None:
    #     return [node.data] + sum([list_longest_path(node.right)], [])
    # else:
    #     left = [node.data] + sum([list_longest_path(node.left)], [])
    #     right = [node.data] + sum([list_longest_path(node.right)], [])
    #     return left if len(left) > len(right) else right


def height(node: Optional['BTNode']) -> int:
    """
    Return the height of this tree, <node>.
    """
    if node is None or node.data is None:
        return 0
    elif node.left is None and node.right is None:
        return 1
    else:
        return 1 + max([height(node.left), height(node.right)])


def list_between(node: Union[BTNode, None], start: object, end: object) -> list:
    """
    Return a Python list of all data in the binary search tree
    rooted at node that are between start and end (inclusive).

    A binary search tree t is a BTNode where all nodes in the subtree
    rooted at t.left are less than t.data, and all nodes in the subtree
    rooted at t.right are more than t.data

    Avoid visiting nodes with values less than start or greater than end.

    >>> b_left = BTNode(4, BTNode(2), BTNode(6))
    >>> b_right = BTNode(12, BTNode(10), BTNode(14))
    >>> b = BTNode(8, b_left, b_right)
    >>> list_between(None, 3, 13)
    []
    >>> list_between(b, 2, 3)
    [2]
    >>> L = list_between(b, 3, 11)
    >>> L.sort()
    >>> L
    [4, 6, 8, 10]
    """
    if node is None or node.data is None:
        return []
    elif node.data < start:
        return sum([list_between(node.right, start, end)], [])
    elif node.data > end:
        return sum([list_between(node.left, start, end)], [])
    else:
        return [node.data] + sum([list_between(node.left, start, end),
                                  list_between(node.right, start, end)], [])

    # Version 2
    # if node is None or node.data is None:
    #     return []
    # elif node.data < start:
    #     return list_between(node.right, start, end)
    # elif node.data > end:
    #     return list_between(node.left, start, end)
    # else:
    #     return [node.data] + sum([list_between(node.left, start, end),
    #                               list_between(node.right, start, end)], [])

    # No listcomp
    # if node is None or node.data is None:
    #     return []
    # elif start > node.data:
    #     return list_between(node.right, start, end)
    # elif end < node.data:
    #     return list_between(node.left, start, end)
    # else:
    #     return [node.data] + list_between(node.left, start, end) + \
    #            list_between(node.right, start, end)


def concatenate_leaves(t: Union[BTNode, None]) -> str:
    """
    Return the string values in the Tree rooted at t concatenated from left to
    right. Assume all leaves have string value.

    >>> t1 = BTNode("one")
    >>> t2 = BTNode("two")
    >>> t3 = BTNode("three", t1, t2)
    >>> concatenate_leaves(t1)
    'one'
    >>> concatenate_leaves(t3)
    'onetwo'
    """
    if t is None or t.data is None:
        return ''
    elif t.left is None and t.right is None:
        return str(t.data)
    else:
        return ''.join([concatenate_leaves(t.left),
                        concatenate_leaves(t.right)])

    # Version 2
    # if t is None or t.data is None:
    #     return ''
    # elif t.left is None and t.right is None:
    #     return str(t.data)
    # else:
    #     s = ''
    #     s += concatenate_leaves(t.left)
    #     s += concatenate_leaves(t.right)
    #     return s

    # Version 3
    # if t is None or t.data is None:
    #     return ''
    # elif t.left is None and t.right is None:
    #     return str(t.data)
    # else:
    #     s = "{}{}".format(concatenate_leaves(t.left),
    #                       concatenate_leaves(t.right))
    #     return s


def count_leaves(t: Union[BTNode, None]) -> int:
    """
    Return the number of leaves in BTNode t.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> count_leaves(None)
    0
    >>> count_leaves(t3)
    2
    """
    if t is None or t.data is None:
        return 0
    elif t.left is None and t.right is None:
        return 1
    else:
        return sum([count_leaves(t.left), count_leaves(t.right)])


def sum_leaves(t: Union[BTNode, None]) -> int:
    """
    Return the sum of the values in the leaves of BTNode t.  Return
    0 if t is empty.
    Assume all leaves have integer value.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> sum_leaves(t2)
    2
    >>> sum_leaves(t3)
    3
    """
    if t is None or t.data is None:
        return 0
    elif t.left is None and t.right is None:
        return t.data if isinstance(t.data, int) else 0
    else:
        return sum([sum_leaves(t.left), sum_leaves(t.right)])


def sum_internal(t: Union[BTNode, None]) -> int:
    """
    Return the sum of the values in the internal nodes of BTNode t.  Return
    0 if t is empty.
    Assume all internal nodes have integer value.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> sum_internal(t2)
    0
    >>> sum_internal(t3)
    3
    """
    t.data: int
    if t is None or t.data is None:
        return 0
    elif t.left is None and t.right is None:
        return 0
    else:
        return t.data + sum([sum_internal(t.left), sum_internal(t.right)])


def bst_contains(node: Union[BTNode, None], value: object) -> bool:
    """
    Return whether tree rooted at node contains value.

    Assume node is the root of a Binary Search Tree

    >>> bst_contains(None, 5)
    False
    >>> bst_contains(BTNode(7, BTNode(5), BTNode(9)), 5)
    True
    """
    if node is None or node.data is None:
        return False
    elif value == node.data:
        return True
    elif value < node.data:
        return bst_contains(node.left, value)
    else:
        return bst_contains(node.right, value)

    # Don't actually need any() since not iterating
    # Version 2
    # if node is None or node.data is None:
    #     return False
    # elif value == node.data:
    #     return True
    # elif value < node.data:
    #     return any([bst_contains(node.left, value)])
    # else:
    #     return any([bst_contains(node.right, value)])

    # Their solution
    # if node is None:
    #     return False
    # elif node.value > value:
    #     return bst_contains(node.left, value)
    # elif node.value < value:
    #     return bst_contains(node.right, value)
    # else:
    #     return True


def bst_distance(node: BTNode, val: object) -> int:
    """
    Find distance of a node with the value from the root

    @param BTNode node: The binary tree
    @param object val: Value to find in the node
    @rtype: int

    >>> tree = BTNode(4)
    >>> bst_distance(tree, 4)
    0
    >>> tree = BTNode(4, BTNode(3, BTNode(1)), BTNode(5))
    >>> bst_distance(tree, 1)
    2
    """
    if node is None or node.data is None:
        return 0
    elif node.data == val:
        return 0
    elif val < node.data:
        return 1 + bst_distance(node.left, val)

    # else:
    return 1 + bst_distance(node.right, val)

    # Version 2
    # if node is None or node.data is None:
    #     return 0
    # elif node.data == val:
    #     return 0
    # elif val < node.data:
    #     return 1 + sum([bst_distance(node.left, val)])
    # else:
    #     return 1 + sum([bst_distance(node.right, val)])

    # Their solution
    # if node.data == val:
    #     return 0
    # else:
    #     if val > node.data:
    #         return 1 + bst_distance(node.right, val)
    #     else:
    #         return 1 + bst_distance(node.left, val)


# TODO: fix
# def is_bst(node: Union[BTNode, None]) -> bool:
#     """
#     Checks whether the Binary Tree rooted at node is a BST
#     @param BTNode|None node: The binary tree
#     @return: bool
#
#     >>> is_bst(None)
#     True
#     >>> tree = BTNode(4, BTNode(3, BTNode(1)), BTNode(5))
#     >>> is_bst(tree)
#     True
#     >>> tree = BTNode(3, BTNode(2, BTNode(1), BTNode(4)), BTNode(5))
#     >>> is_bst(tree)
#     False
#     """
#     def find_max(node):
#         if node is None:
#             return float('-inf')
#         return max([node.value, find_max(node.right), find_max(node.left)])
#
#     def find_min(node):
#         if node is None:
#             return float('inf')
#         return min([node.value, find_min(node.right), find_min(node.left)])
#
#     if node is None:
#         return True
#     else:
#         left_result = True
#         right_result = True
#         if node.left is not None:
#             left_result =  find_max(node.left) < node.value
#         if node.right is not None:
#             right_result = find_min(node.right) > node.value
#         return all([left_result, right_result,
#                     is_bst(node.left), is_bst(node.right)])


def tree_add(node: Union[BTNode, None], num: float) -> Union[BTNode, None]:
    """
    Adds num to each node of the Binary Tree and return a modified Tree

    >>> tree_add(None, 5) is None
    True
    >>> tree_add(BTNode(2, BTNode(1), BTNode(3)), 2)
    BTNode(4, BTNode(3), BTNode(5))
    """
    node.data: int
    if node is None or node.data is None:
        pass
    else:
        node.data += num
        node.left = tree_add(node.left, num)
        node.right = tree_add(node.right, num)
        return node

    # Sol 2:
    # if node is None or node.data is None:
    #     pass
    # else:
    #     new_node = BTNode(node.data + num,
    #                       tree_add(node.left, num), tree_add(node.right, num))
    #     return new_node

    # Their version
    # if node is None:
    #     pass
    # else:
    #     return BTNode(node.data + num,
    #                   tree_add(node.left, num),
    #                   tree_add(node.right, num))


def insert(node: Union[BTNode, None], value: object) -> BTNode:
    """
    Insert value in BST rooted at node if necessary, and return new root.

    Assume node is the root of a Binary Search Tree.

    >>> b = BTNode(5)
    >>> b1 = insert(b, 3)
    >>> print(b1)
    5
        3
    <BLANKLINE>
    """
    if node is None or node.data is None:
        return BTNode(value)
    elif value < node.data:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

    # Version 2
    # if node is None:
    #    return  BinaryTree(value)
    # else:
    #     if value > node.data:
    #         node.right = insert(node.right, value)
    #     elif value < node.data:
    #         node. left = insert(node.left, value)
    #     return node


def find_min(node: BTNode) ->BTNode:
    """
    Find and return subnode with min data.

    Assume node is the root of a binary search tree.

    >>> find_min(BTNode(5, BTNode(3), BTNode(7)))
    BTNode(3)
    """
    if node is None or node.data is None:
        pass
    elif node.left is None:
        return node
    else:
        return find_min(node.left)


def find_max_v2(node: BTNode) ->BTNode:
    """
    Find and return subnode with maximum data.

    Assume node is the root of a binary search tree.

    >>> find_max(BTNode(5, BTNode(3), BTNode(7)))
    BTNode(7)
    """
    if node is None or node.data is None:
        pass
    elif node.right is None:
        return node
    else:
        return find_max(node.right)

    # another solution
    # return find_max(node.right) if node.right is not None else node


def delete(node: Union[BTNode, None], value: object) \
        -> Union[BTNode, None]:
    """
    Delete data from binary search tree rooted at node, if it exists,
    and return root of resulting tree.

    >>> b = BTNode(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> print(b)
            14
        12
            10
    8
            6
        4
            2
    <BLANKLINE>
    >>> b = delete(b, 12)
    >>> print(b)
        14
            10
    8
            6
        4
            2
    <BLANKLINE>
    >>> b = delete(b, 14)
    >>> print(b)
        10
    8
            6
        4
            2
    <BLANKLINE>
    """
    # Algorithm for delete:
    # 1. If this node is None, return that
    if node is None:
        pass

    # 2. If data is less than node.data, delete it from left child and
    #     return this node
    elif value < node.data:
        node.left = delete(node.left, value)
        return node

    # 3. If data is more than node.data, delete it from right child
    #    and return this node
    elif value > node.data:
        node.right = delete(node.right, value)
        return node
    else:
        # 4. If node with data has fewer than two children,
        #    and you know one is None, return the other one
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        # 5. If node with data has two non-None children,
        #    replace data with that of its smallest child in the right subtree,
        #    and delete that child, and return this node
        #    This captures the case when both children are None as well.
        else:
            min_node = find_min(node.right)
            node.data = min_node.data
            node.right = delete(node.right, node.data)
            return node

    # VERSION 2
    # # 1. If this node is None, return that
    # if node is None:
    #     pass
    # # 2. If value is more than node.value, delete it from right child and
    # #     return this node
    # elif value > node.data:
    #     node.right = delete(node.right, value)
    # # 3. If value is less than node.value, delete it from left child
    # #     and return this node
    # elif value < node.data:
    #     node.left = delete(node.left, value)
    # # 4. If node with value has fewer than two children,
    # #     and you know one is None, return the other one
    # elif node.left is None:
    #     node = node.right
    # elif node.right is None:
    #     node = node.left
    # # 5. If node with value has two non-None children,
    # #     replace value with that of its largest child in the left subtree,
    # #     and delete that child, and return this node
    # else:
    #     node.data = find_max(node.left).data
    #     node.left = delete(node.left, node.data)
    #     # we could select the min in right branch
    #     # node.value = find_min(node.right).data
    #     # node.right = delete(node.right, node.data)
    # return node


# challenging! draw a picture to help
def find_left_streak(t: BTNode) -> BTNode:
    """ Return the parent node of the shallowest left streak in t,
    or None if there is no left streak.
    Qparam BSTree t : the root of the whole tree
    ©rtype: BSTreeI None

    >>> left = BTNode(4, (BTNode(3, BTNode(2, BTNode(1, BTNode(0))))))
    >>> t = BTNode(5, left, BTNode(6))
    >>> find_left_streak(t).data
    5
    >>> t.left.right = BTNode(4.5)
    >>> find_left_streak(t).data
    4
    """
    streak_parent = t
    while streak_parent.left is not None:
        node = streak_parent.left
        if (node.left is not None and node.right is None) and \
                (node.left.left is not None and node.left.right is None):
            return streak_parent
        streak_parent = node
    # if the end of the loop is reached, there is no left streak - return None


# Challenging! draw picture
def fix_left_streaks(t: BTNode) -> None:
    """
    >>> left = BTNode(4, (BTNode(3, BTNode(2, BTNode(1, BTNode(0))))))
    >>> t = BTNode(5, left, BTNode(6))
    >>> # height is 6
    >>> t.left.right is None
    True
    >>> t.left.left.right is None
    True
    >>> fix_left_streaks(t)
    >>> # t.height is 4
    >>> t.left.right.data == 4
    True
    >>> t.left.left.right.data == 2
    True
    """
    strk = find_left_streak(t)

    while strk is not None:
        t1, t2, = strk.left.left, strk.left
        strk.left, t1.right, t2.left, t2.right = t1, t2, None, None
        strk = find_left_streak(t)

    # Recursive sol:
    # curr = find_left_streak(t)
    # if curr and curr.left.left:
    #     curr.left.left.right = t.left
    #     t.left = t.left.left
    #     t.left.right.left = None
    #     fix_left_streak(curr.left)


# Very challenging!!
def tpbt(root: Optional[BTNode]) -> Tuple[int, bool]:
    """
    Return a tuple containing (1) the height of the tallest
    perfect binary tree within the tree rooted at root. And
    (2), whether or not that tallest perfect binary tree occurs
    at the root itself.

    """
    # if root is None or root.data is None:
    #     return (0, True)
    # elif root.left is None and root.right is None:
    #     return (1, True)
    # else:
    #     left, right = tpbt(root.left), tpbt(root.right)
    #
    #     # Check if both sides are the same tuple AND that they are True
    #     if left == right and left[1] is True:
    #         return (tpbt(root.left)[0] + 1, True)
    #     else:
    #         return (max(tpbt(root.left)[0] + 1,
    #                     tpbt(root.right)[0] + 1), False)

    # Clean version:
    if root is None or root.data is None:
        return (0, True)
    elif root.left is None and root.right is None:
        return (1, True)
    else:
        left, right = tpbt(root.left), tpbt(root.right)
        if left == right and left[1] is True:  # Both perfect binary trees.
            return (left[0] + 1, True)
        else:
            return (max(left[0] + 1, right[0] + 1), False)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
