###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Implement strStr().py
# Creation Time: 2017/6/30
###########################################
'''
Implement strStr().
Returns the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        haystack = '#'+haystack
        n = len(haystack)
        needle = '#'+needle
        m = len(needle)
        pos = self.compute_prefix_func(needle)
        q = 0
        for i in range(1,n):
            while(q>0 and needle[q+1]!=haystack[i]):
                q = pos[q]
            if needle[q+1] == haystack[i]:
                q = q+1
            if q == m-1:
                return i-(m-1)
        if q == m - 1:
            return n - m
        return -1
    def compute_prefix_func(self,pattern):
        '''
        :param pattern: str
        :return: list[int]
        '''
        newpatter = pattern
        length = len(newpatter)
        pos = [0 for i in range(length)]
        k =0
        for q in range(2,length):
            while(k>0 and newpatter[k+1]!=newpatter[q]):
                k = pos[k]
            if newpatter[k+1]==newpatter[q]:
                k = k+1
            pos[q] = k
        return pos



S = Solution()
#print S.compute_prefix_func(pattern='#ababaca')
#print S.strStr('ababaca','baca')
print S.strStr_('a','')

