def isMatch(self, s: str, p: str) -> bool:
    index_p = 0
    index_s = 0
    next_p = -1
    next_s = -1
    while index_s < len(s):
        if index_p < len(p):
            if p[index_p] in ["?", s[index_s]]:
                index_p += 1
                index_s += 1
            elif p[index_p] == "*":
                index_p += 1
                next_p = index_p
                next_s = index_s
        elif next_p == -1:
            return False
        else:
            next_s += 1
            index_p = next_p
            index_s = next_s
    return all(p[i] == "*" for i in range(index_p, len(p)))
isMatch(0,"abcde", "*a*e")