# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Serialize and Deserialize Binary Tree.py
# Creation Time: 2017/8/29
###########################################
'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return '[]'
        ret = [root]
        idx = 0
        while(idx<len(ret)):
            if ret[idx]!='null':
                if ret[idx].left or ret[idx].right:
                    ret += ['null' for i in range(idx+2)]
                if ret[idx].left:
                    ret[2*idx+1] = ret[idx].left
                if ret[idx].right:
                    ret[2*idx+2] = ret[idx].right
            idx+=1
        for i in range(len(ret)):
            if ret[i]!='null':
                ret[i] = str(ret[i].val)
        return '['+','.join(ret)+']'


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.strip('[').strip(']')
        if data == '':
            return None
        else:
            data = data.split(',')
        for i in range(len(data)):
            if data[i]!='null':
                data[i] = TreeNode(int(data[i]))
        for i in range(len(data)):
            idx = len(data)-1-i
            if data[idx]!='null' and idx!=0:
                if idx%2 == 0:
                    data[(idx-2)/2].right = data[idx]
                else:
                    data[(idx-1)/2].left = data[idx]
        return data[0]
'''
class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()
'''

        # Your Codec object will be instantiated and called as such:
codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
#root.right.right.right = TreeNode(8)
ans = codec.deserialize(codec.serialize(root))
print codec.serialize(ans)
#root = None
#rint codec.serialize(codec.deserialize(codec.serialize(root)))
