from collections import Counter

class A:
    def __init__(self):
        self.show()

    def show(self):
        print("I am A")

class B(A):
    def __init__(self):
        super().__init__()

    def show(self):
        print("I am B")


b = B()