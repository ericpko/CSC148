"""Hash table

=== CSC148 Winter 2018 ===
University of Toronto,
Computer Science
__author__ = 'Eric Koehli'

=== Module description ===
This module contains an implmentation of a hash table.
"""
from typing import List


class HashTable:
    """
    A hash table for (key, value) 2-tuples

    === Attributes ===
    capacity - slots available
    table - contents
    collisions - number of collisions
    items - number of key/value pairs stored
    """
    capacity: int
    table: List[List[tuple]]
    collisions: int
    items: int

    def __init__(self, capacity: int=4) -> None:
        """
        Create a hash table with capacity slots
        """
        self.capacity, self.collisions, self.items = capacity, 0, 0
        # why not self.table = [[]]* capacity?
        self.table = [[] for _ in range(self.capacity)]

    def __contains__(self, key: object) -> bool:
        """ Return whether HashTable self contains key"

        >>> ht = HashTable(2)
        >>> ht["one"] = 1
        >>> "one" in ht
        True
        """
        # Find the correct bucket
        bucket = self.table[hash(key) % self.capacity]
        for item in bucket:
            if item[0] == key:
                return True
        return False

        # Version 2
        # bucket = self.table[hash(value) % self.capacity]
        # return value in [item[0] for item in bucket]

    def double(self) -> None:
        """
        Double the capacity of this hash table, and re-hash all items.
        """
        # stats before doubling
        # print("\nStats before doubling: {}".format(self.stats()))
        # temporarily save self.table
        old_table = self.table
        # reset items and collisions
        self.items, self.collisions = 0, 0
        # create double-sized table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        # insert old items into new table
        for bucket in old_table:
            for item in bucket:
                self[item[0]] = item[1]
        # stats after doubling
        # print("Stats after doubling: {}".format(self.stats()))

    def __setitem__(self, key: object, value: object) -> None:
        """
        Insert (key, value) item into HashTable self.

        >>> ht = HashTable(2)
        >>> ht.capacity == 2
        True
        >>> ht.__setitem__("one", 1)
        >>> ht["two"] = 2
        >>> ht.capacity
        4
        """
        # find the appropriate bucket
        bucket = self.table[hash(key) % self.capacity]
        # if key is there, replace value
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
        # insert item if it's not already there
        if (key, value) not in bucket:
            bucket.append((key, value))
            # update items and collisions
            self.items += 1
            if len(bucket) > 1:
                self.collisions += 1
        # if the density is high, double table
        if (self.items / self.capacity) > 0.7:
            self.double()

    def __getitem__(self, key: object) -> object:
        """
        Return value corresponding to key, or else raise Exception.

        >>> ht = HashTable(2)
        >>> ht["one"] = 1
        >>> ht["one"]
        1
        """
        # get the right bucket
        bucket = self.table[hash(key) % self.capacity]
        # get item from bucket
        for item in bucket:
            if item[0] == key:
                return item[1]
        # raise an error if key not present
        raise KeyError(f'{key} not present.')

    def stats(self) -> str:
        """
        Provide statistics.
        """
        buckets = sum([1 for b in self.table if len(b) > 0])
        max_bucket_length = max([len(b) for b in self.table])
        average = "Average bucket length: {}.\n".format(self.items / buckets)
        ideal = "Density: {}\n".format(self.items / self.capacity)
        collisions = "Collisions: {}\n".format(self.collisions)
        maximum = "Maximum bucket length: {}".format(max_bucket_length)
        return average + ideal + collisions + maximum


if __name__ == '__main__':
    import random
    from time import time
    word_list = open('words').readlines()
    random.shuffle(word_list)
    ht = HashTable(2)
    # for j in range(99171):
    #     ht[word_list[j]] = hash(word_list[j])
    # print(ht.stats())
    # print(ht.retrieve("centre"))
    # ht = HashTable(2)
    with open("inserts_results.txt", "w") as inserts:
        for i in range(99171):
            start = time()
            ht[word_list[i]] = hash(word_list[i])
            inserts.write("{}\t{}\n".format(i, time() - start))
        inserts.close()
    # random.shuffle(word_list)
    # with open("retrieves_results.txt", "w") as retrieves:
    #     for i in range(99171):
    #         start = time()
    #         x = ht[word_list[i]]
    #         retrieves.write("{}\t{}\n".format(i, time() - start))
    #     retrieves.close()
