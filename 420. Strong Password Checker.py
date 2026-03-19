class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        n = len(password)

        lower_case = any(c.islower() for c in password)
        upper_case = any(c.isupper() for c in password)
        digit = any(c.isdigit() for c in password)

        missing = 3 - (lower_case + upper_case + digit)
        # remove the occurences
        replace = 0
        one = two = 0 # pos
        i = 2
        chars = list(password)

        while i < n:
            if chars[i] == chars[i-1] == chars[i-2]:
                length = 2 # cutoff the len
                while i < n  and chars[i] == chars[i-1]:
                    length +=1
                    i +=1
                replace += length //3 # for 3 occurences

                if length  % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two +=1
            else:
                    i +=1
        if i < 6:
            return max(missing , 6 - n)
        elif n <= 20 :
            return max(missing , replace)
        delete = n - 20
        replace -= min(delete, one)
        replace -= min(max(delete - one, 0) // 2, two)
        replace -= max(delete - one - 2*two, 0) // 3

        return delete + max(missing, replace)