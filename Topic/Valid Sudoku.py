def isValidSudoku(self, board) -> bool:
    from collections import defaultdict
    raw = defaultdict(list)
    colum = defaultdict(list)
    block = defaultdict(list)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                continue
            if board[i][j] in raw[i]:
                return False
            raw[i].append(board[i][j])
            if board[i][j] in colum[j]:
                return False
            colum[j].append(board[i][j])
            if board[i][j] in block[(i // 3) * 3 + (j // 3) + 1]:
                return False
            block[(i // 3) * 3 + (j // 3) + 1].append(board[i][j])
    return True

print(isValidSudoku(0, [["5","3","0","2","7","6","4","1","8"],["6","2","4","1","9","5","3","0","7"],["1","9","8","3","4","0","5","6","2"],["8","1","2","7","6","4","0","5","3"],["4","0","6","8","5","3","7","2","1"],["7","5","3","0","2","1","8","4","6"],["0","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","6","8","2","1","7","9"]]))