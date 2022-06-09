# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # def dfs(root):
        #     if not root:
        #         return [], 0
        #     l1, candi1 = dfs(root.left)
        #     l2, candi2 = dfs(root.right)
        #     ans = 0
        #     if not l1 and not l2:
        #         return [root.val], 0
        #     else:
        #         l1.extend(l2)
        #         for i in l1:
        #             ans = max(ans, abs(i - root.val))
        #     ans = max(ans, candi1, candi2)
        #     l1.append(root.val)
        #     return l1, ans
        # return dfs(root)[1]
        
        #O(n) to merge
        #O(n) to find largest
        #(
        self.ans = 0
        def help(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]

            l, r = help(root.left), help(root.right)
            res = []
            while l and r:
                if l[-1] >= r[-1]:
                    res.append(l.pop())
                else:
                    res.append(r.pop())
            if l:
                res.extend(l[::-1])
            if r:
                res.extend(r[::-1])
            res.reverse()
            self.ans = max(self.ans, abs(res[0]-root.val), abs(res[-1]-root.val))
            bisect.insort(res, root.val)
            return res
        help(root)
        return self.ans