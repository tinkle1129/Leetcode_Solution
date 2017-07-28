# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: LRU Cache.py
# Creation Time: 2017/7/28
###########################################
'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

'''


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.stack = []  # List[key]
        self.dict_ = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict_:
            self.stack.remove(key)
            self.stack.append(key)
            return self.dict_[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.get(key)!=-1:
            self.dict_[key] = value
            return
        if len(self.stack)==self.capacity:
            old_key = self.stack.pop(0)
            self.dict_.pop(old_key)
        self.dict_[key] = value
        self.stack.append(key)



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
print obj.get(2)
#param_1 = obj.get(key)
        # obj.put(key,value)