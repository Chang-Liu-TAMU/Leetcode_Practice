# class Node:
#     def __init__(self, name=None, forward=None, backward=None):
#         self.name = name
#         self.forward = forward
#         self.backward = backward

# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.ptr = Node(homepage)

#     def visit(self, url: str) -> None:
#         new = Node(url, backward=self.ptr)
#         if self.ptr.forward:
#             self.ptr.forward.backward = None
#         self.ptr.forward = new
#         self.ptr = new

#     def back(self, steps: int) -> str:
#         for _ in range(steps):
#             if not self.ptr.backward:
#                 break
#             self.ptr = self.ptr.backward
#         return self.ptr.name

#     def forward(self, steps: int) -> str:
#         for _ in range(steps):
#             if not self.ptr.forward:
#                 break
#             self.ptr = self.ptr.forward
#         return self.ptr.name

class BrowserHistory:

    def __init__(self, homepage: str):
        self.d = {1: homepage}
        self.limit = 1
        self.ptr = 1

    def visit(self, url: str) -> None:
        self.ptr += 1
        self.d[self.ptr] = url
        self.limit = self.ptr

    def back(self, steps: int) -> str:
        self.ptr -= steps
        if self.ptr <= 0:
            self.ptr = 1
            return self.d[1]
        return self.d[self.ptr]

    def forward(self, steps: int) -> str:
        self.ptr += steps
        if self.ptr > self.limit:
            self.ptr = self.limit
            return self.d[self.limit]
        return self.d[self.ptr]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)