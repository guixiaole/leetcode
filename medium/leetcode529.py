"""
让我们一起来玩扫雷游戏！
给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，
'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，
数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。
现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），
根据以下规则，返回相应位置被点击后对应的面板：
如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。
示例 1：
输入:
[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
Click : [3,0]
输出:
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
解释:
示例 2：
输入:
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
Click : [1,2]
输出:
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
解释:
"""
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        for i in range(len(click)):  # 总共有多少次点击
            p, q = click[i]
            if board[p][q] == 'M':
                board[p][q] = 'x'
                break
            if board[p][q] == 'E':
                #  应该先检查首先的是不是数字。
                count_click = 0
                # plus_part = [(1, 0), [0, 1], [-1, 0], [0, -1]]
                plus_part = [(1, 0), [1, 1], [0, 1], [-1, -1], [-1, 0], [0, -1], [1, -1], [-1, 1]]
                for p2, q2 in plus_part:
                    left, right = p2 + p, q2 + q

                    if 0 <= left < len(board) and 0 <= right < len(board[0]):
                        if board[left][right] == 'M':
                            count_click += 1
                if count_click != 0:
                    board[p][q] = str(count_click)
                else:
                    dp = [[True for _ in range(len(board[0]))] for __ in range(len(board))]
                    board[p][q] = 'B'
                    dp[p][q] = False
                    queen = [(p, q)]
                    while len(queen) > 0:
                        p1, q1 = queen.pop(0)
                        plus_all = [(1, 0), [1, 1], [0, 1], [-1, -1], [-1, 0], [0, -1], [1, -1], [-1, 1]]
                        for j in range(len(plus_all)):
                            plusl, plusr = plus_all[j][0] + p1, plus_all[j][1] + q1
                            if 0 <= plusl < len(board) and 0 <= plusr < len(board[0]):
                                if dp[plusl][plusr] and board[plusl][plusr] == 'E':
                                    dp[plusl][plusr] = False
                                    count = 0
                                    for h in range(0, len(plus_all)):
                                        plusl1, plusr1 = plus_all[h][0] + plusl, plus_all[h][1] + plusr
                                        if 0 <= plusl1 < len(board) and 0 <= plusr1 < len(board[0]):
                                            if board[plusl1][plusr1] == 'M':
                                                count += 1
                                    if count == 0:
                                        queen.append((plusl, plusr))
                                        board[plusl][plusr] = 'B'
                                    else:
                                        board[plusl][plusr] = str(count)
        return board


if __name__ == '__main__':
    board = [['B', '1', 'E', '1', 'B'],
             ['B', '1', 'M', '1', 'B'],
             ['B', '1', '1', '1', 'B'],
             ['B', 'B', 'B', 'B', 'B']]
    click = [[1, 2]]
    c = Solution()
    board1 = c.updateBoard(board, click)
    for i in range(len(board1)):
        print(board1[i])
