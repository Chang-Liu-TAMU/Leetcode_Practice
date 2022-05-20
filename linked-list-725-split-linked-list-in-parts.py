# @Time: 2022/5/18 10:28
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-725-split-linked-list-in-parts.py


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        ptr = head
        while head:
            n += 1
            head = head.next

        ans = [None] * k
        x, y = divmod(n, k)
        num = [x + 1 if i < y else x for i in range(k)]
        res = []
        t = 0
        c = 1
        while ptr:
            if c == 1:
                res.append(ptr)
            if c == num[t]:
                tem = ptr.next
                ptr.next = None
                # reset
                ptr = tem
                c = 1
                t += 1
            else:
                c += 1
                ptr = ptr.next
        res.extend([None] * (k - len(res)))
        return res
