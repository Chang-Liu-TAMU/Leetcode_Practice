# @Time: 2022/5/13 16:50
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:dp-45-jump-game-II.py

class Solution:
    def jump(self, nums: List[int]) -> int:
        "refer to discuss board"
        j = 0
        memo = [0] * len(nums)
        for i in range(1, len(nums)):
            while j + nums[j] < i:
                j += 1
            memo[i] = memo[j] + 1
        return memo[-1]