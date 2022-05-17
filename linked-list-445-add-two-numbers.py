# @Time: 2022/5/15 13:47
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-445-add-two-numbers.py


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def ddl(node):
            ptr = node
            former = ListNode(0, node)
            former.last = None
            c = 0
            while ptr:
                c += 1
                ptr.last = former
                former = ptr
                ptr = ptr.next
            return former, c

        def add(ptr1, ptr2):
            x = 0
            while ptr1 and ptr2 and ptr1.last:
                ans = ptr1.val + ptr2.val + x
                if ans < 10:
                    ptr1.val = ans
                    x = 0
                else:
                    ptr1.val = ans % 10
                    x = 1
                ptr1 = ptr1.last
                ptr2 = ptr2.last
            if ptr1 and ptr2:
                if not x:
                    return ptr1.next
                else:
                    ptr1.val = 1
                    return ptr1
            else:
                while ptr1.last:
                    ans = ptr1.val + x
                    x, ptr1.val = divmod(ans, 10)
                    ptr1 = ptr1.last
                if x:
                    ptr1.val = 1
                    return ptr1
                else:
                    return ptr1.next

        ptr1, n1 = ddl(l1)
        ptr2, n2 = ddl(l2)
        if n1 >= n2:
            return add(ptr1, ptr2)
        else:
            return add(ptr2, ptr1)