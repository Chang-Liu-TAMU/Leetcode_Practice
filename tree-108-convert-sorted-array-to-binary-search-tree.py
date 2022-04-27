# @Time: 2022/4/27 8:10
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-108-convert-sorted-array-to-binary-search-tree.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def help(i, j):
            if i > j:
                return None
            elif i == j:
                return TreeNode(nums[i])
            else:
                middle = (i + j) // 2
                root = TreeNode(nums[middle])
                root.left = help(i, middle-1)
                root.right = help(middle+1, j)
                return root
        return help(0, len(nums)-1)