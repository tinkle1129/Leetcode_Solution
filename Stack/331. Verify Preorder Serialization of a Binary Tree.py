# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Verify Preorder Serialization of a Binary Tree.py
# Creation Time: 2017/9/4
###########################################
'''
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false
'''


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        order = preorder.split(',')
        if order == [] or order == ['#']:
            return True
        flag = True
        stack = []
        state = []
        idx = 0
        while(idx<len(order)):
            if order[idx] == '#':
                if len(stack)==0:
                    return False
                else:
                    state[-1] +=1
                    while(len(stack) and state[-1]==2):
                        stack.pop()
                        state.pop()
                        if len(state):
                            state[-1]+=1
            else:
                if stack == []:
                    if flag:
                        stack = [order[idx]]
                        state = [0]
                        flag = False
                    else:
                        return False
                else:
                    stack.append(order[idx])
                    state.append(0)
            idx +=1
        return stack == []

S = Solution()
print S.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
print S.isValidSerialization("#,1,3")
print S.isValidSerialization("1,#")
print S.isValidSerialization("9,#,#,1")



