def nextGreaterElement(self, nums1, nums2):
    ans = []
    for i in range(len(nums1)):
        tempans = -1
        for j in range(nums2.index(nums1[i]), len(nums2)):
            if nums2[j] > nums1[i]:
                tempans = nums2[j]
        ans.append(tempans)
    return ans
nextGreaterElement(0, [4,1,2], [1,3,4,2])
