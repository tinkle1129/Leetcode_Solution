# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Insert Delete GetRandom O(1) - Duplicates allowed.py
# Creation Time: 2017/9/24
###########################################
import random


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.list = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.list.append(val)
        if val not in self.data:
            self.data[val] = 1
            return True
        self.data[val] += 1
        return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.data:
            return False
        self.list.remove(val)
        self.data[val] -= 1
        if self.data[val] == 0:
            self.data.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        index = random.randint(1, len(self.list))
        return self.list[index - 1]




        # Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
print obj.insert(1)
print obj.insert(1)
print obj.insert(2)
print obj.getRandom()
print obj.remove(1)
print obj.getRandom()

        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()