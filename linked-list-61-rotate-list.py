# @Time: 2022/4/29 16:19
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-61-rotate-list.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        n = 0
        ptr = head
        tail = None
        while ptr:
            n += 1
            tail = ptr
            ptr = ptr.next
        _, a = divmod(k, n)
        if a == 0:
            return head
        x = 1
        ptr = head
        while x != (n - a):
            ptr = ptr.next
            x += 1

        tail.next = head
        ans = ptr.next
        ptr.next = None
        return ans