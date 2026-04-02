class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        max_num = 10**n -1
        min_num = 10*(n  -1)
        for i in range(max_num , min_num - 1 ,-1):
           pal = int(str(i) + str(i)[::-1])

           for j in range(max_num ,int(pal**0.5) -1 , -1):
            if pal % j == 0:
                if min_num <= pal // j <= max_num:
                    return pal % 1337
        return -1