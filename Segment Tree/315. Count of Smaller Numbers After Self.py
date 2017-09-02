# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Count of Smaller Numbers After Self.py
# Creation Time: 2017/9/1
###########################################
'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
'''

# S2
class Node(object):
    def __init__(self,val):
        self.val = val
        self.small = 0
        self.left = None
        self.right = None
        self.cnt = 1
# S3
class BSTree(object):
    def __init__(self):
        self.root = None

    def insert(self,val):
        if self.root == None:
            self.root = Node(val)
            return 0
        root = self.root
        cnt = 0
        while(root):
            if val < root.val:
                root.small +=1
                if root.left is None:
                    root.left = Node(val)
                    break
                root = root.left
            elif val > root.val:
                cnt += root.small + root.cnt
                if root.right is None:
                    root.right = Node(val)
                    break
                root = root.right
            else:
                cnt += root.small
                root.cnt +=1
                break
        return cnt

class SegmentTree(object):
    def __init__(self,num):
        self.segment = [0] * (4 * num + 10)

    def query(self,node,i,j,start,end):
        if start>=i and end<=j:
            return self.segment[node]
        elif end < i or start > j:
            return 0
        else:
            mid = (start + end) / 2
            p1 = self.query(2 * node, i, j, start, mid)
            p2 = self.query(2 * node + 1, i, j, mid+1, end)
            return p1 + p2

    def update(self,node,start,end,val):
        if start == end:
            self.segment[node] +=1
        else:

            mid = (start+end)/2
            if mid>=val:
                self.update(2*node,start,mid,val)
            else:
                self.update(2*node+1,mid+1,end,val)
            self.segment[node]+=1

class Solution(object):
    def countSmaller(self,nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maparray = sorted(list(set(nums)))
        dict_ = {}
        for i in range(len(maparray)):
            dict_[maparray[i]] = i
        seg_tree = SegmentTree(len(maparray))
        ret = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            idx = len(nums)-1-i
            q = dict_[nums[idx]]
            ret[idx] = seg_tree.query(1,0,q-1,0,len(maparray)-1)
            seg_tree.update(1,0,len(maparray)-1,q)
        return ret

    def countSmaller_solution2(self,nums): # binary search tree
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        root = BSTree()
        ret = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            idx = len(nums)-1-i
            ret[idx]= root.insert(nums[idx])
        return ret
    def countSmaller_solution1(self, nums): # binary search insert
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        new_array = []
        ret = [0 for i in range(len(nums))]
        def getindex(num):
            if new_array == []:
                new_array.append(num)
                return 0
            start = 0
            end = len(new_array)
            while(start<end):
                mid = (start+end)/2
                if new_array[mid]>=num:
                    end = mid
                else:
                    start = mid+1
            new_array.insert(end,num)
            return end
        for i in range(len(nums)):
            idx = len(nums)-1-i
            ret[idx] = getindex(nums[idx])
        return ret

S = Solution()
print S.countSmaller([76,99,51,9,21,84,66,65,36,100,41])