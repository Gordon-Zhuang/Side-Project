def permute(self, nums):
    nums = sorted(nums)
    ans = []

    def choice(left_nums, nowans):
        if not left_nums:
            nonlocal ans
            ans.append(nowans)
            return
        for i in range(len(left_nums)):
            if i < 1 or left_nums[i] != left_nums[i - 1]:
                choice(left_nums[:i] + left_nums[i + 1], nowans.append(left_nums[i]))

    choice(nums, [])
    return ans

permute(0, [1,2,3])