def rotate(self, matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n // 2):
        start = i
        end = n - i - 1
        for j in range(end - start):
            matrix[start][start + j], matrix[start + j][end] = matrix[start + j][end], matrix[start][start + j]
            matrix[start][start + j], matrix[end][end - j] = matrix[end][end - j], matrix[start][start + j]
            matrix[start][start + j], matrix[end - j][start] = matrix[end - j][start], matrix[start][start + j]
rotate(0, [[1,2,3],[4,5,6],[7,8,9]])