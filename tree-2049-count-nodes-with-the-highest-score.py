from collections import defaultdict


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tree = defaultdict(list)
        for child, parent in enumerate(parents):
            tree[parent].append(child)

        memo = {}

        def dfs(n):
            if n not in tree:
                memo[n] = 1
                return 1
            ans = 0
            for i in tree[n]:
                ans += dfs(i)
            ans += 1
            memo[n] = ans
            return ans

        dfs(0)
        assert len(memo) == len(parents)

        res = 0
        c = 0
        for i in range(len(parents)):
            tem = 1
            n = len(parents)
            for child in tree[i]:
                tem *= memo[child]
                n -= memo[child]
            n -= 1
            if n == 0:
                n = 1
            tem *= n
            print(tem)
            if res == tem:
                c += 1
            elif res < tem:
                res = max(res, tem)
                c = 1
        return c