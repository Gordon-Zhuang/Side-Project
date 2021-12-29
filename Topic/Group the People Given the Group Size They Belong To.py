def groupThePeople(groupSizes):
    from collections import defaultdict
    dic = defaultdict(list)
    for i in range(len(groupSizes)):
        dic[groupSizes[i]].append(i)
    key = sorted(dic.keys())
    sorted_key = {}
    for i in key:
        sorted_key[i] = dic[i]
    ans = []
    for i in sorted_key:
        while sorted_key[i]:
            ans.append([])
            for j in range(i):
                ans[-1].append(sorted_key[i].pop(0))
    return ans

groupThePeople([3,3,3,3,3,1,3])