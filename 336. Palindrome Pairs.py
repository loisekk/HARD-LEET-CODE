class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_map = {word: i for i, word in enumerate(words)}
        res = []

        def is_palindrome(s):
            return s == s[::-1]

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]

                #  prefix is palindrome
                if is_palindrome(prefix):
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_map and word_map[rev_suffix] != i:
                        res.append([word_map[rev_suffix], i])

                # suffix is palindrome
                # using the j != for len(word) to avoid duplicates
                if j != len(word) and is_palindrome(suffix):
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_map and word_map[rev_prefix] != i:
                        res.append([i, word_map[rev_prefix]])

        return res