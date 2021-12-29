def slidingPuzzle(self, board):
    ans = -1
    lib = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                index = [i, j]
                break
    old_list = []
    stack = [board]
    next_stack = []
    stack_index = [index]
    next_index = []
    step = 0
    while stack:
        while stack:
            board = stack.pop()
            index = stack_index.pop()
            if board == [[1, 2, 3], [4, 5, 0]]:
                ans = step
                next_stack = []
                break
            for i, j in lib:
                if index[0] + i >= 0 and index[0] + i < 2 and index[1] + j >= 0 and index[1] + j < 3:
                    board[index[0]][index[1]], board[index[0] + i][index[1] + j] = board[index[0] + i][index[1] + j], board[index[0]][index[1]]
                    if board not in old_list:
                        next_stack.append([raw[:] for raw in board])
                        next_index.append([index[0] + i, index[1] + j])
                    board[index[0]][index[1]], board[index[0] + i][index[1] + j] = board[index[0] + i][index[1] + j], board[index[0]][index[1]]
        step += 1
        stack = next_stack
        next_stack = []
        stack_index = next_index
        next_index = []0
    return ans
slidingPuzzle(0, [[4,1,2],[5,0,3]])