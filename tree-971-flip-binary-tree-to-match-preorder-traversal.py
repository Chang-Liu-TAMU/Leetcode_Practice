# @Time: 2022/6/3 15:56
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-971-flip-binary-tree-to-match-preorder-traversal.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.flag = False
        self.ans = []

        def dfs(root, l):
            if self.flag:
                return
            try:
                if root.val != l[0]:
                    self.flag = True
                    return
                if root.left and root.right:
                    x, y = root.left.val, root.right.val
                    if l[1] == x:
                        i = l.index(y)
                        dfs(root.left, l[1:i])
                        dfs(root.right, l[i:])
                    elif l[1] == y:
                        i = l.index(x)
                        self.ans.append(root.val)
                        dfs(root.left, l[i:])
                        dfs(root.right, l[1:i])
                    else:
                        self.flag = True
                elif (not root.left) and (not root.right):
                    if len(l) != 1:
                        self.flag = True
                elif root.left:
                    dfs(root.left, l[1:])
                else:
                    dfs(root.right, l[1:])
            except Exception as e:
                print(e)
                self.flag = True

        dfs(root, voyage)
        if self.flag:
            return [-1]
        return self.ans