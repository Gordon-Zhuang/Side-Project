def frequencySort(self, s: str) -> str:
    from collections import defaultdict
    letter_dic = defaultdict(int)
    freq_dic = defaultdict(list)
    freq_array = []
    ans = ""
    for i in range(len(s)):
        letter_dic[s[i]] += 1
    for N, (index,value) in enumerate(letter_dic.items()):
        freq_dic[value].append(index)
        if value not in freq_array:
            freq_array.append(value)
    freq_array.sort()
    for i in range(len(freq_array)-1,-1):
        string = freq_dic[freq_array[i]]
        for j in range(len(string)):
            ans += string[j] * freq_array[i]
    return ans

frequencySort(0, "tree")