"""Tree

=== University of Toronto ===
Department of Computer Science
__author__ = 'Eric K'

=== Module Description ===
This module contains a simple tree implementation as well some related
tree functions.
"""
from typing import Optional, List, Union
import random


class Tree:
    """
    A recursive tree data structure.
    """
    # === Private Attributes ===
    # _root:
    #     The item stored at this tree's root,
    #     or None if the tree is empty.
    # _subtrees:
    #     The list of all subtrees of this tree.
    _root: Optional[object]
    _subtrees: List['Tree']

    # === Representation Invariants ===
    # - If self._root is None then self._subtrees is an empty list.
    #   This setting of attributes represents an empty Tree.
    # - self._subtrees may be empty when self._root is not None.
    #   This setting of attributes represents a tree consisting of just one
    #   node.

    # === Traversal Template ===
    # if self._root is None:
    #   ...
    # elif self._subtrees == []:
    #   # Then we are at a leaf
    #   ...
    # else:
    #   # We are at an internal node
    #   for subtree in self._subtrees:
    #       recursive call ...

    def __init__(self, root: object=None, subtrees: List['Tree']=None) -> None:
        """Initialize a new Tree with the given root value and subtrees.

        If <root> is None, the tree is empty.
        Precondition: if <root> is None, then <subtrees> is empty.
        """
        self._root = root
        # if not None, make a copy of <subtrees>.
        self._subtrees = subtrees.copy() if subtrees else []

        if self._root is None:
            assert self._subtrees == []

    def is_empty(self) -> bool:
        """Return True if this tree is empty.

        >>> t1 = Tree(None, [])
        >>> t1.is_empty()
        True
        >>> t2 = Tree(3, [])
        >>> t2.is_empty()
        False
        """
        return self._root is None

    def subtrees(self) -> List['Tree']:
        """Return a list of the subtrees of <self> or an empty
        list if <self._subtrees> is empty.
        This method can be used for making Tree functions.

        """
        return self._subtrees

    def value(self) -> object:
        """Return the object at <self._root>
        This method can be used for making Tree functions. Might want
        to call this method <root>

        """
        return self._root

    def __str__(self) -> str:
        """Return a string representation of this tree.

        For each node, its item is printed
        before any of its descendants' items.

        You may find this method helpful
        for debugging.
        >>> t1 = Tree(1, [])
        >>> t2 = Tree(2, [])
        >>> t3 = Tree(3, [])
        >>> t4 = Tree(4, [t1, t2, t3])
        >>> t5 = Tree(5, [t4])
        >>> print(t5)
        5
          4
            1
            2
            3
        """
        return self._str_indented().strip()     # strip the last \n

    def _str_indented(self, depth: int = 0) -> str:
        """A helper method for __str__
        """
        if self.is_empty():
            return ''
        else:
            s = depth * '  ' + str(self._root) + '\n'
            for subtree in self._subtrees:
                s += subtree._str_indented(depth + 1)
            return s

    def __eq__(self, other: 'Tree') -> bool:
        """Return whether <self> and <other> are equal.

        Hint: you can use the standard structure for recursive functions on
        trees, except that you'll want to loop using an index:
          `for i in range(len(self._subtrees))`)

        This way, you can access the corresponding subtree in `other`.

        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t2 = Tree(1, [lt, rt])
        >>> t == t2
        True
        >>> t == lt
        False
        """
        # return (type(self) is type(other) and
        #         self._root == other.value and
        #         self._subtrees == other.subtrees())

        # or...
        if self.is_empty():
            if other.is_empty():
                return True
            else:
                return False
        elif self._root != other._root:
            return False
        else:
            return all(self._subtrees[i].__eq__(other._subtrees[i])
                       for i in range(len(self._subtrees)))

    def __len__(self) -> int:
        """Return the number of nodes contained in this tree.

        >>> t1 = Tree(None, [])
        >>> len(t1)
        0
        >>> t2 = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> len(t2)
        3
        >>> t3 = Tree(18, [Tree(55, []), \
                        Tree(3, [Tree(4, []), Tree(1, [])])])
        >>> t3.__len__()
        5
        """
        if self.is_empty():
            return 0
        else:
            return 1 + sum(len(s) for s in self._subtrees)

    def height(self) -> int:
        """Return the height of this tree.

        >>> t1 = Tree(None, [])
        >>> t1.height()
        0
        >>> t2 = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> t2.height()
        2
        >>> t3 = Tree(18, [Tree(55, []), \
                        Tree(3, [Tree(4, []), Tree(1, [])])])
        >>> t3.height()
        3
        """
        if self.is_empty():
            return 0
        elif self._subtrees == []:
            return 1
        else:
            return 1 + max(s.height() for s in self._subtrees)

    def count(self, item: object) -> int:
        """Return the number of occurrences of <item> in this tree.

        >>> t = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> t.count(3)
        1
        >>> t.count(100)
        0
        >>> bigger = Tree(19, [ \
                Tree(3, [Tree(4, []), Tree(1, [])]), \
                Tree(3, [Tree(4, []), Tree(4, [])]) \
                ])
        >>> bigger.count(4)
        3
        """
        if self.is_empty():
            return 0
        elif self._root == item:
            return 1
        else:
            return sum(subtree.count(item) for subtree in self._subtrees)

    def __contains__(self, item: object) -> bool:
        """Return whether <item> is in this tree.

        >>> t = Tree(1, [Tree(2, []), Tree(5, [])])
        >>> 1 in t  # Same as t.__contains__(1)
        True
        >>> 5 in t
        True
        >>> 4 in t
        False
        >>> t2 = Tree(4, [t])
        >>> 5 in t2
        True
        >>> 4 in t2
        True
        >>> 3 in t2
        False
        """
        if self.is_empty():
            return False
        elif self._root == item:
            return True
        else:
            return any(item in subtree for subtree in self._subtrees)

    def leaves(self) -> list:
        """Return a list of all of the leaf items in the tree.

        >>> Tree(None, []).leaves()
        []
        >>> t = Tree(1, [Tree(2, []), Tree(5, [])])
        >>> t.leaves()
        [2, 5]
        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t.leaves()
        [4, 5, 6, 7]
        """
        if self.is_empty():
            return []
        elif self._subtrees == []:
            return [self._root]
        else:
            return sum([subtree.leaves() for subtree in self._subtrees], [])

    def leaf_count(self) -> int:
        """Return the number of leaves in this Tree.

        >>> Tree(None, []).leaf_count()
        0
        >>> t = Tree(1, [Tree(2, []), Tree(5, [])])
        >>> t.leaf_count()
        2
        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t.leaf_count()
        4
        """
        if self.is_empty():
            return 0
        elif len(self._subtrees) == 0:
            return 1
        else:
            return sum(subtree.leaf_count() for subtree in self._subtrees)

        # or...
        # return len(self.leaves())

    def arity(self) -> int:
        """Return the maximum branching factor (arity) of Tree t.

        >>> Tree().arity()
        0
        >>> t = Tree(23)
        >>> t.arity()
        0
        >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
        >>> tn3 = Tree(3, [Tree(6), Tree(7)])
        >>> tn1 = Tree(1, [tn2, tn3])
        >>> tn1.arity()
        4
        """
        if self.is_empty():
            return 0
        elif self._subtrees == []:
            return 0
        else:
            # We are at an internal node that has a branch.
            return max(len(self._subtrees),
                       max(s.arity() for s in self._subtrees))

    def flatten(self):
        """ Return a list of all values in tree rooted at self.

        """
        if self.is_empty():
            return []
        else:
            return [self._root] + sum([s.flatten() for s in self._subtrees], [])

    def is_leaf(self):
        """Return whether Tree self is a leaf

        @param Tree self:
        @rtype: bool

        >>> Tree(5).is_leaf()
        True
        >>> Tree(5,[Tree(7)]).is_leaf()
        False
        """
        if self.is_empty():
            return False
        return self._subtrees == []

    def add_subtrees(self, new_trees: 'Tree') -> None:
        """Add the trees in <new_trees> as subtrees of this tree.

        Raise ValueError if this tree is empty.

        @type self: Tree
        @type new_trees: list[Tree]
        @rtype: None
        """
        if self.is_empty():
            raise ValueError()
        else:
            self._subtrees.extend(new_trees)

    # You may find this method helpful for debugging.
    def print_tree(self):
        """Print all of the items in this tree.

        For each node, its item is printed before any of its
        descendants' items. The output is nicely indented.

        @type self: Tree
        @rtype: None
        """
        if not self.is_empty():
            # This prints the root item before all of the subtrees.
            print(self._root)
            for subtree in self._subtrees:
                subtree.print_tree()

                # Or alternately, simply call
                # self.print_tree_indent()

    def print_tree_indent(self, depth: int=0) -> None:
        """Print all of the items in this tree at a set indentation level.

        """
        if not self.is_empty():
            print(depth * '  ' + str(self._root))
            for subtree in self._subtrees:
                subtree.print_tree_indent(depth + 1)

    def delete_root(self) -> None:
        """Remove the root item of this tree.

        """
        if len(self._subtrees) == 0:
            # Base case when empty or just one node
            self._root = None
        else:
            chosen_subtree = self._subtrees[0]
            self._root = chosen_subtree._root
            self._subtrees = (chosen_subtree._subtrees +
                              self._subtrees[1:])

    def delete_item(self, item: object) -> bool:
        """Delete *one* occurrence of item from this tree.
        Return True if item was deleted, and False otherwise.

        """
        if self.is_empty():
            return False
        elif self._root == item:
            self.delete_root()
            return True
        else:
            for subtree in self._subtrees:
                # Try to delete item from current subtree
                # If it works, return!
                if subtree.delete_item(item):
                    # If the subtree is now empty, remove it!
                    if subtree.is_empty():
                        self._subtrees.remove(subtree)
                    return True
            return False

    # TODO: implement
    # def branching_factor(self) -> float:
    #     """Return the average branching factor of this tree.
    #
    #     Return 0 if this tree is empty or consists of just a single root node.
    #     Remember to ignore all 0's coming from leaves in this calculation.
    #
    #     >>> Tree(None, []).branching_factor()
    #     0.0
    #     >>> t = Tree(1, [Tree(2, []), Tree(5, [])])
    #     >>> t.branching_factor()
    #     2.0
    #     >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
    #     >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
    #                       Tree(10, [])])
    #     >>> t = Tree(1, [lt, rt])
    #     >>> t.branching_factor()
    #     3.0
    #     """
    #     pass
    #
    # def _branching_factor_helper(self) -> Tuple[int, int]:
    #     """Return a tuple (x,y) where:
    #
    #     x is the total branching factor of all non-leaf nodes in this tree,
    #     and y is the total number of non-leaf nodes in this tree.
    #     """
    #     pass

    def insert(self, item: object) -> None:
        """Insert <item> into this tree using the following algorithm.

            1. If the tree is empty, <item> is the new root of the tree.
            2. If the tree has a root but no subtrees, create a
               new tree containing the item, and make this new tree a subtree
               of the original tree.
            3. Otherwise, pick a random number between 1 and 3 inclusive.
                - If the random number is 3, create a new tree containing
                  the item, and make this new tree a subtree of the original.
                - If the random number is a 1 or 2, pick one of the existing
                  subtrees at random, and *recursively insert* the new item
                  into that subtree.

        >>> t = Tree(None, [])
        >>> t.insert(1)
        >>> 1 in t
        True
        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t.insert(100)
        >>> 100 in t
        True
        """
        # Use the function randint as follows:
        # >>> random.randint(1, 3)
        # 2  # Randomly returns 1, 2, or 3

        if self.is_empty():
            self._root = item
        elif len(self._subtrees) == 0:
            new_tree = Tree(item)
            self._subtrees.append(new_tree)
        else:
            index = random.randint(1, 3)
            new_tree = Tree(item)
            if index == 3:
                self._subtrees.append(new_tree)
            else:
                index = random.randint(0, len(self._subtrees) - 1)
                self._subtrees[index].insert(item)

    def average(self) -> float:
        """Return the average of all the values in this tree.

        Return 0 if this tree is empty.

        >>> Tree(None, []).average()
        0.0
        >>> t = Tree(13, [Tree(2, []), Tree(6, [])])
        >>> t.average()
        7.0
        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t.average()
        5.5
        """
        if self.is_empty():
            return 0.0
        else:
            nodes = len(self)
            total = self.sum_values()
            return total / nodes

    def sum_values(self) -> int:
        """Return the sum of all the values in the Tree.

        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t.sum_values()
        55
        """
        if self.is_empty():
            return 0
        elif isinstance(self._root, int):
            return self._root + sum(s.sum_values() for s in self._subtrees)
        else:
            return sum(s.sum_values() for s in self._subtrees)

        # or...
        # if self.is_empty():
        #     return 0
        # else:
        #     if isinstance(self._root, int):
        #         total = self._root
        #     else:
        #         total = 0
        #     total += sum(subtree.sum_values() for subtree in self._subtrees)
        # return total

    # TODO: implement
    def to_nested_list(self) -> list:
        """Return the nested list representation of this tree.

        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t2 = Tree(1, [lt, rt])
        >>> t3 = Tree()
        >>> t4 = Tree(5)
        >>> t4.to_nested_list()
        [5]
        >>> t3.to_nested_list()
        []
        >>> lt.to_nested_list()
        [2, [4, 5]]
        >>> rt.to_nested_list()
        [3, [6, 7, 8, 9, 10]]
        >>> t.to_nested_list()
        [1, [2, [4, 5]], [3, [6, 7, 8, 9, 10]]]
        """
        pass


# TODO: Implement this function!
def to_tree(obj: Union[int, List]) -> 'Tree':
    """Return the Tree which <obj> represents.

    You may not access Tree attributes directly. This function can be
    implemented only using the Tree initializer.

    >>> print(to_tree(5))
    5
    >>> print(to_tree([]))

    >>> print(to_tree([1, 2, [3, 4], 5])

    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
