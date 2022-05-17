# @Time: 2022/5/16 13:20
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-1721-swapping-nodes-in-linked-list.py


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head)
            head = head.next

        ptr1 = k - 1
        ptr2 = len(l) - k
        l[ptr1], l[ptr2] = l[ptr2], l[ptr1]
        if ptr1 - 1 >= 0:
            l[ptr1 - 1].next = l[ptr1]
        if ptr1 + 1 < len(l):
            l[ptr1].next = l[ptr1 + 1]

        if ptr2 - 1 >= 0:
            l[ptr2 - 1].next = l[ptr2]
        if ptr2 + 1 < len(l):
            l[ptr2].next = l[ptr2 + 1]
        l[-1].next = None
        return l[0]