# @Time: 2022/4/27 8:04
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-107-binary-tree-level-order-traversal-2.py


'''
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
(i.e., from left to right, level by level from leaf to root).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ans = []
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
        ans.reverse()
        return ans