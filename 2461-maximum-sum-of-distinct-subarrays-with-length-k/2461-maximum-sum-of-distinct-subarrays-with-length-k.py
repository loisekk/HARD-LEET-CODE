
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        max_sum = 0
        window_sum = 0
        seen = set()
        left = 0

        for right in range(len(nums)):
            # Remove duplicates from the window
            while nums[right] in seen:
                seen.remove(nums[left])
                window_sum -= nums[left]
                left += 1

            # Add current element
            seen.add(nums[right])
            window_sum += nums[right]

            # Keep window size at most k
            if right - left + 1 > k:
                seen.remove(nums[left])
                window_sum -= nums[left]
                left += 1

            # Check valid window
            if right - left + 1 == k:
                max_sum = max(max_sum, window_sum)

        return max_sum
