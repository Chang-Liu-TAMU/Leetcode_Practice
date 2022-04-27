# @Time: 2022/4/27 10:38
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-113-path-sum-2.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []

        def bt(root, path, s):
            path.append(root.val)
            s += root.val
            if not root.left and not root.right:
                if s == targetSum:
                    ans.append(path[::])

            if root.left:
                bt(root.left, path, s)
            if root.right:
                bt(root.right, path, s)
            path.pop()

        bt(root, [], 0)
        return ans