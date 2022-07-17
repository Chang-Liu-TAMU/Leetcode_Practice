# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        funcs = [lambda x, y: x < y,
                 lambda x, y: x > y]
        flag = 0
        while q:
            tem = []
            for i in range(len(q)):

                node = q[i]
                if node.val % 2 != 1 - flag:
                    return False
                if node.left:
                    tem.append(node.left)
                if node.right:
                    tem.append(node.right)
                if i != 0:
                    if not funcs[flag](q[i - 1].val, q[i].val):
                        return False
            q = tem
            flag = 1 - flag
        return True