# @Time: 2022/5/27 9:59
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-1171-latest-remove-zero-sum-consecutive-nodes-from-linked-list.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        d = {0: sentinel}
        s = 0
        while head:
            s += head.val
            d[s] = head
            head = head.next
        ptr = sentinel
        s = 0
        while ptr:
            s += ptr.val
            jump_to = d[s]
            ptr.next = jump_to.next
            ptr = jump_to.next
        return sentinel.next