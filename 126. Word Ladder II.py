class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(set)
        layer = {beginWord}
        found = False

        while layer and not found:
            wordSet -= layer
            next_layer = set()
            for word in layer:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            next_layer.add(new_word)
                            parents[new_word].add(word)
                            if new_word == endWord:
                                found = True
            layer = next_layer

        if not found:
            return []

        # DFS backtrack
        res = []
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for parent in parents[word]:
                dfs(parent, path + [parent])

        dfs(endWord, [endWord])
        return res 