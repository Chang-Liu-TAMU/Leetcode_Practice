class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = math.floor(math.log(label, 2)) + 1
        def conversion(level, num):
            if level % 2 == 1:
                return num
            lo = 2 ** (level-1)
            hi = lo * 2 - 1
            return lo + hi - num
        label = conversion(level, label)
        ans = []
        odd = level % 2
        print(level)
        while label != 1:
            if odd:
                ans.append(label)
            else:
                ans.append(conversion(level, label))
            odd = 1 - odd
            level -= 1
            label = label // 2
        ans.append(1)
        return reversed(ans)