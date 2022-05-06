# @Time: 2022/5/1 19:40
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-173-binary-search-tree-iterator.py
'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor.
The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.g = self.gen(root)
        self.cache = next(self.g)

    def gen(self, root):
        if root.left:
            yield from self.gen(root.left)
        yield root.val
        if root.right:
            yield from self.gen(root.right)

    def next(self) -> int:
        ans = self.cache
        try:
            self.cache = next(self.g)
        except:
            self.cache = None
        return ans

    def hasNext(self) -> bool:
        if self.cache is not None:
            return True