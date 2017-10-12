# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Minimum Genetic Mutation.py
# Creation Time: 2017/10/12
###########################################
'''
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3

'''


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        def distance_1(str1,str2):
            cnt = 0
            for i,j in zip(str1,str2):
                if i!=j:
                    cnt+=1
            return cnt==1

        if start in bank:
            bank.remove(start)
        stack = [start]
        ret = 1
        visited = [True for str_ in bank]
        while(stack):
            tmp = []
            while(stack):
                item = stack.pop()
                for i in range(len(bank)):
                    if visited[i] and distance_1(item,bank[i]):
                        if bank[i]==end:
                            return ret
                        visited[i]=False
                        tmp.append(bank[i])
            stack = tmp[:]
            ret +=1
        return -1
S = Solution()
print S.minMutation('AACCGGTT','AAACGGTA',["AACCGGTA", "AACCGCTA", "AAACGGTA"])
print S.minMutation('AAAAACCC','AACCCCCC',["AAAACCCC", "AAACCCCC", "AACCCCCC"])



