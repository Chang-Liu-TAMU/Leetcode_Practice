class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        m = [[1]* (n+2) for _ in range(n+2)]
        self.ans = []
        def help(start, path, m, n, s):
            if start == n+1:
                self.ans.append(path[::])
            else:
                for i in range(start, n+1):
                    x, y = start-1, i-1
                    sign = s[x] == s[y] and m[start+1][i-1]
                    if not sign:
                        m[start][i] = 0
                    else:
                        path.append(s[x:y+1])
                        help(i+1, path, m, n, s)
                        path.pop()
        help(1, [], m, n, s)
        return self.ans