# @Time: 2022/4/29 9:20
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-2-add-two-numbers.py

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def help(ptr, x):
            while ptr.next:
                x, y = divmod(ptr.val + x, 10)
                ptr.val = y
                if x == 0:
                    return
                ptr = ptr.next
            tem = ptr.val + x
            if tem < 10:
                ptr.val = tem
            else:
                ptr.val = tem % 10
                ptr.next = ListNode(1)

        ptr1 = l1
        ptr2 = l2
        cache = 0
        former = None
        while ptr1.next and ptr2.next:
            addition = ptr1.val + ptr2.val + cache
            cache, ptr1.val = divmod(addition, 10)
            former = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        if not ptr2.next:
            help(ptr1, ptr2.val + cache)
            return l1
        else:
            help(ptr2, ptr1.val + cache)
            if not former:
                return l2
            else:
                former.next = ptr2
                return l1