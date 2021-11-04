def solveSudoku(self, board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    from collections import defaultdict
    raw = defaultdict(list)
    colum = defaultdict(list)
    block = defaultdict(list)
    blank = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                blank.append([i, j])
            else:
                raw[i].append(board[i][j])
                colum[j].append(board[i][j])
                block[(i // 3) * 3 + (j // 3) + 1].append(board[i][j])

    def sudoku():
        nonlocal blank

        if not blank:
            return
        x = blank[0][0]
        y = blank[0][1]
        for i in range(1,10):
            if str(i) not in raw[x] and str(i) not in colum[y] and str(i) not in block[(x // 3) * 3 + (y // 3) + 1]:
                raw[x].append(str(i))
                colum[y].append(str(i))
                block[(x // 3) * 3 + (y // 3) + 1].append(str(i))
                board[x][y] = str(i)
                temp = blank.pop(0)
                sudoku()
                if not blank:
                    return
                raw[x].pop()
                colum[y].pop()
                block[(x // 3) * 3 + (y // 3) + 1].pop()
                board[x][y] = "."
                blank = [temp] + blank

    sudoku()

solveSudoku(0,[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
