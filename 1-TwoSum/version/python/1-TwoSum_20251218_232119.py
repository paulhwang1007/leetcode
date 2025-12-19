# Last updated: 12/18/2025, 11:21:19 PM
1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        ret = []
4
5        while matrix:
6            # step 1
7            ret += matrix.pop(0)
8
9            # step 2
10            if matrix and matrix[0]:
11                for row in matrix:
12                    ret.append(row.pop())
13
14            # step 3
15            if matrix:
16                ret += matrix.pop()[::-1]
17
18            # step 4
19            if matrix and matrix[0]:
20                for row in matrix[::-1]:
21                    ret.append(row.pop(0))
22        
23        return ret