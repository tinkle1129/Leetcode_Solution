# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  H-Index II.py
# Creation Time: 2017/8/26
###########################################
'''
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
'''


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations == []:
            return 0
        start = 0
        end = len(citations)-1
        flag = 1
        while(flag):
            mid = (start+end)/2
            if mid == start:
                flag = 0
            else:
                if len(citations)-mid>=citations[mid]:
                    start = mid
                else:
                    end = mid
        left = min(len(citations)-start,citations[start])
        right = min(len(citations)-end,citations[end])
        return max(left,right)

S = Solution()
print S.hIndex([0, 1])
print S.hIndex([0, 1, 3, 5, 6])
print S.hIndex([0,4,5,5])
print S.hIndex([0,1,2,3])
