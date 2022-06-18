# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.d = set()
        root.val = 0
        q = [root]
        while q:
            tem = []
            for i in q:
                self.d.add(i.val)
                if i.left:
                    i.left.val = i.val * 2 + 1
                    tem.append(i.left)
                if i.right:
                    i.right.val = i.val * 2 + 2
                    tem.append(i.right)
            q = tem

    def find(self, target: int) -> bool:
        return target in self.d

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)