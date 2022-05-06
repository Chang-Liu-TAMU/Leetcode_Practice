# @Time: 2022/4/29 16:43
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-82-remove-duplicates-from-sorted-list-2.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#method 1
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
#         stack = []
#         dups = set()
#         while head:
#             if head.val not in dups:
#                 if stack:
#                     if stack[-1].val == head.val:
#                         stack.pop()
#                         dups.add(head.val)
#                     else:
#                         stack.append(head)
#                 else:
#                     stack.append(head)
#             head = head.next
#         if not stack:
#             return None
#         for i in range(len(stack)-1):
#             stack[i].next = stack[i+1]
#         stack[-1].next = None
#         return stack[0]



#method2
# class Solution:
# #     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
# #
# #         if not head:
# #             return None
# #         if not head.next:
# #             return head
# #         a, b = head, head.next
# #         while b and b.val == a.val:
# #             b = b.next
# #         if b is a.next:
# #             a.next = self.deleteDuplicates(b)
# #             return a
# #         else:
# #             return self.deleteDuplicates(b)


#method3

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        h = None
        ptr = head
        tail = None
        while True:
            if not ptr.next:
                if not h:
                    return ptr
                else:
                    tail.next = ptr
                    return h
            if ptr.next.val == ptr.val:
                target = ptr.val
                while ptr and ptr.val == target:
                    ptr = ptr.next
                if not ptr:
                    if tail:
                        tail.next = None
                    return h
            else:
                if not h:
                    h = ptr
                    tail = ptr
                else:
                    tail.next = ptr
                    tail = ptr
                ptr = ptr.next