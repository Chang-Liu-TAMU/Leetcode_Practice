# @Time: 2022/4/29 8:54
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-129-sum-root-to-leaf-numbers.py

'''
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def bt(node, path):
            path.append(str(node.val))
            if not node.left and not node.right:
                self.ans += int("".join(path))
            else:
                if node.left:
                    bt(node.left, path)
                if node.right:
                    bt(node.right, path)
            path.pop()
        bt(root, [])
        return self.ans