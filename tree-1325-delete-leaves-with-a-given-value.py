# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        l, r = self.removeLeafNodes(root.left, target), \
                self.removeLeafNodes(root.right, target)
        root.left = l
        root.right = r
        if not l and not r:
            if root.val == target:
                return None
        return root