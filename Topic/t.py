def sorting(self, s):
    array = []
    temp = ""
    ans = ""
    for i in range(len(s)):
        if s[i] == ",":
            array.append(temp)
            temp = ""
        else:
            temp += s[i]
    array.sort()
    for i in range(len(array)):
        ans += array[i]
        ans += ","
    ans = ans[:-1]

    return ans
sorting( 0,"bb,aa,lintcode,c")