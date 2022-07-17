# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(root, path):
            if root:
                if root.val == startValue:
                    self.start = list(path)
                if root.val == destValue:
                    self.dest = list(path)
                path.append("L")
                dfs(root.left, path)
                path.pop()

                path.append("R")
                dfs(root.right, path)
                path.pop()

        dfs(root, [])
        i = 0
        print(self.start)
        print(self.dest)
        for i in range(max(len(self.start), len(self.dest))):
            if i >= len(self.start) or i >= len(self.dest):
                break
            if self.start[i] != self.dest[i]:
                break
        ans = ["U"] * (len(self.start) - i) + self.dest[i:]
        return "".join(ans)