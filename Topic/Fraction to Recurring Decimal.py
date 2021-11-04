<<<<<<< HEAD
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ans =""
        oldlist = []
        if numerator*denominator < 0:
            numerator *= -1
            ans += "-"
        if abs(numerator) < abs(denominator):
            ans += "0"
        elif abs(numerator) > abs(denominator):
            temp = numerator//denominator
            ans += str(temp)
            numerator -= denominator*temp
        if numerator != 0:
            ans += "."
        while numerator != 0:
            oldlist.append(numerator)
            numerator *= 10
            while numerator < denominator:
                numerator *= 10
                ans += "0"
                oldlist.append(0)
            temp = numerator//denominator
            ans += str(temp)
            numerator -= denominator*temp
            if numerator in oldlist:
                index = len(oldlist)-oldlist.index(numerator)
                ans = ans[0:-index]+"("+ans[-index:]
                ans += ")"
                break
        return ans

=======
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ans =""
        oldlist = []
        if numerator*denominator < 0:
            numerator *= -1
            ans += "-"
        if abs(numerator) < abs(denominator):
            ans += "0"
        elif abs(numerator) > abs(denominator):
            temp = numerator//denominator
            ans += str(temp)
            numerator -= denominator*temp
        if numerator != 0:
            ans += "."
        while numerator != 0:
            oldlist.append(numerator)
            numerator *= 10
            while numerator < denominator:
                numerator *= 10
                ans += "0"
                oldlist.append(0)
            temp = numerator//denominator
            ans += str(temp)
            numerator -= denominator*temp
            if numerator in oldlist:
                index = len(oldlist)-oldlist.index(numerator)
                ans = ans[0:-index]+"("+ans[-index:]
                ans += ")"
                break
        return ans

>>>>>>> f0d27928e20afecd1453ff6c377fa43eadf1f97f
    fractionToDecimal(0,7,-12)