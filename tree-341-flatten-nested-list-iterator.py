# @Time: 2022/5/7 15:35
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-341-flatten-nested-list-iterator.py

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.g = self.gen(nestedList)
        self.following = next(self.g, None)

    def next(self) -> int:
        ans = self.following
        self.following = next(self.g, None)
        print(ans)
        return ans

    def hasNext(self) -> bool:
        return self.following is not None

    def gen(self, l):
        for i in l:
            if i.isInteger():
                yield i.getInteger()
            else:
                yield from self.gen(i.getList())

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())