# @Time: 2022/5/10 9:41
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-328-odd-even-linked-list.py



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd_head = head
        odd_tail = head
        even_head = head.next
        even_tail = head.next

        while True:
            if not even_tail.next:
                return head
            if not even_tail.next.next:
                odd_tail.next = even_tail.next
                even_tail.next.next = even_head
                even_tail.next = None
                return head
            ptr1 = even_tail.next
            ptr2 = ptr1.next
            odd_tail.next = ptr1
            ptr1.next = even_head
            odd_tail = ptr1
            even_tail.next = ptr2
            even_tail = ptr2
