<<<<<<< HEAD
def longestPalindrome(self, s: str) -> str:
    if len(s) < 1:
        return s
    ans = 0
    long = 1
    for i in range(1, len(s)):
        if i - long > 0 and s[i - long - 1:i + 1] == s[i - long - 1:i + 1][::-1]:
            ans, long = i - long - 1, long + 2
        if i - long >= 0 and s[i - long:i + 1] == s[i - long:i + 1][::-1]:
            ans, long = i - long, long + 1

    return s[ans:ans + long]
=======
def longestPalindrome(self, s: str) -> str:
    if len(s) < 1:
        return s
    ans = 0
    long = 1
    for i in range(1, len(s)):
        if i - long > 0 and s[i - long - 1:i + 1] == s[i - long - 1:i + 1][::-1]:
            ans, long = i - long - 1, long + 2
        if i - long >= 0 and s[i - long:i + 1] == s[i - long:i + 1][::-1]:
            ans, long = i - long, long + 1

    return s[ans:ans + long]
>>>>>>> f0d27928e20afecd1453ff6c377fa43eadf1f97f
longestPalindrome(0,"bb")