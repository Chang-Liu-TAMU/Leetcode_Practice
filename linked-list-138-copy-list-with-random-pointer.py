# @Time: 2022/5/1 20:04
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-138-copy-list-with-random-pointer.py

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr = head
        d = {None: None}
        while ptr:
            if ptr not in d:
                new = Node(ptr.val)
                d[ptr] = new
            else:
                new = d[ptr]
            if ptr.next not in d:
                d[ptr.next] = Node(ptr.next.val)
            new.next = d[ptr.next]
            if ptr.random not in d:
                d[ptr.random] = Node(ptr.random.val)
            new.random = d[ptr.random]
            ptr = ptr.next
        return d[head]