class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [] # using it LIFO operation
        result = 0
        sign = 1
        num = 0

        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            elif i == "+":
                result += sign * num
                sign = 1
                num = 0
            elif i == "-":
                result += sign*num
                sign = -1
                num = 0
            elif i == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif i ==")":
                result += sign* num
                num = 0
                result *= stack.pop()
                result  += stack.pop()
        return result + sign *num