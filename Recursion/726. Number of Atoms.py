# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Number of Atoms.py
# Creation Time: 2018/3/6
###########################################
'''
Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:
Input:
formula = "H2O"
Output: "H2O"
Explanation:
The count of elements are {'H': 2, 'O': 1}.
Example 2:
Input:
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation:
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:
Input:
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation:
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
'''
import collections
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = [collections.defaultdict(int)]
        idx = 0
        while(idx<len(formula)):
            token = formula[idx]
            if token>='A' and token<='Z':
                ch = token
                idx+=1
                cnt=0
                while (idx < len(formula) and formula[idx]>='a' and formula[idx]<='z'):
                    ch+=formula[idx]
                    idx += 1
                while (idx < len(formula) and formula[idx].isdigit()):
                    cnt = cnt*10+int(formula[idx])
                    idx += 1
                if cnt:
                    stack[-1][ch]+=cnt
                else:
                    stack[-1][ch]+= 1
                idx-=1
            elif token=='(':
                stack.append(collections.defaultdict(int))
            elif token==')':
                idx +=1
                cnt = 0
                while(idx<len(formula) and formula[idx].isdigit()):
                    cnt = cnt*10+int(formula[idx])
                    idx+=1
                if cnt:
                    for key in stack[-1]:
                        stack[-1][key] = stack[-1][key]*cnt
                tstack = stack.pop()
                for key in tstack:
                    stack[-1][key]+=tstack[key]
                idx-=1
            idx+=1

        ret = ''
        for x in sorted(stack[-1].items(),key=lambda x:x[0]):
            if x[1]!=1:
                ret+=x[0]+str(x[1])
            else:
                ret+=x[0]
        return ret

S = Solution()
print S.countOfAtoms("H2O")
print S.countOfAtoms("Mg(OH)2")
print S.countOfAtoms("K4(ON(SO3)2)2")