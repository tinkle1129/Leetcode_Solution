# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: All O`one Data Structure.py
# Creation Time: 2017/10/11
###########################################
'''
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.


'''
import collections


class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(int)

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        self.dic[key] += 1

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.dic:
            if self.dic[key] == 1:
                self.dic.pop(key)
            else:
                self.dic[key] -= 1

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if len(self.dic.keys()):
            return sorted(self.dic.items(), key=lambda x: x[1])[-1][0]
        return ''

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if len(self.dic.keys()):
            return sorted(self.dic.items(), key=lambda x: x[1])[0][0]
        return ''


        # Your AllOne object will be instantiated and called as such:
        # obj = AllOne()
        # obj.inc(key)
        # obj.dec(key)
        # param_3 = obj.getMaxKey()
        # param_4 = obj.getMinKey()