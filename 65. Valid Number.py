class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        digit = False
        dot = False
        exp = False

        for i , c in enumerate(s):
            if c.isdigit():
                digit = True
            elif c in ['+' ,'-']:
                if i > 0 and s[i-1] not in['e' ,'E']:
                    return False
            elif c == '.':
                if dot or exp:
                       return False
                dot = True

            elif c in ['e' , 'E']:
                if exp or not digit:
                    return False
                exp = True
                digit = False
            else:
                return False
        return digit