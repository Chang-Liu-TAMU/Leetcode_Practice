class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums.pop()

        if len(nums) == 2:
            return max(nums)

        memo = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            res = max(memo[i - 2] + nums[i], memo[i - 1])
            memo.append(res)
        return memo[-1]