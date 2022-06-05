# @Time: 2022/6/3 14:50
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-958-check-completeness-of-a-binary-tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        empty = False
        while q:
            tem = []
            for i in q:
                if not i.left:
                    empty = True
                else:
                    if empty:
                        return False
                    else:
                        tem.append(i.left)

                if not i.right:
                    empty = True
                else:
                    if empty:
                        return False
                    else:
                        tem.append(i.right)
            q = tem
        return True