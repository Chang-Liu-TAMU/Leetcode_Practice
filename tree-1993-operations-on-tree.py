from collections import defaultdict


class LockingTree:

    def __init__(self, parent: List[int]):
        self.tree = parent
        self.db = defaultdict(set)
        self.locks = defaultdict(type(None))

    def update(self, num, mode):
        p = self.tree[num]
        while p != -1:
            if mode == "add":
                self.db[p].add(num)
            elif mode == "remove":
                self.db[p].remove(num)
            p = self.tree[p]

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] is None:
            self.locks[num] = user
            self.update(num, "add")
            return True
        else:
            return False

    def unlock(self, num: int, user: int) -> bool:
        if (self.locks[num] == user) or (user == -1):
            self.locks[num] = None
            self.update(num, "remove")
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool:
        if self.locks[num] is None and self.db[num]:
            n = self.tree[num]
            flag = True
            while n != -1:
                if self.locks[n] is not None:
                    flag = False
                    break
                n = self.tree[n]
            if flag:
                for locked in list(self.db[num]):
                    self.unlock(locked, -1)
                self.lock(num, user)
                return True
            else:
                return False

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)

################################################