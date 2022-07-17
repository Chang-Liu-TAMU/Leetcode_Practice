# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        trees = {}
        childs = set()
        for p, c, isleft in descriptions:
            childs.add(c)
            if p not in trees:
                trees[p] = TreeNode(p)
            if c not in trees:
                trees[c] = TreeNode(c)
            if isleft:
                trees[p].left = trees[c]
            else:
                trees[p].right = trees[c]
        root = trees.keys() - childs
        assert len(root) == 1
        root = root.pop()
        return trees[root]