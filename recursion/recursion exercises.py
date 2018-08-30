"""Recursion Practice

=== CSC148 Winter 2018 ===
University of Toronto,
Computer Science
__author__ = 'Eric K'

=== Module Description ===
This module contains a collection of recursive practice questions. unittests
for some of these functions can be found in the lab 5 directory. These are
great practice before implementing a Tree! I have also added more succinct
implementations using listcomp and ternary operators under the more
'intuitive' implementations. For better performance use the listcomp versions.
"""
from typing import List, Union


def gather_lists(list_: List[List[object]]) -> List[object]:
    """
    Return the concatenation of the sublists of list_.

    >>> list_ = [[1, 2], [3, 4]]
    >>> gather_lists(list_)
    [1, 2, 3, 4]
    """
    # special form of sum for "adding" lists
    return sum(list_, [])


def list_all(obj: Union[list, object]) -> list:
    """
    Return a list of all non-list elements in obj or obj's sublists, if obj
    is a list.  Otherwise, return a list containing obj.

    >>> obj = 17
    >>> list_all(obj)
    [17]
    >>> obj = [1, 2, 3, 4]
    >>> list_all(obj)
    [1, 2, 3, 4]
    >>> obj = [[1, 2, [3, 4], 5], 6]
    >>> x: int
    >>> all([x in list_all(obj) for x in [1, 2, 3, 4, 5, 6]])
    True
    >>> all ([x in [1, 2, 3, 4, 5, 6] for x in list_all(obj)])
    True
    """
    # new_list = []
    # # base case:
    # if not isinstance(obj, list):
    #     # The obj is not a list.
    #     new_list.append(obj)
    # else:
    #     # obj is a list.
    #     for item in obj:
    #         # item is either an object or another list.
    #         new_list.extend(list_all(item))
    #         # new_list += list_all(item)
    # return new_list

    # with listcomp...
    if not isinstance(obj, list):
        return [obj]
    else:
        # obj is a list.
        return sum([list_all(item) for item in obj], [])


def max_length(obj: Union[list, object]) -> int:
    """
    Return the maximum length of obj or any of its sublists, if obj is a list.
    otherwise return 0.

    >>> max_length(17)
    0
    >>> max_length([1, 2, 3, 17])
    4
    >>> max_length([[1, 2, 3, 3], 4, [4, 5]])
    4
    >>> max_length([2, [2, 2, 2], 2, 3, [3, 4], 5, 6])
    7
    >>> max_length([3, 1, [1, [2, 3, 4, 5, 6, 7], 4]])
    6
    """
    # # base case:
    # if not isinstance(obj, list):
    #     return 0
    # else:
    #     # obj is a list.
    #     length = len(obj)
    #     for item in obj:
    #         # item is either an object or another list
    #         length = max(length, max_length(item))
    # return length

    # with listcomp...
    if not isinstance(obj, list):
        return 0
    else:
        return max(len(obj), max(max_length(item) for item in obj))


def list_over(obj: Union[list, str], n: int) -> List[str]:
    """
    Return a list of strings of length greater than n in obj,
    or sublists of obj, if obj is a list.
    If obj is a string of length greater than n, return a list
    containing obj.  Otherwise return an empty list.

    >>> list_over("five", 3)
    ['five']
    >>> list_over("five", 4)
    []
    >>> list_over(["one", "two", "three", "four"], 3)
    ['three', 'four']
    """
    # new_list = []
    # # base Case:
    # if isinstance(obj, str):
    #     if len(obj) > n:
    #         new_list.append(obj)
    # else:
    #     # obj is a list.
    #     for item in obj:
    #         # item is either a string or another list.
    #         new_list.extend(list_over(item, n))
    # return new_list

    # with listcomp...
    # if isinstance(obj, str):
    #     if len(obj) > n:
    #         return [obj]
    #     else:
    #         return []
    # else:
    #     # obj is a list.
    #     return sum([list_over(item, n) for item in obj], [])

    # with listcomp and ternary...
    if isinstance(obj, str):
        return [obj] if len(obj) > n else []
    else:
        # obj is a list.
        return sum([list_over(item, n) for item in obj], [])


def list_even(obj: Union[list, int]) -> List[int]:
    """
    Return a list of all even integers in obj,
    or sublists of obj, if obj is a list.  If obj is an even
    integer, return a list containing obj.  Otherwise return
    en empty list.

    >>> list_even(3)
    []
    >>> list_even(16)
    [16]
    >>> list_even([1, 2, 3, 4, 5])
    [2, 4]
    >>> list_even([1, 2, [3, 4], 5])
    [2, 4]
    >>> list_even([1, [2, [3, 4]], 5])
    [2, 4]
    """
    # even_lst = []
    # # base base:
    # if not isinstance(obj, list):
    #     if obj % 2 == 0:
    #         even_lst.append(obj)
    # else:
    #     # obj is a list:
    #     for item in obj:
    #         # item is either an int or another list.
    #         even_lst.extend(list_even(item))
    # return even_lst

    # with listcomp...
    # if isinstance(obj, int):
    #     if obj % 2 == 0:
    #         return [obj]
    #     else:
    #         return []
    # else:
    #     # obj is 100% a list!
    #     return sum([list_even(item) for item in obj], [])

    # with listcomp and ternary...
    if isinstance(obj, int):
        return [obj] if obj % 2 == 0 else []
    else:
        return sum([list_even(item) for item in obj], [])


def count_even(obj: Union[list, int]) -> int:
    """
    Return the number of even numbers in obj or sublists of obj
    if obj is a list.  Otherwise, if obj is a number, return 1
    if it is an even number and 0 if it is an odd number.

    >>> count_even(3)
    0
    >>> count_even(16)
    1
    >>> count_even([1, 2, [3, 4], 5])
    2
    """
    # counter = 0
    # # case case:
    # if isinstance(obj, int):
    #     if obj % 2 == 0:
    #         counter += 1
    # else:
    #     # obj is a list.
    #     for item in obj:
    #         # item is either an int or another list.
    #         counter += count_even(item)
    # return counter

    # with listcomp and ternary...
    if isinstance(obj, int):
        return 1 if obj % 2 == 0 else 0
    return sum(count_even(item) for item in obj)


def count_all(obj: Union[list, object]) -> int:
    """
    Return the number of elements in obj or sublists of obj if obj is a list.
    Otherwise, if obj is a non-list return 1.

    >>> count_all(17)
    1
    >>> count_all([17, 17, 5])
    3
    >>> count_all([17, [17, 5], 3])
    4
    """
    # num_el = 0
    # # base case:
    # if not isinstance(obj, list):
    #     num_el += 1
    # else:
    #     # obj is a list.
    #     for item in obj:
    #         # item is either an object or another list.
    #         num_el += count_all(item)
    # return num_el

    # with listcomp...
    if not isinstance(obj, list):
        return 1
    else:
        return sum(count_all(item) for item in obj)


def count_above(obj: Union[list, int], n: int) -> int:
    """
    Return tally of numbers in obj, and sublists of obj, that are over n, if
    obj is a list.  Otherwise, if obj is a number over n, return 1.  Otherwise
    return 0.

    >>> count_above(17, 19)
    0
    >>> count_above(19, 17)
    1
    >>> count_above([17, 18, 19, 20], 18)
    2
    >>> count_above([17, 18, [19, 20]], 18)
    2
    """
    # num_over = 0
    # # base case:
    # if isinstance(obj, int):
    #     # we know obj is an int
    #     if obj > n:
    #         num_over += 1
    # else:
    #     # obj is a list.
    #     for item in obj:
    #         # item is either an int or another list.
    #         num_over += count_above(item, n)
    # return num_over

    # with listcomp and ternary...
    if isinstance(obj, int):
        return 1 if obj > n else 0
    return sum(count_above(item, n) for item in obj)


def depth(obj: Union[list, object]) -> int:
    """
    Return 0 if obj is a non-list, or 1 + maximum
    depth of elements of obj, a possibly nested
    list of objects.

    Assume obj has finite nesting depth

    >>> depth(3)
    0
    >>> depth([])
    1
    >>> depth([[], [[]]])
    3
    >>> depth([1, 2, 3])
    1
    >>> depth([1, [2, 3], 4])
    2
    """
    if not isinstance(obj, list):
        return 0
    elif obj == []:
        return 1
    else:
        return 1 + max([depth(x) for x in obj])


def rec_max(obj: Union[list, int]) -> int:
    """
    Return obj if it's an int, or the maximum int in obj,
    a possibly nested list of numbers.

    Assume: obj is an int or non-empty list with finite nesting depth,
    and obj doesn't contain any empty lists

    >>> rec_max([17, 21, 0])
    21
    >>> rec_max([17, [21, 24], 0])
    24
    >>> rec_max(31)
    31
    """
    if isinstance(obj, int):
        return obj
    else:
        # obj is a list.
        return max([rec_max(x) for x in obj])


def flatten(value: Union[list, object]) -> List[object]:
    """
    Flatten a list of lists to a list of depth 1

    >>> flatten([1, 2, [3, 4, [5]]])
    [1, 2, 3, 4, 5]
    """
    flat_list = []
    # base base:
    if not isinstance(value, list):
        flat_list.append(value)
    else:
        # value is a list.
        for item in value:
            # item is either an object or another list.
            flat_list += flatten(item)
    return flat_list

    # with listcomp...
    # if not isinstance(value, list):
    #     return [value]
    # else:
    #     return sum([flatten(x) for x in value], [])


def concat_strings(s: Union[str, list]) -> str:
    """
    Concatenate all the strings in possibly-nested string_list.

    >>> concat_strings("brown")
    'brown'
    >>> concat_strings(["now", "brown"])
    'nowbrown'
    >>> concat_strings(["how", ["now", "brown"], "cow"])
    'hownowbrowncow'
    """
    new_s = ''
    if isinstance(s, str):
        return s
    else:
        # s is a list.
        for word in s:
            # word is either a string or another list.
            new_s += concat_strings(word)
    return new_s

    # with listcomp...
    # if isinstance(s, str):
    #     return s
    # else:
    #     return ''.join(concat_strings(x) for x in s)
    # Note: if you want a space between words use ' '.join(...)


def concat_strings2(s: Union[str, list]) -> str:
    """
    Concatenate all the strings in possibly-nested string_list.

    >>> concat_strings2("brown")
    'brown'
    >>> concat_strings2(["now", "brown"])
    'now brown'
    >>> concat_strings2(["how", ["now", "brown"], "cow"])
    'how nowbrown cow'
    """
    if not isinstance(s, list):
        return s
    else:
        return ' '.join([concat_strings(sub) for sub in s])


def nested_count(obj: Union[object, List]) -> int:
    """Return the number of integers in obj.

    >>> nested_count(27)
    1
    >>> nested_count([4, 1, 8])
    3
    >>> nested_count([4])
    1
    >>> nested_count([])
    0
    >>> nested_count([4, [1, 2, 3], 8])
    5
    >>> nested_count([1, [2, 3], [4, 5, [6, 7], 8]])
    8
    >>> list_ = ['how', ['now', 'brown'], 'cow']
    >>> nested_count(list_)
    4
    >>> nested_count([])
    0
    """
    if not isinstance(obj, list):
        return 1
    else:
        return sum(nested_count(x) for x in obj)


def nested_contains(list_: list, value: object) -> bool:
    """
    Return whether list_, or any nested sub-list of list_ contains value.
    >>> list_ = ["how", "now", "brown", 1]
    >>> nested_contains(list_, "now")
    True
    >>> nested_contains(list_, 1)
    True
    >>> nested_contains(list_, 3)
    False
    >>> list_ = ["how", ["now", "brown"], 1]
    >>> nested_contains(list_, "now")
    True
    >>> nested_contains([], 5)
    False
    >>> nested_contains([5], 5)
    True
    """
    # if not isinstance(list_, list):
    #     return list_ == value
    # else:
    #     bools = []
    #     for item in list_:
    #         bools.extend([nested_contains(item, value)])
    #     return any(bools)

    # with listcomp... clearest version imo
    if not isinstance(list_, list):
        return list_ == value
    else:
        return any([nested_contains(item, value) for item in list_])

    # just showing off now... not as readable
    # return any([item == value if not isinstance(item, list)
    #             else nested_contains(item, value) for item in list_])


def list_level(list_: list, d: int) -> list:
    """ Return a list of all non-list elements of <list_> that are at depth
    d.

    >>> list_level([1, [2, [3]]], 2)
    [2]
    >>> list_level([1, [2, 3, 4, 5, 6, [3, 4, 5]]], 2)
    [2, 3, 4, 5, 6]
    >>> list_level([1, [2, 3, 4, 5, 6, [3, 4, 5]]], 3)
    [3, 4, 5]
    >>> list_level([1, [2, [3]]], 0)
    []
    """
    # version 1
    # if not isinstance(list_, list):
    #     return [list_] if d == 0 else []
    # else:
    #     return sum([list_level(s, d - 1) for s in list_], [])

    # version 1b... clearest
    if not isinstance(list_, list):
        if d == 0:
            return [list_]
        else:
            return []
    else:
        return sum([list_level(s, d - 1) for s in list_], [])

    # version 2... why doesn't this one work?
    # if d == 0:
    #     return list_ if isinstance(list_, list) else [list_]
    # elif not isinstance(list_, list):
    #     return []
    # else:
    #     return sum([list_level(s, d - 1) for s in list_], [])

    # version 3
    # if d <= 0:
    #     return []
    # elif d == 1:
    #     return sum([[x] if not isinstance(x, list)
    #                 else [] for x in list_], [])
    # else:
    #     return sum([list_level(i, d - 1) if isinstance(i, list) else []
    #                 for i in list_], [])


def list_levels(list_: list) -> List[list]:
    """Return a list containing a lists of all elements at each level.

    >>> list_levels([1, [2, 3, [4, 5, [6]]]])
    [[1], [2, 3], [4, 5], [6]]
    """
    # version 1
    return [list_level(list_, d) for d in range(1, depth(list_) + 1)]

    # version 2.. intuitive!
    # max_depth = depth(list_)
    # level = 1
    # levels = []
    # while level <= max_depth:
    #     levels.append(list_level(list_, level))
    #     level += 1
    # return levels


def depth_items(list_: List, d: int) -> int:
    """
    Return the number of elements of <list_> that are
    at depth <d>.

    Precondition: Cannot have depth of 0 (i.e. d = 0)

    >>> depth_items([1, [2, [3]]], 2)
    2
    >>> depth_items([1, [2, 3, 4, 5, 6, [3, 4, 5]]], 2)
    6
    >>> depth_items([1, [2, 3, 4, 5, 6, [3, 4, 5]]], 3)
    3
    >>> depth_items([1, [2, [3]]], 1)
    2
    >>> list_ = [0, 1]
    >>> depth_items(list_, 1)
    2
    >>> list_ = [[0, 1], 2, [3, [[], 4]]]
    >>> depth_items(list_, 2)
    4
    >>> # 4 elements: 0, 1, 3, [[] , 4]
    """
    if d == 0:
        return 1
    elif not isinstance(list_, list):
        return 0
    else:
        return sum(depth_items(s, d - 1) for s in list_)

    # Solution to match below:
    # if d <= 0:
    #     return 0
    # elif d == 1:
    #     return 1
    # elif not isinstance(list_, list):
    #     return 0
    # else:
    #     return sum(depth_items(s, d - 1) for s in list_)


def width(list_: List, max_depth: int) -> int:
    """ Return the maximum number of items that occur at the same depth
    in list_ or its sub-lists combined. These could be list or non-list
    items. Elements may be lists or non-lists.
    Qparam list [list I object] list_: a possibly nested list
    Qparam max_depth int: maximum depth of list_
    Qrtype: int

    >>> list_ = [0, 1]
    >>> width(list_, 1)
    2
    >>> list_ = [[0, 1], 2, [3, [[], 4]]]
    >>> width(list_, 4)
    4
    >>> # 4 elements: 0, 1, 3, [[] , 4]
    """
    depth = 0
    max_items = 0

    while depth <= max_depth:
        num_items = depth_items(list_, depth)
        if num_items > max_items:
            max_items = num_items
        depth += 1

    return max_items

    # Solution has to match solution above
    # depth = 0
    # max_items = depth_items(list_, depth)
    # while depth <= max_depth:
    #     depth += 1
    #     items = depth_items(list_, depth)
    #     if items > max_items:
    #         max_items = items
    # return max_items


# TODO: implement
# def list_level2(list_: list, d: int) -> list:
#     """
#     Return a list of all elements of <list_> that are at depth d.
#
#     >>> list_level2([1, [2, [3]]], 2)
#     2
#     >>> list_level2([1, [2, 3, 4, 5, 6, [3, 4, 5]]], 2)
#     6
#     >>> list_level2([1, [2, 3, 4, 5, 6, [3, 4, 5]]], 3)
#     3
#     >>> list_level2([1, [2, [3]]], 1)
#     2
#     >>> list_ = [0, 1]
#     >>> list_level2(list_, 1)
#     2
#     >>> list_ = [[0, 1], 2, [3, [[], 4]]]
#     >>> list_level2(list_, 2)
#     [0, 1, 3, [[] , 4]]
#     """
#     pass


def concatenate_flat(list_: List) -> str:
    """
    Return the concatenation, from left to right, of strings contained
    in flat (depth 1) sublists contained in list., but
    no other strings
    Assume all non-list elements of list, or its
    nested sub-lists are strings

    >>> concatenate_flat(['five', [['four', 'by'], 'three'], ['two']])
    'fourbytwo'
    """
    return ''.join(no_sublists(list_))

    # lst = no_sublists(list_)
    # return ''.join([lst])


def no_sublists(list_: List) -> list:
    """
    Helper for above

    Return a single list of elements of all the sublists of <list_>
    that have no sublists themselves.
    """
    if not isinstance(list_, list):
        return []
    elif all(type(x) != list for x in list_):
        return list_
    else:
        return sum([no_sublists(s) for s in list_], [])

    # Solution 2
    # if not isinstance(list_, list):
    #     return []
    # else:
    #     # We know list_ is a list
    #     if all(type(x) != list for x in list_):
    #         return list_
    #     else:
    #         return sum([no_sublists(s) for s in list_], [])


def concat_level(list_: List, d: int) -> str:
    """
    helper for concatenate_flat

    """
    if not isinstance(list_, list):
        if d == 0:
            return str(list_)
        else:
            return ''
    else:
        return ''.join([concat_level(s, d - 1) for s in list_])


##############################################################################
# More practice with nested lists: CSC 148 Fall 2017
##############################################################################
def duplicate(nested_list: Union[list, int]) -> list:
    """Return a new nested list with all numbers in <nested_list> duplicated.

    Each integer in <nested_list> should appear twice *consecutively* in the
    output nested list. The nesting structure is the same as the input,
    only with some new numbers added. See doctest examples for details.

    If <nested_list> is an int, return a list containing two copies of it.

    >>> duplicate(1)
    [1, 1]
    >>> duplicate([])
    []
    >>> duplicate([1, 2])
    [1, 1, 2, 2]
    >>> duplicate([1, [2, 3]])  # NOT [1, 1, [2, 2, 3, 3], [2, 2, 3, 3]]
    [1, 1, [2, 2, 3, 3]]
    """
    new_list = []
    # base case:
    if isinstance(nested_list, int):
        new_list.extend([nested_list, nested_list])
    else:
        # nested_list is a list.
        for item in nested_list:
            # item is either an int or a list.
            if isinstance(item, int):
                new_list.extend(duplicate(item))
            else:
                # item is another list.
                new_list.append(duplicate(item))
    return new_list

    # try it with listcomp and ternary operators.. challenging!


def add_one(nested_list: Union[list, int]) -> None:
    """Add one to every number stored in <nested_list>.

    Do nothing if <nested_list> is an int.
    If <nested_list> is a list, *mutate* it to change the numbers stored.
    (Don't return anything in either case.)

    >>> lst0 = 1
    >>> add_one(lst0)
    >>> lst0
    1
    >>> lst1 = []
    >>> add_one(lst1)
    >>> lst1
    []
    >>> lst2 = [1, [2, 3], [[[5]]]]
    >>> add_one(lst2)
    >>> lst2
    [2, [3, 4], [[[6]]]]
    """
    # base base:
    if isinstance(nested_list, int):
        pass
    else:
        # nested_list is a list.
        for i in range(len(nested_list)):
            # nested_list[i] is either an int or another list.
            if isinstance(nested_list[i], int):
                nested_list[i] += 1
            else:
                # nested_list[i] is a list.
                add_one(nested_list[i])


def nested_max(obj: Union[int, List]) -> int:
    """Return the maximum item stored in nested list <obj>.

    You may assume all the items are positive, and calling
    nested_max on an empty list returns 0.

    >>> nested_max(17)
    17
    >>> nested_max([1, 2, [1, 2, [3], 4, 5], 4])
    5
    >>> nested_max([])
    0
    >>> nested_max([1, 2, [], [5, [7]]])
    7
    """
    # version 1
    if isinstance(obj, int):
        return obj
    elif obj == []:
        return 0
    else:
        return max(nested_max(i) for i in obj)

    # version 2
    # max_val = 0
    # if isinstance(obj, int):
    #     if obj > max_val:
    #         max_val = obj
    # else:
    #     # obj is a list
    #     for item in obj:
    #         # item is either an int or another list
    #         max_val = max(max_val, nested_max(item))
    # return max_val


def max_length_v2(obj: Union[int, List]) -> int:
    """Return the maximum length of any list in nested list <obj>.

    The *maximum length* of a nested list is defined as:
    1. 0, if <obj> is a number.
    2. The maximum of len(obj) and the lengths of the nested lists contained
       in <obj>, if <obj> is a list.

    >>> max_length_v2(17)
    0
    >>> max_length_v2([1, 2, 3, 17])
    4
    >>> max_length_v2([[1, 2, 3, 3], 4, [4, 5]])
    4
    >>> max_length_v2([2, [2, 2, 2], 2, 3, [3, 4], 5, 6])
    7
    >>> max_length_v2([3, 1, [1, [2, 3, 4, 5, 6, 7], 4]])
    6
    """
    if isinstance(obj, int):
        return 0
    elif obj == []:
        return 0
    else:
        # obj is a list.
        return max(len(obj), max(max_length_v2(x) for x in obj))

    # version 2.. intuitive
    # if isinstance(obj, int):
    #     return 0
    # else:
    #     # obj is a list.
    #     len_lst = len(obj)
    #     for item in obj:
    #         # item is either an int or another list.
    #         len_lst = max(len_lst, max_length_v2(item))
    # return len_lst


def equal(obj1: Union[int, List], obj2: Union[int, List]) -> bool:
    """Return whether two nested lists are equal, i.e., have the same value.

    Note: order matters.

    >>> equal(17, [1, 2, 3])
    False
    >>> equal([1, 2, [1, 2], 4], [1, 2, [1, 2], 4])
    True
    >>> equal([1, 2, [1, 2], 4], [4, 2, [2, 1], 3])
    False
    >>> equal([1, 2, [2, 2], 4], [1, 2, [1, 2], 4])
    False
    """
    # Trick question
    return obj1 == obj2


# ---------- Other examples (from lecture_code_2017.py
# Notice that the only difference between this function and nested_sum
# is the base case.
def nested_sum(obj: Union[int, List]) -> int:
    """Return the sum of the numbers in a nested list.

    Note that a obj is one of two things:
      1. a number
      2. a list of (less deep) nested lists


    >>> nested_sum([1, [2], [3, 4], [[5, 6], 7]])
    28
    >>> nested_sum([[1, [2]], [[[3]]], 4, [[5, 6], [[[7]]]]])
    28
    """
    if isinstance(obj, int):
        return obj
    else:
        return sum(nested_sum(i) for i in obj)


def count(obj: Union[int, List]) -> int:
    """Return the number of integers in obj.

    >>> count(27)
    1
    >>> count([4, 1, 8])
    3
    >>> count([4])
    1
    >>> count([])
    0
    >>> count([4, [1, 2, 3], 8])
    5
    >>> count([1, [2, 3], [4, 5, [6, 7], 8]])
    8
    """
    if isinstance(obj, int):
        return 1
    else:
        return sum(count(i) for i in obj)

    # if isinstance(obj, int):
    #     return 1
    # else:
    #     s = 0
    #     for lst_i in obj:
    #         s += count(lst_i)
    #     return s


# For this function, the base case is more complicated.
def occurrences(obj: Union[int, List], value: int) -> int:
    """Return the number of occurrences of value in obj.

    >>> occurrences([[[4, 5], [5]], [3, 5, [[20]]], 3], 5)
    3
    """
    if isinstance(obj, int):
        return 1 if obj == value else 0
    else:
        return sum(occurrences(x, value) for x in obj)

    # if isinstance(obj, int):
    #     if obj == value:
    #         return 1
    #     else:
    #         return 0
    # else:
    #     s = 0
    #     for lst_i in obj:
    #         s += occurrences(lst_i, value)
    #     return s


# This function has analogous structure in the base case.
# Notice that append won't yield the right structure; we need to use extend.
def negatives(obj: Union[int, List]) -> List[int]:
    """Return a list of the negative numbers in obj.

    >>> negatives([1, [2, 3], 4])
    []
    >>> negatives([1, [-2, 3], -4])
    [-2, -4]
    """
    # v1
    if isinstance(obj, int):
        return [obj] if obj < 0 else []
    else:
        return sum([negatives(i) for i in obj], [])

    # v2
    # if isinstance(obj, int):
    #     if obj < 0:
    #         return [obj]
    #     else:
    #         return []
    # else:
    #     return sum([negatives(i) for i in obj], [])

    # v3
    # negs = []
    # if isinstance(obj, int):
    #     negs.append(obj)
    # else:
    #     # obj is a list.
    #     for item in obj:
    #         # item is either an int or another list.
    #         negs += negatives(item)
    # return negs

    # v4
    # if isinstance(obj, int):
    #     if obj < 0:
    #         return [obj]
    #     else:
    #         return []
    # else:
    #     answer = []
    #     for lst_i in obj:
    #         # lst_i might be a nested list
    #         answer.extend(negatives(lst_i))
    #     return answer


def replaced(obj: Union[int, List], old: int, new: int) -> Union[int, List]:
    """Return a new nested list that is the same as obj, but with all
    occurrences of old replaced by new.

    >>> replaced([[[4, 5], [5]], [3, 5, [[20]]], 3], 5, 555)
    [[[4, 555], [555]], [3, 555, [[20]]], 3]
    >>> replaced(24, 24, 15)
    15
    >>> replaced(36, 15, 74)
    36
    """
    if isinstance(obj, int):
        if obj == old:
            return new
        else:
            return obj
    else:
        return [replaced(i, old, new) for i in obj]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
