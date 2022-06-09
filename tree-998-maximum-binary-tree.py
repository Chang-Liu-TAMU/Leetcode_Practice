# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        prev = None
        ptr = root
        while True:
            new = TreeNode(val)
            if not ptr:
                prev.right = new
                return root
            if ptr.val < val:
                new.left = ptr
                if not prev:
                    return new
                else:
                    prev.right = new
                    return root
            else:
                prev = ptr
                ptr = ptr.right