def findMedianSortedArrays(self, nums1, nums2):
    len1 = len(nums1)
    len2 = len(nums2)
    halflen = (len1 + len2 + 1) // 2
    if len1 > len2:
        len1, len2, nums1, nums2 = len2, len1, nums2, nums1

    if len1 == 0:
        if len2 % 2 == 0:
            return (nums2[len(nums2) // 2] + nums2[(len(nums2) // 2) - 1]) / 2
        else:
            return nums2[len(nums2) // 2]
    elif len2 == 0:
        if len1 % 2 == 0:
            return (nums1[len(nums1) // 2] + nums1[(len(nums1) // 2) - 1]) / 2
        else:
            return nums1[len(nums1) // 2]

    maxi = len1
    mini = 0

    while (mini <= maxi):
        i = (mini + maxi) // 2
        j = halflen - i
        if i < len1 and nums2[j - 1] > nums1[i]:
            mini = i + 1
        elif i > 0 and nums2[j] < nums1[i - 1]:
            maxi = i - 1
        else:
            if i == 0:
                left = nums2[j - 1]

            else:
                left = max(nums1[i - 1], nums2[j - 1])

            if i == len1:
                right = nums2[j]
            else:
                right = min(nums1[i], nums2[j])

            if (len1 + len2) % 2 == 0:
                ans = (left + right) / 2.0
            else:
                ans = left

            return ans

findMedianSortedArrays(0, [1,2,3], [4,5,6,7])