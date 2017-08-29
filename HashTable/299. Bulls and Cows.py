# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Bulls and Cows.py
# Creation Time: 2017/8/29
###########################################
'''
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

For example:

Secret number:  "1807"
Friend's guess: "7810"
Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. In the above example, your function should return "1A3B".

Please note that both secret number and friend's guess may contain duplicate digits, for example:

Secret number:  "1123"
Friend's guess: "0111"
In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".
You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
'''
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
    	hash1={}
    	hash2={}
    	bull=0
    	cows=0
    	minx=min(len(secret),len(guess))
    	for i in range(minx):
    		if secret[i]==guess[i]:
    			bull=bull+1
    		else:
    			hash1.setdefault(secret[i],0)
    			hash1[secret[i]]=hash1[secret[i]]+1
    			hash2.setdefault(guess[i],0)
    			hash2[guess[i]]=hash2[guess[i]]+1
    	for i in hash1:
    		if i in hash2:
	    		cows=cows+min(hash1[i],hash2[i])
    	ans="%d%s%d%s"%(bull,'A',cows,'B')
    	return ans