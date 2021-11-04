<<<<<<< HEAD
def searchRange(self, nums, target: int):
    ans = [len(nums), -1]

    def parting(left, right, target):
        pivid = (left + right) // 2
        if nums[pivid] == target:
            ans[0] = min(ans[0], pivid)
            ans[1] = max(ans[1], pivid)
            if left == right:
                return
            parting(pivid + 1, right, target)
            parting(left, pivid, target)
        elif left == right:
            return
        elif nums[pivid] < target:
            parting(pivid + 1, right, target)
        elif nums[pivid] > target:
            parting(left, pivid, target)

    parting(0, len(nums) - 1, target)
    return ans
=======
def searchRange(self, nums, target: int):
    ans = [len(nums), -1]

    def parting(left, right, target):
        pivid = (left + right) // 2
        if nums[pivid] == target:
            ans[0] = min(ans[0], pivid)
            ans[1] = max(ans[1], pivid)
            if left == right:
                return
            parting(pivid + 1, right, target)
            parting(left, pivid, target)
        elif left == right:
            return
        elif nums[pivid] < target:
            parting(pivid + 1, right, target)
        elif nums[pivid] > target:
            parting(left, pivid, target)

    parting(0, len(nums) - 1, target)
    return ans
>>>>>>> f0d27928e20afecd1453ff6c377fa43eadf1f97f
searchRange(0, [5,7,7,8,8,10], 8)