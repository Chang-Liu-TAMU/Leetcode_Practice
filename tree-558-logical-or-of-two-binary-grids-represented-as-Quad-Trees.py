# @Time: 2022/5/23 11:55
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-558-logical-or-of-two-binary-grids-represented-as-Quad-Trees.py


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def divide(self, leaf):
        leaf.topLeft = Node(leaf.val, leaf.isLeaf, None, None, None, None)
        leaf.topRight = Node(leaf.val, leaf.isLeaf, None, None, None, None)
        leaf.bottomLeft = Node(leaf.val, leaf.isLeaf, None, None, None, None)
        leaf.bottomRight = Node(leaf.val, leaf.isLeaf, None, None, None, None)

    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        a, b = quadTree1, quadTree2
        if a.isLeaf and b.isLeaf:
            if a.val != b.val:
                a.val = 1
            return a
        else:
            if a.isLeaf:
                self.divide(a)
            if b.isLeaf:
                self.divide(b)
            l = []
            name = ["topLeft", "topRight", "bottomLeft", "bottomRight"]
            for n in name:
                l.append(self.intersect(a.__dict__[n], b.__dict__[n]))
            if all(i.isLeaf for i in l) and (not any(i.val for i in l) or all(i.val for i in l)):
                return Node(l[0].val, 1, None, None, None, None)
            else:
                root = Node(1, 0, *l)
                return root