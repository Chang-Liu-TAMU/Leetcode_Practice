class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lmin = lmax = ans = nums[0]
        for i in range(1, len(nums)):
            v = nums[i]
            l = [v, lmin * v, lmax * v]
            lmin = min(l)
            lmax = max(l)
            ans = max(ans, lmax)

        return ans