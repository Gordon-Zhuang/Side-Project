<<<<<<< HEAD
def groupAnagrams(self, strs):
    dic = {}
    temp = strs.copy()
    for i in range(len(temp)):
        temp[i] = str(sorted(temp[i]))
        if temp[i] in dic:
            dic[temp[i]] += [strs[i]]
        else:
            dic[temp[i]] = [strs[i]]
    return dic
=======
def groupAnagrams(self, strs):
    dic = {}
    temp = strs.copy()
    for i in range(len(temp)):
        temp[i] = str(sorted(temp[i]))
        if temp[i] in dic:
            dic[temp[i]] += [strs[i]]
        else:
            dic[temp[i]] = [strs[i]]
    return dic
>>>>>>> f0d27928e20afecd1453ff6c377fa43eadf1f97f
print(groupAnagrams(0,["eat","tea","tan","ate","nat","bat"]))