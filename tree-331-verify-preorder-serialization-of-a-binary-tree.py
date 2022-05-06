# @Time: 2022/5/6 15:47
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-331-verify-preorder-serialization-of-a-binary-tree.py

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        self.ptr = 0

        def dfs(l):
            if self.ptr >= len(l) or l[self.ptr] == "#":
                self.ptr += 1
                return
            self.ptr += 1
            dfs(l)
            dfs(l)

        l = preorder.split(",")
        dfs(l)
        return self.ptr == len(l)