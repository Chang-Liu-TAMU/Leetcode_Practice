# @Time: 2022/4/29 15:47
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-21-merge-two-linked-list.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = None
        tail = None
        while p1 and p2:
            if p1.val <= p2.val:
                if not head:
                    head = p1
                    tail = head
                else:
                    tail.next = p1
                tail = p1
                p1 = p1.next
            else:
                if not head:
                    head = p2
                    tail = head
                else:
                    tail.next = p2
                tail = p2
                p2 = p2.next
        if not head:
            return p1 if p1 else p2
        if p1:
            tail.next = p1
        if p2:
            tail.next = p2
        return head