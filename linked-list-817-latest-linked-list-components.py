# @Time: 2022/5/20 14:41
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-817-latest-linked-list-components.py


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        flag = False
        while head:
            if head.val in s:
                if not flag:
                    flag = True
                    ans += 1
            else:
                flag = False
            head = head.next
        return ans