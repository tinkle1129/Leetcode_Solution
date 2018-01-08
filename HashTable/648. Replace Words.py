# - * - coding:utf8 - * - -
###########################################
# Author: Tinkle
# E-mail: shutingnjupt@gmail.com
# Name:  Replace Words.py
# Creation Time: 2018/1/5
###########################################
'''
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Note:
The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000

'''
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        ret = []
        dict.sort(key=lambda x:len(x))
        for tokens in sentence.split():
            minroot = None
            for tok in dict:
                if tok == tokens[0:len(tok)]:
                    if minroot == None:
                        minroot = tok
                        break
            if minroot == None:
                ret+=[tokens]
            else:
                ret+=[minroot]
        return ' '.join(ret)


class TrieNode(object):
    def __init__(self):
        self.Child = dict()
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            child = node.Child.get(w)
            if child is None:
                child = TrieNode()
                node.Child[w] = child
            node = child
        node.isWord = True

    def search(self, word):
        node = self.root
        ret = ''
        for w in word:
            if node.isWord == True:
                return ret
            child = node.Child.get(w)
            if child:
                node = child
                ret += w
            else:
                return ''
        return ret if node.isWord == True else ''


class Solution1(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        ret = []
        root = Trie()
        for tok in dict:
            root.insert(tok)
        for tokens in sentence.split():
            minroot = root.search(tokens)
            if minroot == '':
                ret += [tokens]
            else:
                ret += [minroot]
        return ' '.join(ret)