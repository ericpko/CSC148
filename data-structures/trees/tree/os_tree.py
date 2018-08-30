"""
treat a filesystem as a tree
"""
from os import scandir, path
from tree2 import Tree


def path_to_tree(path_name: str) -> Tree:
    """
    Return a Tree representing a filesystem starting from pathname.
    """
    return Tree((path_name, [f.name for f in scandir(path_name)]),
                [path_to_tree(path.join(path_name, f.name))
                 for f in scandir(path_name)
                 if f.is_dir()])
