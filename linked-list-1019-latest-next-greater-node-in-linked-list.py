# @Time: 2022/5/25 9:55
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-1019-latest-next-greater-node-in-linked-list.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        '''
        monotone stack
        '''
        ptr = head
        n = 0
        while ptr:
            n += 1
            ptr = ptr.next
        q_asc = []
        ans = [0] * n
        i = 0
        while head:
            while q_asc and q_asc[-1][1] < head.val:
                index, value = q_asc.pop()
                ans[index] = head.val
            q_asc.append((i, head.val))
            i += 1
            head = head.next
        return ans