class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        from collections import defaultdict
        dic = defaultdict(int)
        for i in range(len(arr)):
            dic[arr[i]] += 1
        arr = list(set(arr))
        arr.sort()
        for i in range(len(arr)):
            temp_target = target-arr[i]
            for j in range(i,len(arr)):
                if arr[j] > temp_target/2:
                    break
                if temp_target-arr[j] in dic:
                    if i == j and arr[j] == temp_target-arr[j]:
                        if dic[arr[i]] >= 3:
                            ans += dic[arr[i]]*(dic[arr[i]]-1)*(dic[arr[i]]-2)/6
                    elif i == j:
                        if dic[arr[i]] >= 2:
                            ans += dic[arr[i]]*(dic[arr[i]]-1)/2*dic[temp_target-arr[j]]
                    elif arr[j] == temp_target-arr[j]:
                        if dic[arr[j]] >= 2:
                            ans += dic[arr[j]]*(dic[arr[j]]-1)/2*dic[arr[i]]
                    else:
                        ans += dic[arr[i]]*dic[arr[j]]*dic[temp_target-arr[j]]
        return ans

    threeSumMulti(0, [2,1,3], 6)