<<<<<<< HEAD
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                if j > i + 1 and num[i + 1] == '0':
                    break
                one = int(num[0:i + 1])
                two = int(num[i + 1:j + 1])
                three = one + two
                now = j + 1
                while now + len(str(three)) <= len(num):
                    if num[now: now + len(str(three))] == str(three):
                        if now + len(str(three)) == len(num):
                            return True
                        now += len(str(three))
                        one = two
                        two = three
                        three = one + two

                    else:
                        break
        return False

=======
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                if j > i + 1 and num[i + 1] == '0':
                    break
                one = int(num[0:i + 1])
                two = int(num[i + 1:j + 1])
                three = one + two
                now = j + 1
                while now + len(str(three)) <= len(num):
                    if num[now: now + len(str(three))] == str(three):
                        if now + len(str(three)) == len(num):
                            return True
                        now += len(str(three))
                        one = two
                        two = three
                        three = one + two

                    else:
                        break
        return False

>>>>>>> f0d27928e20afecd1453ff6c377fa43eadf1f97f
    isAdditiveNumber(0, "111122335588143")