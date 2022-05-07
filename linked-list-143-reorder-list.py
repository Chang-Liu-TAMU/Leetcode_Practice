# @Time: 2022/5/7 14:07
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-143-reorder-list.py
'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = []
        while head:
            l.append(head)
            head = head.next
        new = []
        for i in range((len(l)+1)//2):
            new.append(l[i])
            new.append(l[len(l)-1-i])
        for i in range(len(new)-1):
            new[i].next = new[i+1]
        new[-1].next = None