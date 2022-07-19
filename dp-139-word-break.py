class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dp(i, memo):
            if i not in memo and not self.flag:
                if i == len(s):
                    self.flag = True
                    return
                for w in wordDict:
                    if s[i:].startswith(w):
                        dp(i+len(w), memo)
                        if self.flag:
                            return
                memo.add(i)
        self.flag = False
        dp(0, set())
        return self.flag