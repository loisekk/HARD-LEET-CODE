class Solution(object):
    def isMatch(self, s, p):
        
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            first_match = (i < len(s) and (p[j] == s[i] or p[j] == '.'))
            if j + 1 < len(p) and p[j + 1] == '*':
                ans = (
                    dfs(i, j + 2) or              # skip
                    (first_match and dfs(i + 1, j))  # use
                )
            else:
                ans = first_match and dfs(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dfs(0, 0)
