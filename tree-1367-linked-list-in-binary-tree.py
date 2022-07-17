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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def isequal(root, head):
            if not head:
                return True
            l, r = False, False
            if root and root.val != head.val:
                return False
            if root:
                l = isequal(root.left, head.next)
            if root and not l:
                r = isequal(root.right, head.next)
            return l or r

        self.flag = False

        def dfs(root, head):
            if self.flag:
                return
            if root:
                if isequal(root, head):
                    self.flag = True
                else:
                    dfs(root.left, head)
                    dfs(root.right, head)

        dfs(root, head)
        return self.flag