# @Time: 2022/5/21 9:11
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-429-N-ary-tree-level-order-traversal.py

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        q = [root] if root else []
        while q:
            ans.append([])
            tem = []
            for i in q:
                ans[-1].append(i.val)
                if i.children:
                    tem.extend(i.children)
            q = tem
        return ans