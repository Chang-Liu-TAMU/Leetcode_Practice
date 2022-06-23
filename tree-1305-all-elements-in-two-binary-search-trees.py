# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def gen(root):
            if root:
                yield from gen(root.left)
                yield root.val
                yield from gen(root.right)

        g1 = gen(root1)
        g2 = gen(root2)
        ans = []
        a, b = next(g1, None), next(g2, None)
        while True:
            if a is None and b is None:
                return ans
            elif a is None:
                ans.append(b)
                ans.extend(list(g2))
                return ans
            elif b is None:
                ans.append(a)
                ans.extend(list(g1))
                return ans
            else:
                if a <= b:
                    ans.append(a)
                    a = next(g1, None)
                else:
                    ans.append(b)
                    b = next(g2, None)