###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  4Sum.py
# Creation Time: 2017/6/25
###########################################
'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution(object):
    def fourSum(self,nums,target):
        '''
        :param nums: list[int]
        :param target: int
        :return: list[list[int]]
        '''
        ret = []
        nums.sort()
        print nums
        if len(nums)<4:
            return ret
        idx = 0
        while(idx+3<len(nums)):
            if (sum(nums[idx:idx+4])<=target and (nums[idx]+nums[-1]+nums[-2]+nums[-3])>=target):
                if idx>0 and nums[idx]==nums[idx-1]:
                    pass
                else:
                    #print idx
                    idj = idx+1
                    while(idj+2<len(nums)):
                        while(idj+2<len(nums) and (nums[idx]+nums[idj]+nums[-1]+nums[-2]<target)):
                            idj +=1
                        if idj+2<len(nums):
                            #print idx,idj
                            idk = idj+1
                            idm = len(nums)-1
                            while(idk<idm):
                                if nums[idx]+nums[idj]+nums[idk]+nums[idm]<target:
                                    idk +=1
                                elif nums[idx]+nums[idj]+nums[idk]+nums[idm]>target:
                                    idm -=1
                                else:
                                    ret.append([nums[idx],nums[idj],nums[idk],nums[idm]])
                                    idk +=1;idm-=1
                                    while(idk<idm and nums[idk]==nums[idk-1]):
                                        idk +=1
                                    while (idk < idm and nums[idm] == nums[idm + 1]):
                                        idm -= 1
                        idj+=1
                        while(idj<len(nums) and nums[idj]==nums[idj-1]):
                            idj+=1
            idx +=1
        return ret
S = Solution()
print S.fourSum([1, 0, -1, 0, -2, 2],0)
print S.fourSum([1,1,1,1,1,1,1,1,4],4)
print S.fourSum([0,4,-5,2,-2,4,2,-1,4],12)
