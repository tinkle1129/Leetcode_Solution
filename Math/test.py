import sys
class Solution(object):
    def mininumChange(self,nums1,nums2):
        if nums1 == nums2: return 0
        s1 = ''
        s2 = ''
        size = len(nums1)
        for i in range(size):
            if nums1[i]!=nums2[i]:
                s1+=nums1[i]
                s2+=nums2[i]
        