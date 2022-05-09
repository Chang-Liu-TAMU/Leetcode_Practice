# @Time: 2022/5/8 12:55
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-148-sort-list.py


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        n = 0
        ptr = head
        while ptr:
            if not ptr.next:
                tail = ptr
            n += 1
            ptr = ptr.next

        def merge_sort(head, tail, l):
            if l == 1:
                assert head is tail
                return head
            m = l // 2
            n = 1
            ptr1 = head
            while n != m:
                ptr1 = ptr1.next
                n += 1
            ptr2 = ptr1.next
            ptr1.next = None
            l1 = merge_sort(head, ptr1, m)
            l2 = merge_sort(ptr2, tail, l - m)
            head = None
            tail = None
            while l1 and l2:
                if l1.val <= l2.val:
                    if not head:
                        head = tail = l1
                    else:
                        tail.next = l1
                    tail = l1
                    l1 = l1.next
                else:
                    if not head:
                        head = tail = l2
                    else:
                        tail.next = l2
                    tail = l2
                    l2 = l2.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return head

        return merge_sort(head, tail, n)