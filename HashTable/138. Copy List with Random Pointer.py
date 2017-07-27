# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Copy List with Random Pointer.py
# Creation Time: 2017/7/26
###########################################
'''
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.
'''
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if head == None:
            return head
        node_dict = {}
        node_dict[head] = RandomListNode(head.label)
        tmp = head
        while(head):
            random = head.random
            nexthd = head.next
            if random !=None:
                if random not in node_dict:
                    node_dict[random] = RandomListNode(random.label)
                node_dict[head].random = node_dict[random]
            if nexthd !=None:
                if nexthd not in node_dict:
                    node_dict[nexthd] = RandomListNode(nexthd.label)
                node_dict[head].next = node_dict[nexthd]
            head = head.next
        return node_dict[tmp]