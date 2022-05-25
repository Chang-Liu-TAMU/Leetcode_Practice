# @Time: 2022/5/24 9:33
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-622-design-circular-queue.py

class Node:
    def __init__(self, val=None, next_=None, prev=None):
        self.val = val
        self.next = next_
        self.prev = prev


class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        for i in range(k):
            new = Node()
            if not self.head:
                self.head = self.tail = new
            else:
                self.tail.next = new
                new.prev = self.tail
                self.tail = new
        self.tail.next = self.head
        self.head.prev = self.tail
        self.tail = self.head

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.tail.val = value
            self.tail = self.tail.next
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = self.head.next
            self.head.prev.val = None
            return True
        else:
            return False

    def Front(self) -> int:
        return self.head.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.tail.prev.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.head.val is None

    def isFull(self) -> bool:
        return self.head.val is not None and self.head is self.tail

    # Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()