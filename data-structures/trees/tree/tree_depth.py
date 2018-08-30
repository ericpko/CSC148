"""Tree depth

=== CSC148 Winter 2018 ===
Department of Computer Science,
University of Toronto
__author__ = 'Eric K'

=== Module Description ===
This module contains methods of accessing different levels of tree depth
for different types of tree data structures.
"""
from tree2 import Tree
from binary_tree2 import BinaryTree
from bst2 import *
from tree2_functions import descendants_from_list
from typing import Optional, Union


#           *********************************
#                 ===> Tree depth <===
#           *********************************
def list_below(t: Tree, n: int) -> list:
    """
    Return list of values in t from nodes with paths no longer
    than n from root.

    >>> t = Tree(0)
    >>> list_below(t, 0)
    [0]
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_below(t, 1)
    >>> L.sort()
    >>> L
    [0, 1, 2, 3]
    """
    if t.value is None:
        return []
    elif n >= 0:
        return [t.value] + sum([list_below(s, n - 1) for s in t.children], [])
    else:
        return sum([list_below(s, n - 1) for s in t.children], [])


def count_odd_above(t: Tree, n: int) -> int:
    """
    Return the number of nodes with depth less than n that have odd values.
    Assume t's nodes have integer values.

    >>> t1 = Tree(4)
    >>> t2 = Tree(3)
    >>> t3 = Tree(5, [t1, t2])
    >>> count_odd_above(t3, 1)
    1
    """
    t.value: int

    # if t.value is None:
    #     return 0
    # elif n > 0:
    #     odds = 0
    #     if t.value % 2 == 1:
    #         odds += 1
    #     return odds + sum(count_odd_above(s, n - 1) for s in t.children)
    # else:
    #     return 0

    # Version A
    # if t.value is None:
    #     return 0
    # elif n <= 0:
    #     return 0
    # else:
    #     odds = 0
    #     if t.value % 2 == 1:
    #         odds += 1
    #     return odds + sum(count_odd_above(s, n - 1) for s in t.children)

    # Version 2
    if t.value is None:
        return 0
    elif n <= 0:
        return 0
    else:
        return 1 if t.value % 2 == 1 else 0 + sum(count_odd_above(s, n - 1)
                                                  for s in t.children)

    # Version 3
    # if t is None or t.value is None:
    #     return 0
    # elif n <= 0:
    #     return 0
    # else:
    #     odds = 0
    #     if t.value % 2 != 0:
    #         odds += 1
    #     for s in t.children:
    #         odds += count_odd_above(s, n - 1)
    #     return odds


def count_at_depth(t: Tree, d: int) -> int:
    """ Return the number of nodes at depth d of t.

    >>> t = Tree(17, [Tree(0), Tree(1, [Tree(4)]), Tree(2, [Tree(5)]), Tree(3)])
    >>> count_at_depth(t, 0)
    1
    >>> count_at_depth(t, 1)
    4
    >>> count_at_depth(t, 2)
    2
    >>> count_at_depth(t, 5)
    0
    """
    if t.value is None:
        return 0
    elif d == 0:
        return 1
    else:
        return sum(count_at_depth(s, d - 1) for s in t.children)

    # Version 2
    # if t.value is None:
    #     return 0
    # elif d == 0:
    #     return 1
    # else:
    #     total = 0
    #     for s in t.children:
    #         s += count_at_depth(s, d - 1)
    #     return total

    # Version 3
    # if t.value is None:
    #     return 0
    # elif d < 0:
    #     return 0
    # elif d == 0:
    #     return 1
    # else:
    #     return sum(count_at_depth(s, d - 1) for s in t.children)


def sum_at_depth(t: Tree, d: int) -> int:
    """ Return the sum of the number of nodes at depth d of t.

    >>> t = Tree(17, [Tree(0), Tree(1, [Tree(4)]), Tree(2, [Tree(5)]), Tree(3)])
    >>> sum_at_depth(t, 0)
    17
    >>> sum_at_depth(t, 1)
    6
    >>> sum_at_depth(t, 2)
    9
    >>> sum_at_depth(t, 5)
    0
    """
    if t.value is None:
        return 0
    elif d == 0:
        return t.value if isinstance(t.value, int) else 0
    else:
        return sum(sum_at_depth(s, d - 1) for s in t.children)

    # Version 2
    # if t.value is None:
    #     return 0
    # elif d < 0:
    #     return 0
    # elif d == 0:
    #     return t.value
    # else:
    #     return sum(count_at_depth(s, d - 1) for s in t.children)


def concatenate_at_depth(t: Tree, d: int) -> str:
    """ Return the concatenation of node values at depth d of t.
    Assume that node values are strings and that there are no
    None values in any list of children in t or its descendants.

    >>> t = Tree("a", [Tree("b"), Tree("c", [Tree("d")]), \
Tree("e", [Tree("f")]), Tree("g")])
    >>> concatenate_at_depth(t, 0)
    'a'
    >>> concatenate_at_depth(t, 1)
    'bceg'
    >>> concatenate_at_depth(t, 2)
    'df'
    >>> concatenate_at_depth(t, 5)
    ''
    """
    if t.value is None:
        return ''
    elif d == 0:
        return str(t.value)
    else:
        return ''.join([concatenate_at_depth(s, d - 1) for s in t.children])


#           **************************************
#                 ===> BinaryTree depth <===
#           **************************************
def swap_even(t: Optional[BinaryTree], depth: int=0) -> None:
    """
    Swap left and right children of nodes at even depth.
    Recall that the root has depth 0, its children have depth 1,
    grandchildren have depth 2, and so on.

    >>> b1 = BinaryTree(1, BinaryTree(2, BinaryTree(3)))
    >>> b4 = BinaryTree(4, BinaryTree(5), b1)
    >>> print (b4)
        1
            2
                3
    4
        5
    <BLANKLINE>
    >>> swap_even(b4)
    >>> print (b4)
        5
    4
        1
            2
                3
    <BLANKLINE>
    """
    # depth + or - 1
    if t is None or t.value is None:
        pass
    elif depth % 2 == 0:
        t.left, t.right = t.right, t.left
    else:
        swap_even(t.left, depth + 1)
        swap_even(t.right, depth + 1)


def occurs(root: BinaryTree, s: str) -> bool:
    """
    Return true iff s is a substring of some sequence of
    values from the root to a leaf.

    >>> left = BinaryTree('b', None, BinaryTree('d', BinaryTree('e'), None))
    >>> right = BinaryTree('c', BinaryTree('e'), BinaryTree('f', \
BinaryTree('h'), BinaryTree('i')))
    >>> whole = BinaryTree('a', left, right)
    >>> occurs(whole, 'acfh')
    True
    >>> occurs(whole, 'ace')
    True
    >>> occurs(whole, 'bde')
    False
    """
    level = 0
    for ch in s:
        if ch not in str_vals(root, level):
            return False
        level += 1
    return True

    # path = ''
    # level = 0
    # for ch in s:
    #     if ch in str_vals(root, level):
    #         path += ch
    #     level += 1
    # return path == s


def str_vals(root: BinaryTree, d: int=0) -> str:
    """
    A helper function for occurs.

    >>> left = BinaryTree('b', None, BinaryTree('d', BinaryTree('e'), None))
    >>> right = BinaryTree('c', BinaryTree('e'), BinaryTree('f', \
BinaryTree('h'), BinaryTree('i')))
    >>> whole = BinaryTree('a', left, right)
    >>> str_vals(whole, 2)
    'def'
    """
    if root is None or root.value is None:
        return ''
    elif d == 0:
        return str(root.value)
    else:
        return str_vals(root.left, d - 1) + str_vals(root.right, d - 1)
    # could also use ''.join([recursive, recursive])


def level_nums(bt: BinaryTree) -> list:
    """
    Return a list of the number of items at each level of <bt>
    start at level 0.

    >>> bt = BinaryTree(4, BinaryTree(5), BinaryTree(6, BinaryTree(7)))
    >>> level_nums(bt)
    [1, 2, 1]
    """
    if bt is None:
        return [0]

    level = 0
    per_level = []
    num_items = items_at_level(bt, level)
    per_level.append(num_items) if num_items != 0 else None
    while num_items > 0:
        level += 1
        num_items = items_at_level(bt, level)
        per_level.append(num_items) if num_items != 0 else None

    return per_level

    # level = 0
    # num_items = []
    # items = items_at_level(bt, level)
    # if items != 0:
    #     num_items.append(items)
    # while items != 0:
    #     level += 1
    #     items = items_at_level(bt, level)
    #     if items != 0:
    #         num_items.append(items)
    #
    # return num_items


def items_at_level(bt: BinaryTree, level: int) -> int:
    """
    Return the number of items at <level>.

    """
    if bt is None or bt.value is None:
        return 0
    elif level == 0:
        return 1
    else:
        return sum([items_at_level(bt.left, level - 1),
                    items_at_level(bt.right, level - 1)])


# Dec 2016 exam question
def levels(bt: BinaryTree) -> list:
    """
    Question from one of the exams
    I have no idea what this does... sorry!
    """
    if bt is None or bt.value is None:
        return []
    else:
        left = levels(bt.left)
        right = levels(bt.right)

        new_list = [(1, [bt.value])]
        for item in left:
            level = item[0] + 1
            lst = item[1]
            new_list.append((level, lst))

        for item in right:
            level = item[0] + 1
            lst = item[1]
            # In this case, you'll have to add it to the
            # existing entry in new_list.
            added_to_new_list = False
            for entry in new_list:
                if entry[0] == level:
                    entry[1] += lst
                    added_to_new_list = True
            if not added_to_new_list:
                new_list.append((level, lst))

        return new_list


#           **************************************
#                    ===> BST depth <===
#           **************************************
def count_shallower(t: Union[BTNode, None], n: int) -> int:
    """ Return the number of nodes in tree rooted at t with
    depth less than n.

    >>> t = BTNode(0, BTNode(1, BTNode(2)), BTNode(3))
    >>> count_shallower(t, 2)
    3
    """
    if t is None or t.data is None:
        return 0
    elif n <= 0:
        return 0
    else:
        return 1 + sum([count_shallower(t.left, n - 1),
                        count_shallower(t.right, n - 1)])

    # Version 2
    # if t is None or t.data is None:
    #     return 0
    # elif n > 0:
    #     return 1 + sum([count_shallower(t.left, n - 1),
    #                     count_shallower(t.right, n - 1)])
    # else:
    #     return 0

    # Sol 3:
    # if t is None or t.data is None:
    #     return 0
    # elif n <= 0:
    #     return 0
    # else:
    #     return 1 + count_shallower(t.left, n - 1) + \
    #            count_shallower(t.right, n - 1)


# Heap 2018 Midterm 2
def btnode_distance_sum(node: Union[BTNode, None], d: int) -> int:
    """ Return the sum of data at distance d from node.
    Assume all data in tree rooted at node is of type int
    and d is non-negative.

    >>> btnode_distance_sum(None, 1)
    0
    >>> bt = BTNode(5, BTNode(6), BTNode(7))
    >>> btnode_distance_sum(bt, 7)
    0
    >>> btnode_distance_sum(bt, 0)
    5
    >>> btnode_distance_sum(bt, 1)
    13
    """
    if node is None or node.data is None:
        return 0
    elif d == 0:
        return node.data if isinstance(node.data, int) else 0
    elif d < 0:
        return 0
    else:
        return sum([btnode_distance_sum(node.left, d - 1),
                    btnode_distance_sum(node.right, d - 1)])

    # Heap solution
    # node.data: int
    # if node is None:
    #     return 0
    # elif d < 0:
    #     return 0
    # elif d == 0:
    #     return node.data
    # else:
    #     return (btnode_distance_sum(node.left, d - 1) +
    #             btnode_distance_sum(node.right, d - 1))


def btnode_list_distance(node: Union[BTNode, None], d: int) -> list:
    """ Return list of node data distance d from root node.
    Assume d is non-negative.

    >>> btnode_list_distance(None, 1)
    []
    >>> bt = BTNode(5, BTNode(6), BTNode(7))
    >>> btnode_list_distance(bt, 0)
    [5]
    >>> btnode_list_distance(bt, 1)
    [6, 7]
    >>> btnode_list_distance(bt, 2)
    []
    """
    if node is None or node.data is None:
        return []
    elif d == 0:
        return [node.data]
    elif d < 0:
        return []
    else:
        return sum([btnode_list_distance(node.left, d - 1),
                    btnode_list_distance(node.right, d - 1)], [])


def btnode_string_distance(node: Union[BTNode, None], d: int) -> str:
    """ Return concatenation of data distance d from node.
    Assume all data in tree rooted at node are strings and d is non-negative.

    >>> btnode_string_distance(None, 1)
    ''
    >>> bt = BTNode("a", BTNode("b"), BTNode("c"))
    >>> btnode_string_distance(bt, 0)
    'a'
    >>> btnode_string_distance(bt, 1)
    'bc'
    >>> btnode_string_distance(bt, 2)
    ''
    """
    # if node is None or node.data is None:
    #     return ''
    # elif d == 0:
    #     return str(node.data)
    # else:
    #     s = ''
    #     s += btnode_string_distance(node.left, d - 1)
    #     s += btnode_string_distance(node.right, d - 1)
    #     return s

    # Version 2
    # if node is None or node.data is None:
    #     return ''
    # elif d == 0:
    #     return str(node.data)
    # else:
    #     return ''.join([btnode_string_distance(node.left, d - 1),
    #                     btnode_string_distance(node.right, d - 1)])

    # Version 3
    if node is None:
        return ''
    elif d < 0:
        return ''
    elif d == 0:
        return str(node.data)
    else:
        return (btnode_string_distance(node.left, d - 1) +
                btnode_string_distance(node.right, d - 1))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
