# @Time: 2022/5/7 14:41
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-146-LRU-cache.py


class Node:
    def __init__(self, key=None, val=None, front=None, back=None):
        self.key = key
        self.val = val
        self.front = front
        self.back = back


class DLL:
    def __init__(self):
        self.head = Node("head")
        self.tail = Node("tail")
        self.head.back = self.tail
        self.tail.front = self.head

    def insert_at_head(self, node):
        node.front = self.head
        tem = self.head.back
        self.head.back = node
        node.back = tem
        tem.front = node

    def delete_node(self, node):
        node.front.back = node.back
        node.back.front = node.front

    def delete_tail(self, d):
        node = self.tail.front
        self.delete_node(node)
        del d[node.key]


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.occupied = 0
        self.dll = DLL()
        self.d = {}
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.d:
            val = self.d[key].val
            self.update(key, val)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.update(key, value)
        else:
            new = Node(key, value)
            self.d[key] = new
            self.dll.insert_at_head(new)
            if self.count == self.capacity:
                self.dll.delete_tail(self.d)
            else:
                self.count += 1

    def update(self, key, val):
        self.d[key].val = val
        self.dll.delete_node(self.d[key])
        self.dll.insert_at_head(self.d[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)