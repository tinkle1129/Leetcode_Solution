'''
Leetcode 461. Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.

'''
class Solution(object):
    def hammingDistance(self, x, y):
		ret=0
		ans=x ^ y
		while(ans):
			ret = ret+ans % 2
			ans = ans>>1
		return ret


S = Solution()
print S.hammingDistance(7,9)