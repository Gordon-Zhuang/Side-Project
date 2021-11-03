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
print(groupAnagrams(0,["eat","tea","tan","ate","nat","bat"]))