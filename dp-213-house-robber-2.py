# @Time: 2022/4/25 14:35
# @Author: chang liu
# @Email: chang_liu_tamu@gmail.com
# @File:dp-213-house-robber-2.py
from typing import List

'''
description:

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
 All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
 Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two 
 adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can 
rob tonight without alerting the police.

****************************************************************
example:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

****************************************************************
tags:
    dynamic programming


'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(start, end):
            d = end - start + 1
            if d == 2:
                return max(nums[start:end + 1])

            a, b = nums[start], max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                c = max(a + nums[i], b)
                a, b = b, c
            return b

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        return max(house_robber(0, len(nums) - 2), house_robber(1, len(nums) - 1))