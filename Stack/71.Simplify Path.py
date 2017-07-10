# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name: Simplify Path.py
# Creation Time: 2017/7/10
###########################################
'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_array = path.split('/')
        stack = []
        for item in path_array:
            if item not in ['','.','..']:
                stack.append(item)
            elif item == '..' and len(stack):
                stack.pop(-1)
        if stack ==[]:
            return '/'
        else:
            return '/'+'/'.join(stack)