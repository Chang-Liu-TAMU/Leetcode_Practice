# @Time: 2022/5/8 12:30
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-147-insertion-sort-list.py

'''
Given the head of a singly linked list,
sort the list using insertion sort, and return the sorted list's head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head)
            head = head.next

        for i in range(1, len(l)):
            j = i - 1
            t = l[i]
            while j >= 0 and l[j].val > t.val:
                l[j + 1] = l[j]
                j -= 1
            l[j + 1] = t
        l.append(None)
        for i in range(len(l) - 1):
            l[i].next = l[i + 1]
        return l[0]