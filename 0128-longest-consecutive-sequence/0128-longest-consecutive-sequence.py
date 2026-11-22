class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        #  nums = [100,4,200,1,3,2]
        #  nums = [1,2,3,4,100,200]
        nums.sort()
        # stack vs counter 
        count = 1
        longest = 1 
        for i in range(1, len(nums)):# start , stop , step 
          if nums[i] == nums[i-1] :
            continue
          elif nums[i] == nums[ i - 1] + 1 :
            count +=1 
            # nums[i] = 1
            # nums[i-1] = 1
            # nums[i-1] + 1 = 2 -> checker who check's if the element is greater or not 
          else:
            count = 1
          longest = max(longest , count)
        return longest 