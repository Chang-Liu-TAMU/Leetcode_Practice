# @Time: 2022/5/10 18:15
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-450-delete-node-in-a-BST.py



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                ans = root.left
                ptr1 = ans.right
                ans.right = root.right
                ptr2 = ans.right
                if not ptr1: return ans
                while ptr2.left:
                    ptr2 = ptr2.left
                ptr2.left = ptr1
                return ans
        ptr = root
        former = None
        while ptr and ptr.val != key:
            former = ptr
            if ptr.val > key:
                ptr = ptr.left
            else:
                ptr = ptr.right

        if not ptr:
            return root
        if not ptr.left:
            if ptr is former.left:
                former.left = ptr.right
            else:
                former.right = ptr.right
        elif not ptr.right:
            if ptr is former.left:
                former.left = ptr.left
            else:
                former.right = ptr.left
        else:
            x = ptr.left
            y = ptr.right
            z = y
            while z.left:
                z = z.left
            if ptr is former.left:
                former.left = x
            else:
                former.right = x
            tem = x.right
            x.right = y
            z.left = tem
        return root