class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def pick(nums , k):
            stack = []
            remove = len(nums) - k

            for num in nums:
                while stack and remove > 0 and stack[-1] < num:
                    stack.pop()
                    remove -=1
                stack.append(num)
            return stack[:k]
        
        def merge(a,b):
            res = []
            while a or b:
                if a > b:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            return res
        best= []

        for i in range(k +1):
            if i <= len(nums1) and (k-i) <= len(nums2):
                part1 = pick(nums1 , i)
                part2 = pick(nums2 , k-i)
                new  = merge(part1[:] , part2[:])
                best  = max (best , new)
        return best