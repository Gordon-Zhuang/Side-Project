class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        anslist = []
        ans = ""
        while i < len(s):
            temp = ""
            while i < len(s) and s[i] != " ":
                temp += s[i]
                i += 1
            anslist.append(temp)
            while i < len(s) and s[i] == " ":
                i += 1
        for i in range(len(anslist)-1,-1,-1):
            ans += anslist[i]+" "
        ans = ans[:-1]

        return ans

    reverseWords(0, "  hello world  ")