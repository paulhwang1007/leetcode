# Last updated: 12/19/2025, 9:57:52 AM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid:
4            return 0
5        
6        rows, cols = len(grid), len(grid[0])
7        visit = set()
8        islands = 0
9
10        def bfs(r, c):
11            q = collections.deque()
12            visit.add((r, c))
13            q.append((r, c))
14            
15            while q:
16                row, col = q.popleft()
17                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
18
19                for dr, dc in directions:
20                    r, c = row + dr, col + dc
21                    if ((r) in range(rows) and 
22                        (c) in range(cols) and
23                        grid[r][c] == "1" and
24                        (r, c) not in visit):
25                        q.append((r, c))
26                        visit.add((r, c))
27
28        for r in range(rows):
29            for c in range(cols):
30                if grid[r][c] == "1" and (r, c) not in visit:
31                    bfs(r, c)
32                    islands += 1
33        return islands