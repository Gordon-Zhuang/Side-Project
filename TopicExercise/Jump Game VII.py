<<<<<<< HEAD
"""
def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
    d = [True]
    checkindex = 0
    for i in range(2, len(s)):
        if i >= minJump:
            checkindex += d[i - minJump]
        if i > maxJump:
            checkindex -= d[i - maxJump - 1]
        d.append(checkindex > 0 and s[i] == "0")
    return d[-1]
"""


def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
    used = set()
    que = [0]
    now = 0
    lastJump = 0
    if s[-1] != "0":
        return False
    while que:
        now = que.pop(0)
        for i in range(max(now + minJump, lastJump), max(now + maxJump + 1, len(s))):
            if i == len(s) - 1 and s[i] == "0":
                return True
            if s[i] == "0" and i not in used:
                used.add(i)
                que.append(i)
        lastJump = now + maxJump + 1
    return False
=======
"""
def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
    d = [True]
    checkindex = 0
    for i in range(2, len(s)):
        if i >= minJump:
            checkindex += d[i - minJump]
        if i > maxJump:
            checkindex -= d[i - maxJump - 1]
        d.append(checkindex > 0 and s[i] == "0")
    return d[-1]
"""


def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
    used = set()
    que = [0]
    now = 0
    lastJump = 0
    if s[-1] != "0":
        return False
    while que:
        now = que.pop(0)
        for i in range(max(now + minJump, lastJump), max(now + maxJump + 1, len(s))):
            if i == len(s) - 1 and s[i] == "0":
                return True
            if s[i] == "0" and i not in used:
                used.add(i)
                que.append(i)
        lastJump = now + maxJump + 1
    return False
>>>>>>> f0d27928e20afecd1453ff6c377fa43eadf1f97f
canReach(0,"01101110",2,3)