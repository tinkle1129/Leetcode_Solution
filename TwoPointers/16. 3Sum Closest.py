###########################################
# Author: Tinkle
# E-mail: shutingnupt@gmail.com
# Name:  3Sum Closest.py
# Creation Time: 2017/6/24
###########################################
'''
    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        if len(nums)==3:
            return sum(nums)
        ret = nums[0]+nums[1]+nums[2]
        for i in range(1,len(nums)-1): #boundary

            start = i - 1
            end = i + 1
            while(start>=0 and end<len(nums)):
                tmpnums = nums[i] + nums[start] + nums[end]
                if(start>0 and abs(target-tmpnums)>=abs(target-(nums[i]+nums[start-1]+nums[end]))):
                    start = start-1
                elif(end<len(nums)-1 and abs(target-tmpnums)>=abs(target-(nums[i]+nums[start]+nums[end+1]))):
                    end = end+1
                else:
                    #print nums[i], nums[start], nums[end]
                    break
            #print nums[i], nums[start], nums[end]
            if abs(target-(nums[i]+nums[start]+nums[end]))<abs(target-ret):
                ret = nums[i]+nums[start]+nums[end]
            if abs(target-ret)==0:
                return ret
        return ret





S = Solution()
print S.threeSumClosest([1,1,1,0],100)
print S.threeSumClosest([1,2,4,8,16,32,64,128],82)