# @Time: 2022/4/29 15:55
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-24-swap-nodes-in-pairs.py
'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the
 values in the list's nodes (i.e., only nodes themselves may be changed.)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        if not head:
            return None
        while head:
            l.append(head)
            head = head.next
        for i in range(len(l) // 2):
            l[i*2], l[i*2+1] = l[i*2+1], l[i*2]
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        l[-1].next = None
        return l[0]