# @Time: 2022/5/10 9:17
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:dp-22-generate-parentheses.py


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.ans = []

        def g(x, y, path):
            if x < y or x > self.n or y > self.n:
                return
            if x == self.n and y == self.n:
                self.ans.append("".join(path))
                return
            path.append("(")
            g(x + 1, y, path)
            path.pop()

            path.append(")")
            g(x, y + 1, path)
            path.pop()

        g(0, 0, [])
        return self.ans