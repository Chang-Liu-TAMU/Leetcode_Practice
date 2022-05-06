# @Time: 2022/4/30 16:56
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-92-reverse-linked-list-2.py
'''
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        l = []
        while head:
            l.append(head)
            head = head.next
        l[left-1:right] = l[left-1:right][::-1]
        for i in range(max(0, left-2), right):
            if i == len(l) - 1:
                l[i].next = None
            else:
                l[i].next = l[i+1]
        return l[0]