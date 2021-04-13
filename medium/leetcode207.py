"""
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
示例 1:
输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:
输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
"""
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    flag = [-1 for _ in range(numCourses)]
    for i in range(len(prerequisites)):
        flag[prerequisites[i][0]] += 1
        #  首先确定这个有没有先决条件,找到一个闭合的圈
    flag_queen = 1
    pos = 0
    flag_len = 0
    #  连续两次数组长度没有变化
    last_len = len(prerequisites)
    while flag_queen == 1 and len(prerequisites) >= 1:  # 首先要在这个里面，并且没找到闭合的圈
        if pos == len(prerequisites):
            pos = 0  # 在一个圈里面。并且每次循环之后开始看看有没有闭合的圈
            if len(prerequisites) != last_len:
                last_len = len(prerequisites)
                flag_len = 0
            else:
                flag_len += 1
                if flag_len >= 2:
                    flag_queen = 0
        else:
            if flag[prerequisites[pos][1]] == -1:
                flag[prerequisites[pos][0]] -= 1
                prerequisites.pop(pos)
            else:
                pos += 1
    if flag_queen == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    prerequisites = [[2, 0], [2, 1]]
    print(canFinish(3, prerequisites))
