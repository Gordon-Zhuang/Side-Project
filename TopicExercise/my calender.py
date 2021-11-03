from collections import defaultdict
class MyCalendarThree:
    def __init__(self):
        self.calender = defaultdict(int)
    def book(self, start: int, end: int) -> int:
        self.calender[start] += 1
        self.calender[end] -= 1
        event, ans = 0, 0
        self.calender = sorted(self.calender)
        for day in self.calender:
            event += self.calender[day]
            ans = max(ans, event)
        return ans


test = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
calender = MyCalendarThree()
for i in range(len(test)):
    print(calender.book(test[i][0], test[i][1]))