def longestValidParentheses(self, s: str) -> int:
    tempans = 0
    numarr = [0]
    ans = 0
    if len(s) < 1:
        return ans
    head = [s[0]]
    for i in range(1, len(s)):
        if head:
            temp = head.pop()
            if temp == "(" and s[i] == ")":
                tempans += (2 + numarr.pop())
            else:
                head.append(temp)
                head.append(s[i])
                numarr.append(tempans)
                ans = max(tempans, ans)
                tempans = 0
        else:
            head.append(s[i])
            numarr.append(i)
            ans = max(tempans, ans)
            tempans = 0
    ans = max(tempans, ans)

    return ans
longestValidParentheses(0, "())")