class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dp(s1, s2, s3, i, j, k, mode, memo):
            if self.flag:
                return True
            if not mode:
                return dp(s1, s2, s3, i, j, k, "123", memo) or dp(s1, s2, s3, i, j, k, "12", memo)
            if (i, j, mode) in memo:
                return False
            elif mode == "121":
                ans = []
                for x in range(i + 2):
                    if s1[i - x:i + 1] == s3[k - x:k + 1]:
                        ans.append(dp(s1, s2, s3, i - x - 1, j, k - x - 1, "12", memo))
                    else:
                        break
                if not any(ans):
                    memo.add((i, j, mode))
                    return False
                else:
                    return True
            else:
                if s1[:i + 1] + s2[:j + 1] == s3[:k + 1]:
                    self.flag = True
                    return True
                ans = []
                for x in range(j + 2):
                    if s2[j - x:j + 1] == s3[k - x:k + 1]:
                        ans.append(dp(s1, s2, s3, i, j - x - 1, k - x - 1, "121", memo))
                    else:
                        break
                if not any(ans):
                    memo.add((i, j, mode))
                    return False
                else:
                    return True

        self.flag = False
        if len(s1) + len(s2) != len(s3):
            return False
        if s1 + s2 == s3 or s2 + s1 == s3:
            return True
        return dp(s1, s2, s3, len(s1) - 1, len(s2) - 1, len(s3) - 1, None, set()) or \
               dp(s2, s1, s3, len(s2) - 1, len(s1) - 1, len(s3) - 1, None, set())
