# @Time: 2022/5/7 13:40
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-142-linked-list-cycle-II.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head
        while ptr1 and ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if ptr1 is ptr2:
                a = head
                b = ptr1
                while a is not b:
                    a = a.next
                    b = b.next
                return a
        return None


"""

distance from head to cycle entry is z
0 - 0 - 0 - 0 - 0 - * - 0 - 0 - * - 0
                    |               |
                    0               0
                    |               |
                    0 - 0 - 0 - 0 - 0
when slow one arrives at cycle entry, assume x away from fast one
and x + y is the total length of the cycle
when they meet, slow one is away from entry y

one important fact: when you walk z at pace 1/step from entry, you end up at 
x away from entry.

and remember x + y = the whole cycle. You are at the cycle entry.
                                        
"""