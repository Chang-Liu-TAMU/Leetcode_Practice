class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        s = set(leftChild) | set(rightChild)
        if -1 in s:
            s.remove(-1)
        if len(s) != n - 1:
            return False

        root = (set(range(n)) - s).pop()
        q = [root]
        seen = set()
        while q:
            tem = []
            for i in q:
                if i in seen:
                    return False
                seen.add(i)
                if leftChild[i] != -1:
                    tem.append(leftChild[i])
                if rightChild[i] != -1:
                    tem.append(rightChild[i])
            q = tem
        return len(seen) == n