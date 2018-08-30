"""Tree traversals

=== CSC148 Winter 2018 ===
Department of Computer Science,
University of Toronto
__author__ = 'Eric K'

=== Module Description ===
This module contains methods of traversing different tree data structures.
"""
from tree2 import Tree
from binary_tree2 import BinaryTree
from bst2 import *
from tree2_functions import descendants_from_list
from queue_api import Queue
from typing import Callable, Any, Optional, Union


#           *********************************
#               ===> Tree traversals <===
#           *********************************
def preorder_visit(t: Tree, act: Callable[[Tree], None]) -> None:
    """
    Visit each node of Tree t in preorder, and act on the nodes
    as they are visited.

    >>> node: Tree
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> preorder_visit(t, act)
    0
    1
    4
    5
    6
    2
    7
    3
    """
    if t.value is None:
        pass
    else:
        act(t)
        for subtree in t.children:
            preorder_visit(subtree, act)


def postorder_visit(t: Tree, act: Callable[[Tree], None]) -> None:
    """
    Visit each node of t in postorder, and act on it when it is visited.

    >>> node: Tree
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> postorder_visit(t, act)
    4
    5
    6
    1
    7
    2
    3
    0
    """
    if t.value is None:
        pass
    else:
        for subtree in t.children:
            postorder_visit(subtree, act)
        act(t)


def levelorder_visit(t: Tree, act: [[Tree], None]) -> None:
    """
    Visit every node in Tree t in level order and act on the node
    as you visit it.

    >>> node: Tree
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> levelorder_visit(t, act)
    0
    1
    2
    3
    4
    5
    6
    7
    """
    to_visit = Queue()
    to_visit.add(t)

    while not to_visit.is_empty():
        tree = to_visit.remove()
        act(tree)
        for subtree in tree.children:
            to_visit.add(subtree)

    # or...
    # if t.value is None:
    #     pass
    #
    # q = Queue()
    # q.add(t)
    # while q.is_empty() is False:      # while not q.is_empty():
    #     t = q.remove()
    #     t: Tree
    #
    #     act(t)
    #
    #     for s in t.children:
    #         q.add(s)


def visit_level(t: Tree, level: int, act: Callable[[Tree], None]) -> int:
    """
    Visit nodes of t at level n, act on them, and return the number visited.

    >>> node: Tree
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> visit_level(t, 1, act)
    1
    2
    3
    3
    """
    if t.value is None:
        pass
    elif level == 0:
        # This is like a leaf -> return 1 when we act on a tree.
        act(t)
        return 1
    else:
        # We aren't at the level that we want, so we need to progressively
        # decrease by 1 level each time we go to the next level.
        return sum(visit_level(s, level - 1, act) for s in t.children)

    # or...
    # if t.value is None:
    #     pass
    # elif level == 0:
    #     act(t)
    #     return 1
    # else:
    #     sum = 0
    #     for subtree in t.children:
    #         sum += visit_level(subtree, level - 1, act)
    #     return sum


def levelorder_visit_recursive(t: Tree, act: Callable[[Tree], None]) -> None:
    """
    Visit Tree t in level order and act on its nodes.

    >>> node: Tree
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> levelorder_visit_recursive(t, act)
    0
    1
    2
    3
    4
    5
    6
    7
    """
    if t.value is None:
        pass
    else:
        level = 0
        visited = visit_level(t, level, act)
        while visited > 0:
            level += 1
            visited = visit_level(t, level, act)


def string_postorder(t: Tree) -> str:
    """
    Return a string of tree in post order

    >>> t = Tree("a", [Tree("b"), Tree("c", [Tree("d")]), \
Tree("e", [Tree("f")]), Tree("g")])
    >>> string_postorder(t)
    'bdcfega'
    >>> string_postorder(Tree("a"))
    'a'
    >>> t = Tree("a", [Tree("b", [Tree("c")]), Tree("d")])
    >>> string_postorder(t)
    'cbda'
    """
    if t.value is None:
        return ''
    else:
        return ''.join([string_postorder(s) for s in t.children]) + str(t.value)

    # Version 2
    # if t.value is None:
    #     return ''
    # else:
    #     s = ''
    #     for subtree in t.children:
    #         s += string_postorder(subtree)
    #     s += str(t.value)
    #     return s


# Midterm 2 2018 Heap
def list_preorder(t: Tree) -> list:
    """
    Return a list of t's values in preorder.

    >>> list_preorder(Tree(0))
    [0]
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> list_preorder(t)
    [1, 2, 3, 4]
    """
    if t.value is None:
        return []
    else:
        return [t.value] + sum([list_preorder(s) for s in t.children], [])

    # if t.value is None:
    #     return []
    # elif t.children == []:
    #     return [t.value]
    # else:
    #     pre = [t.value]
    #     for subtree in t.children:
    #         pre.extend(list_preorder(subtree))
    #     return pre


def list_postorder(t: Tree) -> list:
    """
    Return a list of t's values in postorder.

    >>> list_postorder(Tree(0))
    [0]
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> list_postorder(t)
    [3, 2, 4, 1]
    """
    if t.value is None:
        return []
    # elif t.children == []:
    #     return [t.value]
    else:
        return sum([list_postorder(s) for s in t.children], []) + [t.value]

    # Version 2
    # if t.value is None:
    #     return []
    # else:
    #     post = []
    #     for s in t.children:
    #         post.extend(list_postorder(s))
    #     return post + [t.value]


#           ****************************************
#               ===> Binary tree traversals <===
#           ****************************************
def b_postorder_visit(t: BinaryTree, act: Callable[[BinaryTree], Any]) -> None:
    """
    Visit BinaryTree t in postorder and act on nodes as you visit.

    >>> node: BinaryTree
    >>> bt = BinaryTree(5, BinaryTree(7), BinaryTree(9))
    >>> def f(node): print(node.value)
    >>> b_postorder_visit(bt, f)
    7
    9
    5
    """
    if t is None or t.value is None:
        pass
    else:
        b_postorder_visit(t.left, act) if t.left is not None else None
        b_postorder_visit(t.right, act) if t.right is not None else None
        act(t)


def b_preorder_visit(t: BinaryTree, act: Callable[[BinaryTree], Any]) -> None:
    """
    Visit BinaryTree t in preorder and act on nodes as you visit.

    >>> node: BinaryTree
    >>> bt = BinaryTree(5, BinaryTree(7), BinaryTree(9))
    >>> def f(node): print(node.value)
    >>> b_preorder_visit(bt, f)
    5
    7
    9
    """
    if t is None or t.value is None:
        pass
    else:
        act(t)
        b_preorder_visit(t.left, act) if t.left is not None else None
        b_preorder_visit(t.right, act) if t.right is not None else None


def b_inorder_visit(t: BinaryTree, act: Callable[[BinaryTree], Any]) -> None:
    """
    Visit each node of binary tree rooted at root in order and act.

    >>> node: BinaryTree
    >>> bt = BinaryTree(5, BinaryTree(7), BinaryTree(9))
    >>> def f(node): print(node.value)
    >>> b_inorder_visit(bt, f)
    7
    5
    9
    """
    if t is None or t.value is None:
        pass
    else:
        b_inorder_visit(t.left, act) if t.left is not None else None
        act(t)
        b_inorder_visit(t.right, act) if t.right is not None else None


#           ****************************************
#                   ===> BST traversals <===
#           ****************************************
def inorder_visit_v3(b: Optional[BTNode],
                     visit: Callable[[BTNode], Any]) -> None:
    """
    Visit each node of binary tree rooted at root in order.

    >>> b = BTNode("A", BTNode("C"), BTNode("D"))
    >>> node: BTNode
    >>> def f(node): print(node.data)
    >>> inorder_visit_v3(b, f)
    C
    A
    D
    """
    if b is None or b.data is None:
        pass
    else:
        inorder_visit_v3(b.left, visit) if b.left is not None else None
        visit(b)
        inorder_visit_v3(b.right, visit) if b.right is not None else None


def preorder_visit_v3(b: Optional[BTNode],
                      visit: Callable[[BTNode], Any]) -> None:
    """
    Visit each node of binary tree rooted at root in preorder
    and perform effect.


    >>> b = BTNode("A", BTNode("C"), BTNode("D"))
    >>> node: BTNode
    >>> def f(node): print(node.data)
    >>> preorder_visit_v3(b, f)
    A
    C
    D
    """
    if b is None or b.data is None:
        pass
    else:
        visit(b)
        preorder_visit_v3(b.left, visit) if b.left is not None else None
        preorder_visit_v3(b.right, visit) if b.right is not None else None


def postorder_visit_v3(b: Union[BTNode],
                       visit: Callable[[BTNode], Any]) -> None:
    """
    Visit each node of binary tree rooted at root in postorder
    and perform effect.

    >>> b = BTNode("A", BTNode("C"), BTNode("D"))
    >>> node: BTNode
    >>> def f(node): print(node.data)
    >>> postorder_visit_v3(b, f)
    C
    D
    A
    """
    if b is None or b.data is None:
        pass
    else:
        postorder_visit_v3(b.left, visit) if b.left is not None else None
        postorder_visit_v3(b.right, visit) if b.right is not None else None
        visit(b)


# def levelorder_visit_v3(b: Union[BTNode],
#                         visit: Callable[[BTNode], Any]) -> None:
#     """
#     Visit each node of binary tree rooted at root in level order.
#
#     If tree rooted at root is empty, do nothing.
#
#     >>> b = BTNode("A", BTNode("C", BTNode("B")), BTNode("D"))
#     >>> node: BTNode
#     >>> def f(node): print(node.data)
#     >>> levelorder_visit_v3(b, f)
#     A
#     C
#     D
#     B
#     """
#     # if b is None or b.data is None:
#     #     pass
#     # else:
#     #     q = Queue()
#     #     q.add(b)
#     #     while not q.is_empty():
#     #         btree = q.remove()
#     #         btree: BTNode
#     #         visit(btree)
#     #
#     #         q.add(b.left) if b.left is not None else None
#     #         q.add(b.right) if b.right is not None else None
#
#     if b is None or b.data is None:
#         pass
#
#     else:
#         q = Queue()
#         q.add(b)
#         while not q.is_empty():
#             btree = q.remove()
#             btree: BTNode
#
#             visit(btree)
#
#             if b.left is not None:
#                 q.add(b.left)
#             if b.right is not None:
#                 q.add(b.right)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
