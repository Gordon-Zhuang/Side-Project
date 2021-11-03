def multiply(self, num1: str, num2: str) -> str:
    n1, n2 = num1, num2

    def multidic(n1, n2):
        ans = int(n1) * int(n2)
        return str(ans // 10), str(ans % 10)

    def adddic(n1, n2):
        ans = int(n1) + int(n2)
        return str(ans // 10), str(ans % 10)

    ans = [0] * (len(n1) + len(n2))
    for i in range(len(n1)):
        for j in range(len(n2)):
            pos = i + j + 1
            carry_mut, num = multidic(n1[i], n2[j])
            carry_add, ans[pos] = adddic(ans[pos], num)
            temp, carry_add = adddic(carry_mut, carry_add)
            while carry_add != "0":
                pos -= 1
                carry_add, ans[pos] = adddic(carry_add, ans[pos])
    strans = ""
    if ans[0] == "0":
        counter = 1
    else:
        counter = 0
    while counter < len(ans):
        strans += ans[counter]
        counter += 1
multiply(0, "123", "456")