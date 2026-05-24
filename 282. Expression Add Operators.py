class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result = []
        def backtrack(index, path, value, prev):
            if index == len(num):
                if value == target:
                    result.append(path)
                return
            # Creating   nums from substring
            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break
                curr_str = num[index:i + 1]
                curr = int(curr_str)

                if index == 0:
                    backtrack(i + 1,curr_str,curr,curr)
                else:
                    backtrack(i + 1,path + "+" + curr_str,value + curr,curr)
                    backtrack(i + 1,path + "-" + curr_str,value - curr,-curr)
                    backtrack(i + 1,path + "*" + curr_str,value - prev + (prev * curr),prev * curr)
        backtrack(0, "", 0, 0)
        return result