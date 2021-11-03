def convert(self, s, numRows):
    num = numRows - 1
    ans = ""
    for row in range(numRows):
        index = row
        ans += s[index]
        while index < len(s):
            temp = (num - row) * 2

            if temp > 0:
                index += temp
                if index < len(s):
                    ans += s[index]
            temp = (row - 0 ) * 2
            if temp > 0:
                index += temp
                if index < len(s):
                    ans += s[index]

    return ans

convert(0,"PAYPALISHIRING",4)
