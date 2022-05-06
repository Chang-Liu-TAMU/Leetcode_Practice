# @Time: 2022/5/6 18:52
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-141-linked-list-cycle.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # seen = set()
        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next
        # return False
        if not head:
            return False
        ptr1 = head.next
        ptr2 = head
        while ptr1 and ptr2:
            if ptr1 is ptr2:
                return True
            if ptr1.next and ptr1.next.next:
                ptr1 = ptr1.next.next
            else:
                return False
            ptr2 = ptr2.next