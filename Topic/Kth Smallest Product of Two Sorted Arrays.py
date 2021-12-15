def kthSmallestProduct(self, nums1, nums2, k):
    num1_neg, num1_pos = [- i for i in nums1 if i < 0][::-1], [i for i in nums1 if i >= 0]
    num2_neg, num2_pos = [- i for i in nums2 if i < 0][::-1], [i for i in nums2 if i >= 0]
    negative_number = len(num1_neg) * len(num2_pos) + len(num1_pos) * len(num2_neg)
    if k > negative_number:
        k -= negative_number
        multi_number = 1
    else:
        k = negative_number - k + 1
        num2_neg, num2_pos = num2_pos, num2_neg
        multi_number = -1

    def check(arr1, arr2, number):
        count = 0
        for i in range(len(arr1)):
            j = 0
            if arr1[i] == 0:
                count += len(arr2)
                continue
            else:
                number /= arr1[i]
            while j < len(arr2) and arr2[j] <= number:
                count += 1
                j += 1
        return count

    left = 0
    right = 10 ** 10
    while left < right:
        mid = (left + right) // 2
        if check(num1_neg, num2_neg, mid) + check(num1_pos, num2_pos, mid) >= k:
            right = mid
        else:
            left = mid + 1
    return left * multi_number

kthSmallestProduct(0, [-9,6,10], [-7,-1,1,2,3,4,4,6,9,10], 15)