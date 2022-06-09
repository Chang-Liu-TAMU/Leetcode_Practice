# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def help(preorder, i, j):
            if i > j:
                return None
            new = TreeNode(preorder[i])
            if i == j:
                return new
            m = None
            for k in range(i + 1, j + 1):
                if preorder[k] > preorder[i]:
                    m = k
                    break
            if m is None:
                new.left = help(preorder, i + 1, j)
                return new
            else:
                new.left = help(preorder, i + 1, m - 1)
                new.right = help(preorder, m, j)
                return new

        return help(preorder, 0, len(preorder) - 1)
