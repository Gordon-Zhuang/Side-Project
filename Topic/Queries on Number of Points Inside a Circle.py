def countPoints(self, points, queries):
    ans = [0] * len(queries)
    for circle in range(len(queries)):
        for point_index in range(len(points)):
            if pow(points[point_index][0] - queries[circle][0], 2) + pow(points[point_index][1] - queries[circle][1],
                                                                         2) == pow(queries[circle][2], 2):
                ans[circle] += 1
    return ans

countPoints(0, [[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]])