<<<<<<< HEAD
def nextPermutation(self, nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    check = 0
    index = 0
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[i]:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                index = j+1
                check = 1
                break
        if check == 1:
            break
    for i in range(index, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    print(nums)
    return nums

=======
def nextPermutation(self, nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    check = 0
    index = 0
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[i]:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                index = j+1
                check = 1
                break
        if check == 1:
            break
    for i in range(index, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    print(nums)
    return nums

>>>>>>> f0d27928e20afecd1453ff6c377fa43eadf1f97f
nextPermutation(0, [1,3,2])