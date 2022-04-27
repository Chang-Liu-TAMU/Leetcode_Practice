# @Time: 2022/4/27 8:44
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-109-convert-sorted-list-to-binary-search-tree.py

'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def help(i, j):
            if i > j:
                return None
            elif i == j:
                return TreeNode(nums[i])
            else:
                middle = (i + j) // 2
                root = TreeNode(nums[middle])
                root.left = help(i, middle - 1)
                root.right = help(middle + 1, j)
                return root

        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return help(0, len(nums) - 1)