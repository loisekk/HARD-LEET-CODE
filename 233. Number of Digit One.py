class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        pos = 1
        while pos <= n:
            lower = n % pos
            current = (n // pos) % 10
            higher = n // (pos * 10)

            if current == 0:
                count += higher * pos
            elif current == 1:
                count += higher * pos + (lower + 1)
            else:
                count += (higher + 1) * pos
            pos *= 10

        return count