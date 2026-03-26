class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", 
                    "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", 
                    "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
                    "Seventeen", "Eighteen", "Nineteen"]

        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", 
                "Sixty", "Seventy", "Eighty", "Ninety"]

        thousands = ["", "Thousand", "Million", "Billion"]

        # num under 1000
        def eng(i):
            res = ""
            if i >= 100:
                res += below_20[i // 100] + " Hundred "
                i%= 100
            if i >= 20:
                res += tens[i// 10] + " "
                i %= 10
            if i > 0:
                res += below_20[i] + " "
            return res

        res = ""
        j = 0

        while num > 0:
            if num % 1000 != 0:
                res = eng(num % 1000) + thousands[j] + " " + res
            num //= 1000
            j += 1

        return res.strip()