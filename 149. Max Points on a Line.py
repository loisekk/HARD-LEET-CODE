class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        if len(points) <= 2:
            return len(points)
        res = 2
        for i in range(len(points)):
            slopes = defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue

                dy = points[j][1] - points[i][1]
                dx = points[j][0] - points[i][0]
                g = gcd(abs(dy), abs(dx))
                if g != 0:
                    dy //= g
                    dx //= g

                slopes[(dy, dx)] += 1
                res = max(res, slopes[(dy, dx)] + 1)
            return res    