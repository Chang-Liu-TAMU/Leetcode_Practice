# @Time: 2022/4/28 20:03
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-116-populate-next-right-pointers-in-each-node.py
'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:


struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''




"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = [root]
        while q:
            tem = []
            for i in range(len(q) - 1):
                q[i].next = q[i + 1]
                if q[i].left:
                    tem.append(q[i].left)
                if q[i].right:
                    tem.append(q[i].right)
            q[-1].next = None
            if q[-1].left:
                tem.append(q[-1].left)
            if q[-1].right:
                tem.append(q[-1].right)

            q = tem
        return root