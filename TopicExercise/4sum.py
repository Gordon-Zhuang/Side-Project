class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int

        from collections import defaultdict
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        dic3 = defaultdict(int)
        dic4 = defaultdict(int)
        for i in range(len(nums1)):
            dic1[nums1[i]] += 1
        for i in range(len(nums2)):
            dic2[nums2[i]] += 1
        for i in range(len(nums3)):
            dic3[nums3[i]] += 1
        for i in range(len(nums4)):
            dic4[nums4[i]] += 1
        ans = 0
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = list(set(nums3))
        nums4 = list(set(nums4))

        for i in range(len(nums1)):
            tempi = 0-nums1[i]
            for j in range(len(nums2)):
                tempj = tempi -nums2[j]
                for k in range(len(nums3)):
                    if tempj - nums3[k] in nums4:
                        ans += dic1[nums1[i]]*dic2[nums2[j]]*dic3[nums3[k]]*dic4[tempj - nums3[k]]
        return ans
        """
        ans = 0
        from collections import defaultdict
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dic1[nums1[i] + nums2[i]] += 1
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                dic2[nums3[i] + nums4[i]] += 1
        for i in dic1:
            if 0 - i in dic2:
                ans += dic1[i] * dic2[0 - i]
        return ans

    fourSumCount(0, [1,2],[-2,-1],[-1,2],[0,2])