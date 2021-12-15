def maxPoints(self, points):
    from collections import defaultdict
    ans = 0
    for i in range(len(points)):
        dic = defaultdict(int)
        for j in range(i + 1, len(points)):
            if points[i][0] - points[j][0] == 0:
                slope = "unlimit"
            else:
                slope = (points[i][1] - points[j][1]) * 1.0 / points[i][0] - points[j][0]
            dic[slope] += 1
            ans = max(ans, max(dic.values()) + 1)
    return ans
maxPoints(0, [[1,1],[2,2],[3,3]])