# @Time: 2022/5/2 9:23
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-199-binary-tree-right-side-view.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            tem = []
            ans.append(q[-1].val)
            for i in q:
                if i.left:
                    tem.append(i.left)
                if i.right:
                    tem.append(i.right)
            q = tem
        return ans