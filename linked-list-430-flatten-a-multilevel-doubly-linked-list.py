# @Time: 2022/5/19 12:54
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-430-flatten-a-multilevel-doubly-linked-list.py


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def help(head):
            h = None
            t = None
            while head:
                if not h:
                    h = head
                    t = head
                else:
                    t.next = head
                    head.prev = t
                    t = head
                next_ = head.next
                if head.child:
                    hh, tt = help(head.child)
                    head.child = None
                    t.next = hh
                    hh.prev = t
                    t = tt
                head = next_
            return h, t

        if not head:
            return None
        h = help(head)[0]

        return h