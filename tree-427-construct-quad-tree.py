# @Time: 2022/5/22 11:21
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-427-construct-quad-tree.py

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isleaf(grid, i, j, p, q):
            s = sum([sum(grid[k][p:q + 1]) for k in range(i, j + 1)])
            t = (j - i + 1) * (q - p + 1)
            if s == 0:
                return True, 0
            elif s == t:
                return True, 1
            else:
                return False, None

        def help(grid, i, j, p, q):
            # can not use isleaf, val = isleaf(*args)
            # just know it
            leaf, val = isleaf(grid, i, j, p, q)
            if leaf:
                return Node(val, 1, None, None, None, None)
            else:
                n = j - i + 1
                n //= 2
                tl = help(grid, i, i + n - 1, p, p + n - 1)
                tr = help(grid, i, i + n - 1, p + n, q)
                bl = help(grid, i + n, j, p, p + n - 1)
                br = help(grid, i + n, j, p + n, q)
                new = Node(1, 0, tl, tr, bl, br)
                return new

        n = len(grid)
        return help(grid, 0, n - 1, 0, n - 1)