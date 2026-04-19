class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        wordset = set(wordDict)

        def backtrack(start, path):
            # If we reached end ->  valid sentence
            if start == len(s):
                res.append(" ".join(path)) # merge list and str
                return

            # Try every possible word
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in word_set:
                    path.append(word)          # choose
                    backtrack(end, path)       # explore
                    path.pop()                 # un-choose

        backtrack(0, [])
        return res