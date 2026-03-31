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

        n = len(points)
        if n <= 2:
            return n
        res = 0
        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 1   # count the point itself
            for j in range(i + 1, n):
                dy = points[j][1] - points[i][1]
                dx = points[j][0] - points[i][0]

                # ✅ duplicate point
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue
                g = gcd(abs(dy), abs(dx))
                if g != 0:
                    dy //= g
                    dx //= g

                # ✅ normalize slope
                if dx < 0:
                    dx *= -1
                    dy *= -1
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                slopes[(dy, dx)] += 1
            max_line = 0
            for count in slopes.values():
                max_line = max(max_line, count)
            res = max(res, max_line + duplicates)
        return res    
