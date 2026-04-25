class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ''' 1st approach '''
        # pos = [(i,j) for i in range(len(board)) for j in range(len(board[i]))]
        # res = []
        # loc = []
        # def back_track(board , words , i , j):
        #     for l in pos:
        #         for m in pos[i]:
        #             wrd = [list(word) for word in words]
        #             for n in wrd : 
        #                 if pos[i,j] == wrd[n]:
        #                     loc +=  (i,j)
        #                     continue
        #                 elif pos[i,j] == len(pos[i,j] - 1): # element not found so we reached to the lastindex of pos
        #                     for o in range(len(pos) -1,- 1 ,-1): # back_Track
        #                         if pos[i,j] == wrd[n]:
        #                             loc += (i,j)
        #                             continue
        #                         else: 
        #                             break
        #                 else: # no condition for != cause we already reached to the last index because char not matched then we back_track to search the[ word == board ]
        #                     break
        #     combined = [''.join(char) for char in  loc]
        #     res = set(combined)
        # return res 

        ''' 2nd approach '''

        # res = set()
        # rows, cols = len(board), len(board[0])
        # def back_track(i , j , word , loc , chk ):
        #     if loc == len(word):
        #         res.add(word)
        #         return
        #     if (i<0 or j<0 or i>=rows or j>= cols or (i,j) in chk or board[i][j] != word[loc]):
        #         return
        #     # check mark
        #     chk.add((i,j))
        #     # for backtrack we have to check possible 4 dir 
        #     back_track(i+1, j, word, loc+1, chk)
        #     back_track(i-1, j, word, loc+1, chk)
        #     back_track(i, j+1, word, loc+1, chk)
        #     back_track(i, j-1, word, loc+1, chk)
        #      # all possible check direction if found stores the addres and return 
        #     chk.remove((i,j))
        # for word in words:
        #         for i in range(rows):
        #             for j in range(cols):
        #                 back_track(i,j,word,0,set())
        # return list(res)

        ''' 3rd approach '''
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["#"] = word   # end marker

        rows, cols = len(board), len(board[0])
        res = []
        def backtrack(i, j, node):
            char = board[i][j]
            if char not in node:
                return
    
            nxt = node[char]
            word = nxt.pop("#", None)
            if word:
                res.append(word)
            # mark visited
            board[i][j] = "*"
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] != "*":
                    backtrack(ni, nj, nxt)
            # restore
            board[i][j] = char
            # optimization: remove leaf node
            if not nxt:
                node.pop(char)
        for i in range(rows):
            for j in range(cols):
                backtrack(i, j, trie)
        return res