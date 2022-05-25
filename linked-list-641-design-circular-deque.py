# @Time: 2022/5/22 13:53
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:linked-list-641-design-circular-deque.py


class Node:
    def __init__(self, val=None, next_=None, prev=None):
        self.val = val
        self.next = next_
        self.prev = prev


class MyCircularDeque:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        for i in range(k):
            new = Node()
            if not self.head:
                self.head = new
                self.tail = new
                self.head.next = self.tail
                self.tail.prev = self.head
            else:
                self.tail.next = new
                new.prev = self.tail
                self.tail = new
        self.tail.next = self.head
        self.head.prev = self.tail
        self.tail = self.head

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.head = self.head.prev
            self.head.val = value
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.tail.val = value
            self.tail = self.tail.next
            # print(f"head is tail ? {self.head is self.tail}")
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            tem = self.head
            self.head = self.head.next
            tem.val = None
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            tem = self.tail.prev
            tem.val = None
            self.tail = tem
            return True
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            # make sure self.isEmpty is called
            # lapse: if not self.isEmpty -->> always evaluated to True
            return self.head.val
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.tail.prev.val
        else:
            return -1

    def isEmpty(self) -> bool:
        return (self.head is self.tail) and (self.head.val is None)

    def isFull(self) -> bool:
        return (self.head is self.tail) and (self.head.val is not None)

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()