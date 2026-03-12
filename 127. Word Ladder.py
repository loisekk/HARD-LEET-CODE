class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        queue = deque([(beginWord, 1)])

        while queue:
            word, level = queue.popleft()

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i+1:]

                    if new_word == endWord:
                        return level + 1
                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        queue.append((new_word, level + 1))
        return 0