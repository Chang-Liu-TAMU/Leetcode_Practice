# @Time: 2022/4/29 15:33
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-19-remove-nth-node-from-end-of-list.py


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x = 0
        ptr = head
        while ptr:
            x += 1
            ptr = ptr.next
        if n == x:
            return head.next

        y = x - n
        x = 1
        ptr = head
        while x != y:
            x += 1
            ptr = ptr.next
        ptr.next = ptr.next.next
        return head