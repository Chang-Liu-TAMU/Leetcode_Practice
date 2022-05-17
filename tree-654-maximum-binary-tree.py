# @Time: 2022/5/16 13:01
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-654-maximum-binary-tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def help(arr, i, j):
            m = i
            val = arr[i]
            for k in range(i, j + 1):
                if arr[k] > val:
                    val = arr[k]
                    m = k
            return m

        def construct(arr, i, j):
            if i == j:
                return TreeNode(arr[i])
            if i > j:
                return None
            m = help(arr, i, j)
            root = TreeNode(arr[m])
            root.left = construct(arr, i, m - 1)
            root.right = construct(arr, m + 1, j)
            return root

        return construct(nums, 0, len(nums) - 1)