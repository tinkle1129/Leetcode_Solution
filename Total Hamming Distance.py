'''
Leetcode 477. Total Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
'''
class Solution(object):
	def totalHammingDistance(self, nums):
		'''
		:param nums: List[int]
		:return: int
		'''
		ret=0
		while(sum(nums)):
			Zero_Nums=0
			One_Nums=0
			for i in range(len(nums)):
				if nums[i]%2==0:
					Zero_Nums = Zero_Nums+1
				else:
					One_Nums = One_Nums+1
				nums[i]=nums[i]>>1
			ret = Zero_Nums*One_Nums+ret
		return ret

S = Solution()
print S.totalHammingDistance([4,2,14])