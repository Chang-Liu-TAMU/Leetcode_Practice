from collections import defaultdict


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        trees = defaultdict(list)
        for i, j in edges:
            trees[i].append(j)
            trees[j].append(i)

        self.ans = [1] * n

        def dfs(root, seen):
            tem = []
            for neig in trees[root]:
                if neig not in seen:
                    seen.add(neig)
                    tem.append(dfs(neig, seen))
            ans = Counter([labels[root]])
            for i in tem:
                ans += i
            self.ans[root] = ans[labels[root]]
            return ans

        dfs(0, set([0]))
        return self.ans