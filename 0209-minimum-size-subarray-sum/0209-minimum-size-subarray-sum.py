class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        total = 0
        ans = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans