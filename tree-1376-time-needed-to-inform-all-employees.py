from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = defaultdict(list)
        for i, j in enumerate(manager):
            tree[j].append(i)

        self.ans = 0

        def dfs(id_, payload):
            if id_ not in tree:
                self.ans = max(self.ans, payload)
            else:
                for i in tree[id_]:
                    dfs(i, payload + informTime[id_])

        dfs(headID, 0)
        return self.ans