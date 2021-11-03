def search(self, nums, target) -> int:
    ans = []
    def parting(left, right, target):
        if nums[right] == target:
            ans.append(right)
            return
        if left == right:
            return
        if target > nums[0]:
            if nums[(left + right) // 2] < nums[0] or nums[(left + right) // 2] >= target:
                parting(left, (left + right) // 2, target)
            else:
                parting((left + right) // 2, right, target)
        elif target < nums[0]:
            if nums[(left + right) // 2] < nums[0] and nums[(left + right) // 2] >= target:
                parting(left, (left + right) // 2+1, target)
            else:
                parting((left + right) // 2, right, target)

    parting(0, len(nums) - 1, target)
    if ans:
        return ans[0]
    return -1
search(0, [4,5,6,7,0,1,2], 3)