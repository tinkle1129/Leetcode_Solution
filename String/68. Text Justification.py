# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  Text Justification.py
# Creation Time: 2017/7/10
###########################################
'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

'''
class Solution(object):
    def modify(self,tmpwords,maxWidth):
        """
        :type tmpwords:List[str] eg:['This','is','an']
        :type maxWidth: int
        """
        word_count=len(tmpwords)
        space_count=max(1,word_count-1)
        character_num=sum([len(i) for i in tmpwords])
        base_space=(maxWidth-character_num)/space_count
        extra_space=(maxWidth-character_num)%space_count
        ret=''
        for i in range(space_count):
            ret=ret+tmpwords[i]+''.join([' ']*base_space)
            if i<extra_space:
                ret=ret+' '
        if word_count>1:
            ret=ret+tmpwords[-1]
        return ret
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result=[]
        tmp=[]
        flag=0
        for i in words:
            if flag+len(i)<=maxWidth:
                tmp.append(i)
                flag=flag+len(i)+1
            else:
                if len(tmp):
                    result.append(self.modify(tmp,maxWidth))
                tmp=[i]
                flag=len(i)+1
        ans=''
        for i in tmp[0:len(tmp)-1]:
            ans=ans+i+' '
        if len(tmp):
            ans=ans+tmp[-1]
        ans=ans+''.join([' ']*(maxWidth-len(ans)))
        result.append(ans)
        return result