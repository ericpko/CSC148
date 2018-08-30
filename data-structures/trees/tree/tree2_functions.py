"""Tree functions

=== CSC148 Winter 2018 ===
Department of Computer Science,
University of Toronto
__author__ = 'Eric K'

=== Module Description ===
This module contains some functions for the tree2.py implementation. Note that
some of these could be modified into methods.
"""
from tree2 import Tree
from typing import Any, Callable, List, Optional
from queue_api import Queue


#   ************ General tree traversal pattern ************
#   if t.value is None:
#       return base case
#   elif t.children == []: # we are at a leaf
#       return something at leaf
#   else:
#       # we are at an internal node
#       ...
#       for subtree in t.children:
#           do something
#       return recurse
#   ********************************************************

def is_leaf(t: Tree) -> bool:
    """Return whether Tree t is a leaf

    >>> Tree(5).is_leaf()
    True
    >>> Tree(5,[Tree(7)]).is_leaf()
    False
    """
    if t.value is None:
        return False
    return t.children == []

    # or...
    # if t.value is None:
    #     return False
    # elif t.children == []:
    #     return True
    # else:
    #     return False


def height(t: Tree) -> int:
    """
    Return length of longest path, + 1, in tree rooted at t.

    >>> t = Tree(5)
    >>> t.height()
    1
    >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> t.height()
    3
    """
    if t.value is None:
        return 0
    elif t.children == []:
        return 1
    else:
        return 1 + max(s.height() for s in t.children)


def flatten(t: Tree) -> list:
    """ Return a list of all values in tree rooted at t.

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
    if t.value is None:
        return []
    else:
        return [t.value] + sum([s.flatten() for s in t.children], [])


def list_internal(t: Tree) -> List[Any]:
    """
    Return list of values in internal nodes of t.

    >>> t = Tree(0)
    >>> list_internal(t)
    []
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_internal(t)
    >>> L.sort()
    >>> L
    [0, 1, 2]
    """
    if t.value is None:
        return []
    elif t.children == []:
        # then we're at a leaf -> so return []
        return []
    else:
        # now we're at internal nodes.
        return [t.value] + sum([list_internal(s) for s in t.children], [])

    # or...
    # if t.value is None:
    #     return []
    # elif t.children == []:
    #     return []
    # else:
    #     internal = [t.value]
    #     for subtree in t.children:
    #         internal.extend(list_internal(subtree))
    #     return internal


def list_internal_trees(t: Tree) -> List['Tree']:
    """ Return a list of Tree t's non-None children.
    These are all internal nodes.

    """
    if t.value is None:
        return []
    elif t.children == []:
        return []
    else:
        return [t] + sum([s.list_internal_trees() for s in t.children], [])


def count_internal(t: Tree) -> int:
    """
    Return number of internal nodes of t.

    >>> t = Tree(0)
    >>> count_internal(t)
    0
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> t
    Tree(0, [Tree(1, [Tree(4), Tree(5), Tree(6)]), Tree(2, [Tree(7), \
Tree(8)]), Tree(3)])
    >>> count_internal(t)
    3
    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    """
    if t.value is None:
        return 0
    elif t.children == []:
        # we're at a leaf -> not internal.
        return 0
    else:
        # we're at an internal node
        return 1 + sum(count_internal(subtree) for subtree in t.children)

    # or...
    # if t.value is None:
    #     return 0
    # elif t.children == []:
    #     return 0
    # else:
    #     internal = 1
    #     for subtree in t.children:
    #         internal += count_internal(subtree)
    #     return internal


def count_leaves(t: Tree) -> int:
    """
    Return the number of leaves in Tree t.

    >>> t = Tree(7)
    >>> count_leaves(t)
    1
    >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> count_leaves(t)
    6
    """
    if t.value is None:
        return 0
    elif t.children == []:
        return 1
    else:
        return sum(count_leaves(subtree) for subtree in t.children)


def list_leaves(t: Tree) -> list:
    """
    Return list of values in leaves of t.

    >>> t = Tree(0)
    >>> list_leaves(t)
    [0]
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_leaves(t)
    >>> list_.sort() # so list_ is predictable to compare
    >>> list_
    [3, 4, 5, 6, 7, 8]
    """
    if t.value is None:
        return []
    elif t.children == []:
        # then we're at a leaf
        return [t.value]
    else:
        return sum([list_leaves(s) for s in t.children], [])


def list_interior(t: Tree) -> List:
    """
    Return list of values in interior nodes of t.

    >>> t = Tree(0)
    >>> list_interior(t)
    []
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_interior(t)
    >>> L.sort()
    >>> L
    [0, 1, 2]
    """
    if t.value is None:
        return []
    elif t.children == []:
        # then we're at a leaf
        return []
    else:
        return [t.value] + sum([list_interior(s) for s in t.children], [])


def sum_internal(t: Tree) -> int:
    """
    Return sum of the internal (non-leaf) nodes of t.

    Assume all nodes have integer values.

    >>> t = Tree(0)
    >>> sum_internal(t)
    0
    >>> t = descendants_from_list(Tree(1), [2, 3, 4, 5, 6, 7, 8, 9], 3)
    >>> sum_internal(t)
    6
    """
    if t.value is None:
        return 0
    elif t.children == []:
        return 0
    else:
        if isinstance(t.value, int):
            return t.value + sum(sum_internal(s) for s in t.children)
        else:
            return sum(sum_internal(s) for s in t.children)

    # or...
    # if t.value is None:
    #     return 0
    # elif len(t.children) == 0:
    #     # we're at a leaf -> don't care about leaves here.
    #     return 0
    # else:
    #     # we're at an internal node.
    #     return t.value + sum(sum_internal(subtree) for subtree in t.children)

    # if t.value is None:
    #     return 0
    # elif t.children == []:
    #     return 0
    # else:
    #     return t.value if isinstance(t.value, int) else 0 + sum(
    #         sum_internal(s) for s in t.children)


def sum_leaves(t: Tree) -> int:
    """
    Return sum of the leaves of t.
    >>> t = Tree(0)
    >>> sum_leaves(t)
    0
    >>> t = descendants_from_list(Tree(1), [2, 3, 4, 5, 6, 7, 8, 9], 3)
    >>> sum_leaves(t)
    39
    """
    if t.value is None:
        return 0
    elif t.children == []:
        return t.value if isinstance(t.value, int) else 0
    else:
        return sum(sum_leaves(s) for s in t.children)

    # or...
    # if t.value is None:
    #     return 0
    # elif len(t.children) == 0:
    #     # Then we're at a leaf
    #     return t.value if isinstance(t.value, int) else 0
    #     # Same as:
    #     # if isinstance(t.value, int):
    #     #     return t.value
    #     # else:
    #     #     return 0
    # else:
    #     leaf_total = 0
    #     for subtree in t.children:
    #         leaf_total += sum_leaves(subtree)
    #     return leaf_total


def arity(t: Tree) -> int:
    """
    Return the maximum branching factor (arity) of Tree t.

    >>> t = Tree(23)
    >>> arity(t)
    0
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> arity(tn1)
    4
    """
    if t.value is None:
        return 0
    elif t.children == []:
        # Then we are at a leaf (a tree with a single root).
        return 0
    else:
        # We are at an internal node that has a branch.
        return max(len(t.children), max(arity(s) for s in t.children))

    # or...
    # if t.value is None:
    #     return 0
    # elif t.children == []:
    #     return 0
    # else:
    #     branch = len(t.children)
    #     sub_branch = []
    #     for s in t.children:
    #         sub_branch.extend([arity(s)])
    #     sub_branch = max(sub_branch)
    #     return max(branch, sub_branch)


def two_count(t: Tree) -> int:
    """Return the number of times 2 occurs as a value in any node of t.
    precondition - t is a non-empty tree with number values

    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(2), Tree(5.75)])
    >>> tn3 = Tree(3, [Tree(6), Tree(2)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> two_count(tn1)
    3
    """
    if t.value is None:
        return 0
    elif t.value == 2:
        return 1 + sum(two_count(s) for s in t.children)
    else:
        return sum(two_count(s) for s in t.children)

    # Version 2
    # return 1 if t.value == 2 else 0 + sum(two_count(c) for c in t.children)


def contains_test_passer(t: Tree, test: Callable[[Any], bool]) -> bool:
    """
    Return whether t contains a value that test(value) returns True for.

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4.5, 5, 6, 7.5, 8.5], 4)
    >>> n: int
    >>> def greater_than_nine(n): return n > 9
    >>> contains_test_passer(t, greater_than_nine)
    False
    >>> def even(n): return n % 2 == 0
    >>> contains_test_passer(t, even)
    True
    """
    if t.value is None:
        return False
    else:
        # we don't need to distinguish between leafs and internal nodes
        if test(t.value):
            return True
        else:
            return any(contains_test_passer(s, test) for s in t.children)


def list_if(t: Tree, p: Callable[[Any], bool]) -> list:
    """
    Return a list of values in Tree t that satisfy predicate p(value).

    Assume p is defined on all of t's values.

    >>> v: int
    >>> def p(v): return v > 4
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_if(t, p)
    >>> set(list_) == {5, 6, 7, 8}
    True
    >>> def p(v): return v % 2 == 0
    >>> list_ = list_if(t, p)
    >>> set(list_) == {0, 2, 4, 6, 8}
    True
    """
    # version 1
    if t.value is None:
        return []
    elif p(t.value):
        return [t.value] + sum([list_if(s, p) for s in t.children], [])
    else:
        return sum([list_if(s, p) for s in t.children], [])

    # version 2
    # if t.value is None:
    #     return []
    # else:
    #     # we don't need to distinguish between leaves and internal nodes.
    #     if p(t.value):
    #         return [t.value] + sum([list_if(s, p) for s in t.children], [])
    #     else:
    #         return sum([list_if(subtree, p) for subtree in t.children], [])

    # version 3
    # if t.value is None:
    #     return []
    # else:
    #     return [t.value] + sum([list_if(s, p) for s in t.children], []) \
    #         if p(t.value) \
    #         else sum([list_if(s, p) for s in t.children], [])


# helper function that may be useful in the functions above
def gather_lists(list_: List[list]) -> list:
    """
    Concatenate all the sublists of L and return the result.

    >>> gather_lists([[1, 2], [3, 4, 5]])
    [1, 2, 3, 4, 5]
    >>> gather_lists([[6, 7], [8], [9, 10, 11]])
    [6, 7, 8, 9, 10, 11]
    """
    new_list = []
    for l in list_:
        new_list += l
    return new_list
    # equivalent to...
    # return sum([list_ for list_ in list_], [])


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


# Challenging!
def prune(t: Tree, predicate: Callable[[object], bool]) -> Optional[Tree]:
    """ Return a new tree with the same values as t, except it
    prunes (omits) all paths of t that start with nodes where
    predicate(node.value) == False. If predicate(t.value) == False,
    then prune returns None.
    Assume that all values in t are ints, and that predicate
    always takes an int and returns a bool.

    >>> v: int
    >>> t1 = Tree(6, [Tree(8) , Tree(9)])
    >>> t2 = Tree(4, [Tree(11), Tree(10)])
    >>> t3 = Tree(7, [Tree(3), Tree(12)])
    >>> t = Tree(5, [t1, t2, t3])
    >>> t3_pruned = Tree(7, [Tree(12)])
    >>> def predicate (v) : return v > 4
    >>> prune(t, predicate) == Tree(5, [t1, t3_pruned])
    True
    """
    # version 1
    # if t.value is None:
    #     pass
    # elif not predicate(t.value):
    #     pass
    # else:
    #     new_t = Tree(t.value)
    #     for s in t.children:
    #         subtree = prune(s, predicate)
    #         if subtree is not None:
    #             new_t.children.append(subtree)
    #     return new_t

    # version 2 ** modifies t ***
    # if t.value is None:
    #     pass
    # elif not predicate(t.value):
    #     pass
    # else:
    #     list_ = [prune(subtree, predicate) for subtree in t.children]
    #     t.children = [x for x in list_ if x is not None]
    #     return t

    # Version 3
    # if t.value is None:
    #     pass
    # elif not predicate(t.value):
    #     pass
    # else:
    #     new_t = Tree(t.value)
    #     lst = [prune(s, predicate) for s in t.children]
    #     new_t.children = [s for s in lst if s is not None]
    #     return new_t

    # version 4:
    # if t.value is None:
    #     pass
    # elif not predicate(t.value):
    #     return Tree()
    # else:
    #     new_t = Tree(t.value)
    #     for subtree in t.children:
    #         tree = prune(subtree, predicate)
    #         if tree.value is not None:
    #             new_t.children.append(tree)
    #     return new_t

    if t.value is None:
        pass
    elif predicate(t.value) is False:
        pass
    else:
        new_t = Tree(t.value)
        for s in t.children:
            child = prune(s, predicate)
            if child is not None:
                new_t.children.append(child)
        return new_t

    # version 5
    # if t is None or t.value is None:
    #     pass
    # elif predicate(t.value) is False:
    #     pass
    # else:
    #     new_t = Tree(t.value)
    #     children = [prune(s, predicate) for s in t.children]
    #     new_t.children = [x for x in children if x is not None]
    #     return new_t


# Challenging! Seen on final exam
def pathlength_sets(t: Tree) -> None:
    """
    Replace the value of each node in Tree t by a set containing all
    path lengths from that node to any leaf. A path's length is the
    number of edges it contains.

    >>> t = Tree(5)
    >>> pathlength_sets(t)
    >>> print(t)
    {0}
    >>> t.children.append(Tree(17))
    >>> t.children.append(Tree(13, [Tree(11)]))
    >>> pathlength_sets(t)
    >>> print(t)
    {1, 2}
       {0}
       {1}
          {0}
    """
    if t.value is None:
        pass
    elif t.children == []:
        t.value = {0}
    else:
        t.value = set()
        for s in t.children:
            pathlength_sets(s)
            t.value = t.value.union(s.value)
        t.value = set([e + 1 for e in t.value])

    # Solution if it asked for height:
    # if t.value is None:
    #     pass
    # elif t.children == []:
    #     t.value = {1}
    # else:
    #     t.value = {1}
    #     for s in t.children:
    #         pathlength_sets(s)
    #         t.value = t.value.union(s.value)
    #     t.value = set([e + 1 for e in t.value])


def mem_list(t: Tree) -> list:
    """
    Helper for unique_paths
    """
    if t is None or t.value is None:
        return []
    elif t.children == []:
        return [id(t)]
    else:
        return [id(t)] + sum([mem_list(s) for s in t.children], [])


def unique_paths(t: Tree) -> bool:
    """
    Return whether there is a unique path from t to each of it's
    decendents.

    Assume the trees are the same if they have the same memory addresses

    >>> t1 = Tree(1)
    >>> t2 = Tree(2)
    >>> t3 = Tree(3, [t1, t2])
    >>> unique_paths(t3)
    True
    >>> t4 = Tree(4, [t3, t1])
    >>> unique_paths(t4)
    False
    """
    mem = mem_list(t)
    return len(mem) == len(set(mem))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
