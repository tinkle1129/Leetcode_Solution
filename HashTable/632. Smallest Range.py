import collections
class Solution(object):
    def smallestRange_(self, nums): #TLE
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        ret = None
        flag = True
        while flag:
            cur = [item[0] for item in nums]
            maxV, minV = max(cur), min(cur)
            if ret == None or maxV - minV < ret[1] - ret[0]:
                ret = [minV, maxV]
            pos = cur.index(min(cur))
            if len(nums[pos])>1:
                nums[pos].pop(0)
            else:
                flag = False
        return ret

    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        dmap = collections.defaultdict(set)
        cover = collections.defaultdict(set)
        nsize = len(nums)

        for idx, nlist in enumerate(nums):
            for num in nlist:
                dmap[num].add(idx)
        snum = sorted(set(n for nlist in nums for n in nlist))
        ssize = len(snum)

        start = end = 0
        ans = [snum[0], snum[-1]]
        gap = 0x7FFFFFFF
        while start < ssize and end < ssize:
            while end < ssize and len(cover) < nsize:
                for idx in dmap[snum[end]]:
                    cover[idx].add(snum[end])
                end += 1
            while start < ssize and len(cover) == nsize:
                if len(cover) == nsize and snum[end - 1] - snum[start] < gap:
                    gap = snum[end - 1] - snum[start]
                    ans = [snum[start], snum[end - 1]]
                for idx in dmap[snum[start]]:
                    cover[idx].remove(snum[start])
                    if not cover[idx]: del cover[idx]
                start += 1
        return ans


S = Solution()
print S.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])

