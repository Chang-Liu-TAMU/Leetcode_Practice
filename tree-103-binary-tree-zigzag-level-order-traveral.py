# @Time: 2022/4/26 21:31
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-103-binary-tree-zigzag-level-order-traveral.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ans = []
        flag = True
        while q:
            tem = []
            ans.append([])
            for i in q:
                ans[-1].append(i.val)
                if i.left:
                    tem.append(i.left)
                if i.right:
                    tem.append(i.right)
            if not flag:
                ans[-1].reverse()
            flag = not flag
            q = tem
        return ans