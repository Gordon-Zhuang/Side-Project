def isMatch(self, s, p):
    index = 0
    while index + 3 < len(p):
        if p[index + 1] == "*" and p[index:index + 2] == p[index + 2:index + 4]:
            p = p[:index + 2] + p[index + 4:]
            index += 1
        index += 1
    checktable = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
    checktable[0][0] = True
    for i in range(2, len(p) + 1):
        checktable[i][0] = checktable[i - 2][0] and p[i - 1] == '*'
    for index_p in range(1, len(p) + 1):
        for index_s in range(1, len(s) + 1):
            if p[index_p - 1] != "*":
                if checktable[index_p - 1][index_s - 1] and (p[index_p - 1] == s[index_s - 1] or p[index_p - 1] == "."):
                    checktable[index_p][index_s] = True
            else:
                if checktable[index_p - 2][index_s] or checktable[index_p - 1][index_s]:
                    checktable[index_p][index_s] = True
                if checktable[index_p][index_s - 1] and (p[index_p - 2] == s[index_s - 1] or p[index_p - 2] == "."):
                    checktable[index_p][index_s] = True
    return checktable[-1][-1]
isMatch(0, "mississippi", "mis*is*p*.")