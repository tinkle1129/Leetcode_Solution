###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Longest Common Prefix.py
# Creation Time: 2017/6/24
###########################################
'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        '''
        :param strs: List[str]
        :return: str
        '''
        if len(strs)==0:
            return ''
        ans = len(strs[0])
        for s in strs:
            ans = min(len(s),ans)
        ret = strs[0][0:ans]
        for s in strs:
            tmp = ret
            ret = ''
            flag = 1
            for idx in range(len(tmp)):
                if flag and tmp[idx]==s[idx]:
                    ret +=tmp[idx]
                else:
                    flag = 0
        return ret

S =Solution()
strs=['abc','abcde','abcdef','accdefg','ab']
print S.longestCommonPrefix(strs)