# @Time: 2022/5/14 18:02
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-623-add-one-row-to-tree.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new = TreeNode(val)
            new.left = root
            return new
        level = 1
        q = [root]
        while q:
            tem = []
            if level == depth - 1:
                for i in q:
                    l = i.left
                    r = i.right
                    i.left = TreeNode(val)
                    i.left.left = l
                    i.right = TreeNode(val)
                    i.right.right = r
                break
            else:
                for i in q:
                    if i.left:
                        tem.append(i.left)
                    if i.right:
                        tem.append(i.right)
                q = tem
                level += 1
        return root