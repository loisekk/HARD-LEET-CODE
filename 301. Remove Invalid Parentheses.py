from collections import deque
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def valid(x):
            count = 0
            for c in x:
                if c == '(': count += 1
                elif c == ')': count -= 1
                if count < 0: return False
            return count == 0

        q = deque([s])
        seen = {s}
        res = []
        found = False

        while q:
            cur = q.popleft()

            if valid(cur):
                res.append(cur)
                found = True

            if found:
                continue

            for i in range(len(cur)):
                if cur[i] in '()':
                    nxt = cur[:i] + cur[i+1:]
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append(nxt)

        return res