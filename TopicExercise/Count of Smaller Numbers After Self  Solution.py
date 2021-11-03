def countSmaller(self, nums):
    def insertarray(array, num):
        left = 0
        right = len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if mid < num:
                left = mid
            else:
                right = mid
        if right == 0:
            temp = 0
        else:
            temp = array[left]
        return array[:right] + [num] + array[right:], temp

    sortedarray = []
    ans = []
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] not in sortedarray:
            sortedarray, temp = insertarray(sortedarray, nums[i])
            ans = temp + ans
        else:
            temp = sortedarray.index(nums[i])
            if temp != 0:
                temp = sortedarray[temp - 1]
            ans = temp + ans
    return ans

countSmaller(0, [5,2,6,1])