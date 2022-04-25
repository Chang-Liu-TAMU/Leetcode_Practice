# @Time: 2022/4/25 16:31
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-95-unique-binary-search-tree-2.py
# Definition for a binary tree node.
from typing import List, Optional

'''
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def help(i, j, memo):
            if i > j:
                return [None]
            if i == j:
                return [TreeNode(i)]
            if (i, j) in memo:
                return memo[(i, j)]
            ans = []
            for k in range(i, j+1):
                l = help(i, k-1, memo)
                r = help(k+1, j, memo)
                for ll in l:
                    for rr in r:
                        new = TreeNode(k)
                        new.left = ll
                        new.right = rr
                        ans.append(new)
            memo[(i, j)] = ans
            return ans
        return help(1, n, {})