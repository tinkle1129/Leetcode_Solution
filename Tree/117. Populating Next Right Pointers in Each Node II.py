# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Populating Next Right Pointers in Each Node II.py
# Creation Time: 2017/7/20
###########################################
'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

'''
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            if root.left and root.right:
                root.left.next = root.right
                tmp = root.next
                while tmp:
                    if tmp.left:
                        root.right.next = tmp.left
                        break
                    if tmp.right:
                        root.right.next = tmp.right
                        break
                    tmp = tmp.next
            elif root.left:
                tmp = root.next
                while tmp:
                    if tmp.left:
                        root.left.next = tmp.left
                        break
                    if tmp.right:
                        root.left.next = tmp.right
                        break
                    tmp = tmp.next
            elif root.right:
                tmp = root.next
                while tmp:
                    if tmp.left:
                        root.right.next = tmp.left
                        break
                    if tmp.right:
                        root.right.next = tmp.right
                        break
                    tmp = tmp.next
            self.connect(root.right)
            self.connect(root.left)





