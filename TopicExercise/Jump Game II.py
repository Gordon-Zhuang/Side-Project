def jump(self, nums):
    step = 1
    index = 0
    lenth = len(nums)
    while index < lenth:
        temp = 0
        tempindex = 0
        for jump in range(nums[index] + 1):
            if nums[index + jump] + index + jump >= lenth:
                return step + 1
            if nums[index + jump] + jump > temp:
                temp = nums[index + jump] + jump
                tempindex = index + jump
        index = tempindex
        step += 1
print(jump(0,[2,3,1,1,4]))