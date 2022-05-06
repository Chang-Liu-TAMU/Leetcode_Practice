# @Time: 2022/5/2 9:54
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-222-count-complete-tree-nodes.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d = 0
        ptr = root
        while ptr:
            d += 1
            ptr = ptr.left

        q = [root]
        h = 1
        while q:
            if h == d - 1:
                break
            tem = []
            for i in q:
                if i.left:
                    tem.append(i.left)
                if i.right:
                    tem.append(i.right)
            h += 1
            q = tem
        ans = 2 ** d - 1
        for i in range(-1, -len(q) - 1, -1):
            if not q[i].right:
                ans -= 1
            else:
                break
            if not q[i].left:
                ans -= 1
            else:
                break
        return ans
