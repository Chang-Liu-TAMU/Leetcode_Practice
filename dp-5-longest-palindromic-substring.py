# @Time: 2022/5/9 21:59
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:dp-5-longest-palindromic-substring.py

class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = [[True] * len(s) for _ in range(len(s))]
        ans = 1
        res = s[0]
        for i in range(len(s) - 1):
            y = i + 1
            for x in range(len(s) - i - 1):
                ii = x + 1
                jj = y - 1
                tem = m[ii][jj] and s[x] == s[y]
                if tem:
                    m[x][y] = True
                    c = y - x + 1
                    if c > ans:
                        ans = c
                        res = s[x:y + 1]
                else:
                    m[x][y] = False
                y += 1
        return res
