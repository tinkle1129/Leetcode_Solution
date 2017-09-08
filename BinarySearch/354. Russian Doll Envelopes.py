# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Russian Doll Envelopes.py
# Creation Time: 2017/9/8
###########################################
'''
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        nums = sorted(envelopes,cmp = lambda x,y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        dp = []
        cnt = 0
        for i in range(len(nums)):
            begin,end = 0,cnt-1
            while(begin<=end):
                mid = (begin+end)/2
                if dp[mid][1] < nums[i][1]:
                    begin = mid+1
                else:
                    end = mid - 1
            if begin<cnt:
                dp[begin] = nums[i]
            else:
                dp.append(nums[i])
                cnt +=1
        return cnt

S = Solution()
print S.maxEnvelopes([[5,4],[6,4],[5,3],[4,2],[3,1],[6,7],[2,3]])