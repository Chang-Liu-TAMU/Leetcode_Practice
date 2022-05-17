# @Time: 2022/5/17 13:42
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:dp-55-jump-game.py

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        greedy

        refer to discussion board
        """

        g = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= g:
                g = i
        return g == 0
