# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Minimum Index Sum of Two Lists.py
# Creation Time: 2018/1/8
###########################################
'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
'''
import collections


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hashtable = collections.defaultdict(list)
        ans = []
        minimun_idx = len(list1) + len(list2)
        for idx, rest in enumerate(list1):
            hashtable[rest] += [idx]
        for idx, rest in enumerate(list2):
            hashtable[rest] += [idx]
        for rest in hashtable:
            if len(hashtable[rest]) == 2:
                if sum(hashtable[rest]) < minimun_idx:
                    ans = [rest]
                    minimun_idx = sum(hashtable[rest])
                elif sum(hashtable[rest]) == minimun_idx:
                    ans.append(rest)
        return ans

S = Solution()
print S.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Shogun","Burger King"])