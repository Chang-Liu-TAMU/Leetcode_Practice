# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def help(direction, root, accu):
            if not root:
                return accu
            if not direction:
                return max([help("l", root.left, accu), help("r", root.right, accu)])
            elif direction == "l":
                return max([help("r", root.right, accu+1), help("l", root.left, 0)])
            else:
                return max([help("l", root.left, accu+1), help("r",
root.right, 0)])
        return help(None, root, 0)