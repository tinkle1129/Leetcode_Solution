# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name: Employee Importance.py
# Creation Time: 2018/4/7
###########################################
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emp = dict()
        visited = dict()
        for employee in employees:
            emp[employee.id] = employee
        def dfs(idx):
            if idx in visited:
                return 0
            visited[idx] = True
            ret=emp[idx].importance
            for sub in emp[idx].subordinates:
                ret+=dfs(sub)
            return ret
        return dfs(id)