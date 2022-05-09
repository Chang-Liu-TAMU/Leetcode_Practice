# @Time: 2022/5/9 21:18
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:tree-449-serialize-deserialize-BST.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """

        def traverse(root, l, style):
            if root:
                if style == "in":
                    traverse(root.left, l, style)
                    l.append(root.val)
                    traverse(root.right, l, style)
                elif style == "pre":
                    l.append(root.val)
                    traverse(root.left, l, style)
                    traverse(root.right, l, style)

        inorder = []
        preorder = []
        traverse(root, inorder, "in")
        traverse(root, preorder, "pre")
        return "$".join((str(x) for x in preorder)) + "&" + "$".join((str(x) for x in inorder))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        preorder, inorder = data.split("&")
        preorder = preorder.split("$")
        inorder = inorder.split("$")
        if not inorder[0]:
            return None

        def construct(i, j, p, q):
            nonlocal preorder, inorder
            if i > j:
                return None
            h = preorder[i]
            m = inorder.index(h)
            left = construct(i + 1, i + m - p, p, m - 1)
            right = construct(i + m - p + 1, j, m + 1, q)
            root = TreeNode(int(h))
            root.left = left
            root.right = right
            return root

        return construct(0, len(preorder) - 1, 0, len(inorder) - 1)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans