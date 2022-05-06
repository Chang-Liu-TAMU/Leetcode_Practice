# @Time: 2022/4/29 16:09
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-25-reverse-nodes-in-k-groups.py
'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = [[]]
        n = 1
        p = head
        while p:
            l[-1].append(p)
            if n % k == 0:
                l.append([])
            n +=1
            p = p.next
        if l[-1] == []:
            l.pop()
        for i in l:
            if len(i) == k:
                i.reverse()
        for i in l:
            for j in range(len(i)-1):
                i[j].next = i[j+1]
        for i in range(len(l)-1):
            l[i][-1].next = l[i+1][0]
        l[-1][-1].next = None
        return l[0][0]