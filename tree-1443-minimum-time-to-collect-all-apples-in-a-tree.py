from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        trees = defaultdict(list)
        for i, j in edges:
            trees[i].append(j)
            trees[j].append(i)

        self.ans = 0

        def dfs(i, seen):
            seen.add(i)
            l = []
            for child in trees[i]:
                if child not in seen:
                    tem = dfs(child, seen)
                    if tem:
                        self.ans += 1
                    l.append(tem)
            l.append(hasApple[i])
            return any(l)

        dfs(0, set())
        return self.ans * 2