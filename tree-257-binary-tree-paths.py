# @Time: 2022/5/6 9:29
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-257-binary-tree-paths.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def help(node, path):
            path.append(str(node.val))
            if not node.left and not node.right:
                self.ans.append("->".join(path))
            if node.left:
                help(node.left, path)
            if node.right:
                help(node.right, path)
            path.pop()
        self.ans = []
        help(root, [])
        return self.ans