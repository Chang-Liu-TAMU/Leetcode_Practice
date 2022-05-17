# @Time: 2022/5/12 20:15
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-382-linked-list-random-node.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    reservoir sampling
    (k / i)  *   (i) / (i+1)  * (i+1) / (i+2) * (n-1) / n = k / n
    """
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        ans = 0
        ptr = self.head
        n = 1
        k = 1
        while ptr:
            if random.random() < k / n:
                ans = ptr.val
            ptr = ptr.next
            n += 1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()