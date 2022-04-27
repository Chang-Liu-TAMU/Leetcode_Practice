# @Time: 2022/4/27 7:56
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-106-construct-binary-tree-from-inorder-and-postorder-traversal.py


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        a = postorder[-1]
        i = inorder.index(a)
        root = TreeNode(a)
        l = self.buildTree(inorder[:i], postorder[:i])
        r = self.buildTree(inorder[i + 1:], postorder[i:len(postorder) - 1])
        root.left = l
        root.right = r
        return root
