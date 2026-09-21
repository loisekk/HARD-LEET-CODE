class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """   
        lar = 0
        lar_1 = []
        for i , height in enumerate(heights + [0]):
         st = i 
         while lar_1 and lar_1[-1][-1] > height:
            index , previous_height = lar_1.pop()
            lar = max(lar , previous_height * (i - index))
            st = index 
         lar_1.append((st , height))
        return lar