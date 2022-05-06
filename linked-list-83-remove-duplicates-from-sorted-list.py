# @Time: 2022/4/30 16:12
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-83-remove-duplicates-from-sorted-list.py


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        ptr = head
        former = None
        while ptr:
            if not former:
                former = ptr
            else:
                while ptr and ptr.val == former.val:
                    ptr = ptr.next
                former.next = ptr
                former = ptr
            if ptr:
                ptr = ptr.next
        return head