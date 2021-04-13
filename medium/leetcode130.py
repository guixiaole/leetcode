"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        首先找到边缘处的O，然后使用DFS进行遍历，修改参数，最后遍历board，进行修改。
        """
        if len(board) <= 0:
            return
        dp = [[False for _ in range(len(board[0]))] for __ in range(len(board))]
        #  首先是四个边界。
        pos = [0, len(board) - 1]
        for h in range(len(pos)):
            pos_h = pos[h]
            for i in range(len(board[0])):
                if board[pos_h][i] == 'O' and not dp[pos_h][i]:
                    dp[pos_h][i] = True
                    statck = [(pos_h, i)]  # 存储其坐标
                    while len(statck) > 0:
                        left, right = statck.pop(0)
                        plus_minus = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        for j in range(len(plus_minus)):
                            tempplus, tempminus = plus_minus[j]
                            temp_left = tempplus + left
                            temp_right = tempminus + right
                            if -1 < temp_left < len(board) and -1 < temp_right < len(board[0]):
                                if not dp[temp_left][temp_right] and board[temp_left][temp_right] == 'O':
                                    statck.append((temp_left, temp_right))
                                    dp[temp_left][temp_right] = True
        pos1 = [0, len(board[0]) - 1]
        for h in range(0, len(pos1)):
            pos_h = pos1[h]
            for i in range(0, len(board)):
                if board[i][pos_h] == 'O' and not dp[i][pos_h]:
                    dp[i][pos_h] = True
                    statck = [(i, pos_h)]  # 存储其坐标
                    while len(statck) > 0:
                        left, right = statck.pop(0)
                        plus_minus = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        for j in range(len(plus_minus)):
                            tempplus, tempminus = plus_minus[j]
                            temp_left = tempplus + left
                            temp_right = tempminus + right
                            if -1 < temp_left < len(board) and -1 < temp_right < len(board[0]):
                                if not dp[temp_left][temp_right] and board[temp_left][temp_right] == 'O':
                                    statck.append((temp_left, temp_right))
                                    dp[temp_left][temp_right] = True
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 'O' and not dp[i][j]:
                    board[i][j] = 'X'


if __name__ == '__main__':
    c = Solution()
    board = [["O", "X", "O", "O", "X", "X", "X", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "O", "X"],
             ["X", "O", "X", "O", "O", "X", "X", "O", "O", "X", "O", "X", "O", "X", "O", "X", "X", "O", "O", "O"],
             ["O", "X", "O", "O", "O", "X", "X", "X", "X", "O", "O", "O", "O", "O", "X", "X", "X", "X", "O", "X"],
             ["X", "X", "O", "O", "O", "X", "X", "O", "O", "O", "X", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
             ["O", "X", "O", "X", "X", "O", "X", "O", "O", "O", "X", "O", "O", "X", "O", "O", "O", "O", "O", "X"],
             ["X", "O", "O", "X", "O", "X", "O", "O", "O", "X", "X", "O", "X", "O", "O", "X", "O", "O", "O", "O"],
             ["X", "O", "O", "O", "X", "X", "O", "O", "O", "O", "O", "X", "O", "O", "X", "O", "O", "O", "O", "X"],
             ["X", "O", "O", "O", "X", "O", "X", "X", "X", "O", "X", "O", "X", "X", "X", "X", "O", "O", "O", "X"],
             ["X", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "X"],
             ["O", "O", "O", "X", "O", "X", "X", "X", "X", "X", "X", "X", "X", "X", "O", "O", "O", "O", "X", "O"],
             ["X", "O", "X", "O", "X", "O", "O", "X", "X", "X", "O", "X", "X", "O", "O", "X", "X", "O", "O", "O"],
             ["O", "X", "O", "O", "X", "O", "O", "O", "O", "O", "O", "X", "X", "X", "X", "O", "O", "O", "X", "O"],
             ["X", "O", "O", "O", "X", "X", "X", "O", "X", "O", "O", "O", "X", "O", "X", "O", "X", "O", "O", "X"],
             ["O", "O", "O", "O", "X", "O", "X", "X", "O", "X", "O", "X", "O", "X", "X", "X", "X", "O", "O", "O"],
             ["O", "X", "X", "O", "O", "O", "O", "X", "O", "O", "X", "X", "X", "O", "O", "X", "X", "O", "X", "O"],
             ["X", "O", "X", "X", "X", "X", "X", "X", "O", "X", "X", "O", "X", "O", "O", "X", "O", "O", "O", "X"],
             ["X", "O", "O", "O", "X", "O", "X", "O", "O", "X", "O", "X", "O", "O", "X", "O", "O", "X", "X", "X"],
             ["O", "O", "X", "O", "O", "O", "O", "X", "O", "O", "X", "X", "O", "X", "X", "X", "O", "O", "O", "O"],
             ["O", "O", "X", "O", "O", "O", "O", "O", "O", "X", "X", "O", "X", "O", "X", "O", "O", "O", "X", "X"],
             ["X", "O", "O", "O", "X", "O", "X", "X", "X", "O", "O", "X", "O", "X", "O", "X", "X", "O", "O", "O"]]
    c.solve(board)
