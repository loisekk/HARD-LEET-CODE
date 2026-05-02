class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows = len(matrix)
        node = matrix
        visit = set()
        # def dfs(i , j ):
        #     if (i < 0 or j < 0 or i >= rows or j>= cols or matrix[i][j] == '0' or (i,j) in visit ):
        #       return 0 
        #     visit.add((i,j))
        #     return ( 1 + dfs(i+1 , j) + dfs(i-1 , j) + 
        #             dfs(i,j+1) + dfs(i,j-1))
        #     max_area = 0
        #     for i in range(rows):
        #         for j in range(cols):
        #             if matrix[i][j] == '1' and (i,j) not in visit:
        #                 max_area = max(max_area , dfs(i,j))
        #     return max_area
        ''' 2nd approach '''
        # def dfs(i , j , rows ,cols,  node  , visit):
        #     for i in rows:
        #         for j in cols:
        #             if (i < 0 and j < 0 and matrix(i,j) == '0' and (i,j) in visit):
        #                 return 0
        #             elif (i>0 and j>0 andi < len(matrix) and j < len(matrix[0]) and
        #                   matrix(i,j) == '1' and (i,j) not in visit):
        #                 node = matrix[i][j]
        #     dfs(i+1 , j)
        #     dfs(i-1 , j)
        #     dfs(i , j+1)
        #     dfs(i , j-1)
        #     max_area = 0
        #     count = 0
        #     for n in matrix:
        #         for j in matrix[0]:
        #             if matrix[i][j] == '1' and (i,j) not in vist:
        #                 area  = dfs(i,j)
        #                 if area > max_area:
        #                     count =1
        #                 elif area == max_area:
        #                     count += 1
        #     return count

        '''3rd approach '''

        if not  matrix:
            return 0
        cols = len(matrix[0])
        heights = [0] * (cols+1)
        max_area = 0 
        for rows in matrix:
            for i in range(cols):
                if rows[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0 
            stack = [-1]
            for i in range(cols + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area , h *w)
                stack.append(i)
        return max_area
