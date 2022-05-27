# @Time: 2022/5/26 13:24
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-863-latest-all-nodes-distance-k-in-binary-tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(child, father):
            if child:
                child.father = father
                dfs(child.left, child)
                dfs(child.right, child)
        dfs(root, None)
        seen = set()
        seen.add(target)
        seen.add(None)
        q = [target]
        dis = 0
        while q:
            if not q:
                break
            if dis == k:
                return [x.val for x in q]
            tem = []
            for node in q:
                for v in ["left", "right", "father"]:
                    candi = node.__dict__[v]
                    if candi not in seen:
                        seen.add(candi)
                        tem.append(candi)
            q = tem
            dis += 1
        return []