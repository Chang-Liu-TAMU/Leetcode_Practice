# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        def find_ptr(l1, n):
            prev, ptr = None, l1
            c = 0
            while c != n:
                c += 1
                prev = ptr
                ptr = ptr.next
            return prev, ptr

        head = list2
        while list2.next:
            list2 = list2.next
        tail = list2

        x, y = find_ptr(list1, a)
        i, j = find_ptr(list1, b)
        tail.next = j.next
        if not x:
            return head
        x.next = head
        return list1