# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Exclusive Time of Functions.py
# Creation Time: 2018/1/2
###########################################
'''
Given the running logs of n functions that are executed in a nonpreemptive single threaded CPU, find the exclusive time of these functions.

Each function has a unique id, start from 0 to n-1. A function may be called recursively or by another function.

A log is a string has this format : function_id:start_or_end:timestamp. For example, "0:start:0" means function 0 starts from the very beginning of time 0. "0:end:0" means function 0 ends to the very end of time 0.

Exclusive time of a function is defined as the time spent within this function, the time spent by calling other functions should not be considered as this function's exclusive time. You should return the exclusive time of each function sorted by their function id.

Example 1:
Input:
n = 2
logs =
["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
Output:[3, 4]
Explanation:
Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 0 calls function 1, function 1 starts at time 2, executes 4 units of time and end at time 5.
Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time.
So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.
Note:
Input logs will be sorted by timestamp, NOT log id.
Your output should be sorted by function id, which means the 0th element of your output corresponds to the exclusive time of function 0.
Two functions won't start or end at the same time.
Functions could be called recursively, and will always end.
1 <= n <= 100

'''
import collections
class Solution(object):
    def exclusiveTime_(self, n, logs): #Line 12: MemoryError
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        start = int(logs[0].split(':')[-1])
        end = int(logs[-1].split(':')[-1])
        ret = []
        timestamp = [-1]*(end-start+1)
        id_list = [[i,-1,-1] for i in range(n)]
        for log in logs:
            log = log.split(':')
            if log[1]=='start':
                id_list[int(log[0])][1]=int(log[2])-start
            else:
                id_list[int(log[0])][2]=int(log[2])-start
        for item in sorted(id_list,key=lambda x:x[1]):
            for i in range(item[1],item[2]+1):
                timestamp[i]=item[0]
        ans =collections.Counter(timestamp)
        for i in ans:
           ret.append(ans[i])
        return ret

    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        ans = [0 for i in range(n)]
        for log in logs:
            logname, state, logtime = log.split(':')
            logname = int(logname)
            logtime = int(logtime)
            if state == 'start':
                if len(stack):
                    ans[stack[-1][0]] += logtime - stack[-1][1]
                stack.append([logname, logtime])
            else:
                lastitem = stack.pop()
                ans[lastitem[0]] += logtime - lastitem[1] + 1
                if len(stack):
                    stack[-1][1] = logtime + 1
        return ans

S = Solution()
print S.exclusiveTime(1
,["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"])