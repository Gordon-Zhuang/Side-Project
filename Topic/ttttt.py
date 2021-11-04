class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        def word(now, leftword, w):
            if len(leftword) == 0:
                ans.append(words[w])
                words[w] = "-"
                return True
            for i, j in [[1,0],[0,1],[-1,0],[0,-1]]:
                check = False
                if now[0]+i >= 0 and now[0]+i < len(board) and now[1]+j >= 0 and now[1]+j < len(board[0]) and board[now[0]+i][now[1]+j] == leftword[0]:
                    temp = board[now[0]+i][now[1]+j]
                    board[now[0]+i][now[1]+j] = -1
                    check = word([now[0]+i,now[1]+j], leftword[1:], w)
                    board[now[0]+i][now[1]+j] = temp
                if check == True:
                    return True
            return False
        for i in range(len(words)):
            for j in range(len(board)):
                for k in range(len(board[j])):
                    if board[j][k] == words[i][0]:
                        word([j,k], words[i][1:], i)
        return ans

    findWords(0, [["a","a"]], ["aaa"])


"""
    arr = []
    ardic = defaultdict(int)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "d":
                arr.append([i,j])
                ardic[i,j] += 2

    dic = defaultdic(list)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            dic[abs(arr[i][0]-arr[j][0])+abs(arr[i][1]-arr[j][1])] += [[arr[i][0], arr[i][1], arr[j][0], arr[j][1]]]
    order = sorted(dic.keys())
    ansarr1 = []
    ansarr2 = []
    for i in range(len(order)):
        for j in range(len(dic[order[i]]):
            if arrdic[(dic[order[i]][j][0],dic[order[i]][j][1])] > 0 and arrdic[(dic[order[i]][j][2],dic[order[i]][j][3])] > 0:
"""