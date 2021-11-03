def myPow(self, x: float, n: int) -> float:

    def pow2(now, p):
        if p <= n:
            renumber, left = pow2(now * now, p * 2)
            return renumber + (now - 1) * renumber * (left // p), left - p * (left // p)
        return 1, n

    if n < 0:
        n *= -1
        ans, temp = pow2(1/x, 1)
        return ans
    else:
        ans, temp = pow2(x, 1)
        return ans
print(myPow(0,2,-5))