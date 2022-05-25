# @Time: 2022/5/21 10:07
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-707-design-linked-list.

class Node:
    def __init__(self, val=None, next_=None, prev=None):
        self.val = val
        self.next = next_
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.c = 0

    def __getitem__(self, index):
        ptr = self.head
        n = -1
        while n != index:
            n += 1
            ptr = ptr.next
        return ptr

    def get(self, index: int) -> int:
        if 0 <= index < self.c:
            return self[index].val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.update(-1, val, "add")

    def addAtTail(self, val: int) -> None:
        self.update(self.c - 1, val, "add")

    def addAtIndex(self, index: int, val: int) -> None:
        self.update(index - 1, val, "add")

    def deleteAtIndex(self, index: int) -> None:
        self.update(index, None, "delete")

    def update(self, index, val, mode):
        if mode == "delete":
            if 0 <= index < self.c:
                ptr = self[index]
                self.c -= 1
                x, y = ptr.prev, ptr.next
                x.next = y
                y.prev = x
        elif mode == "add":
            if -1 <= index <= self.c - 1:
                ptr = self[index]
                self.c += 1
                new = Node(val)
                n = ptr.next
                ptr.next = new
                new.prev = ptr
                new.next = n
                n.prev = new

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)