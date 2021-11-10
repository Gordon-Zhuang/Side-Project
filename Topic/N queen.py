def solveNQueens(self, n: int):
    ans = []

    def dfs(column, left_row, queen_array):
        if column == n:
            temp_ans = ["." * n for _ in range(n)]
            for i in range(len(queen_array)):
                temp_ans[queen_array[i][0]] = temp_ans[queen_array[i][0]][:[queen_array[i][1]]] + "Q" + temp_ans[queen_array[i][0]][[queen_array[i][1]]+1:]
            ans.append(temp_ans)
            return
        for i in range(len(left_row)):
            check = 1
            temp1 = column + left_row[i]
            temp2 = column - left_row[i]
            for j in range(len(queen_array)):
                if temp1 == queen_array[j][0] + queen_array[j][1] or temp2 == queen_array[j][0] - queen_array[j][1]:
                    check = 0
                    break
            if check == 1:
                dfs(column + 1, left_row[:i] + left_row[i + 1:], queen_array + [[column, left_row[i]]])

    dfs(0, [i for i in range(n)], [])
    return ans
solveNQueens(0, 4)