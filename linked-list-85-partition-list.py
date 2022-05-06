# @Time: 2022/4/30 16:34
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-85-partition-list.py
'''
Given the head of a linked list and a value x, partition it such that all
nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the
two partitions.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        small = None
        tail1 = None
        large = None
        tail2 = None
        while head:
            if head.val < x:
                if not small:
                    small = head
                    tail1 = head
                else:
                    tail1.next = head
                    tail1 = head
            else:
                if not large:
                    large = head
                    tail2 = head
                else:
                    tail2.next = head
                    tail2 = head
            head = head.next
        if tail2:
            tail2.next = None
        if small:
            tail1.next = large
            return small
        else:
            return large