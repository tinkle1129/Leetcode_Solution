# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Find Smallest Letter Greater Than Target.py
# Creation Time: 2018/4/22
###########################################
'''
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.

'''
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        start = 0
        end = len(letters)-1
        while(start<=end):
            mid = (start+end)/2
            if letters[mid]<target:
                start = mid+1
            elif letters[mid]==target:
                while(mid<len(letters) and letters[mid]==target):
                    mid+=1
                if mid == len(letters):
                    return letters[0]
                return letters[mid]
            else:
                end = mid-1
        return letters[start] if start<len(letters) else letters[0]
    
S = Solution()
print S.nextGreatestLetter(['c','f','j'],'a')