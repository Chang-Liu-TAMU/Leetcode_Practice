# @Time: 2022/4/26 21:23
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-102-binary-tree-order-traversal.py

'''
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            ans.append([])
            tem = []
            for i in q:
                ans[-1].append(i.val)
                if i.left:
                    tem.append(i.left)
                if i.right:
                    tem.append(i.right)
            q = tem
        return ans
