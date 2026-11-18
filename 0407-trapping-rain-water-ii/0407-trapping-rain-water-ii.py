class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        import heapq
        if not heightMap or not heightMap[0]:
            return 0 
        heap = []
        m , n= len(heightMap) , len(heightMap[0])
        visited= [[False] * n for _ in range(m)  ] 

        for i in range(m):
            for j in (0, n - 1):
                if not visited[i][j]:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        for j in range(n):
            for i in (0, m - 1):
                if not visited[i][j]:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        water = 0 
        dire = [(0,1) , (0,-1) , (1,0) , (-1,0)] 
        while heap:
            height , x , y  = heapq.heappop(heap)
            for dx , dy in dire:
                nx , ny = x + dx , y+dy
                if 0 <= nx < m  and 0<ny < n:
                    if not visited[nx][ny]:
                        visited[nx][ny]  = True

                        neigh = heightMap[nx][ny]  
                        water += max(0 , height - neigh)
                        heapq.heappush(heap , (max(height , neigh), nx , ny))
        return water