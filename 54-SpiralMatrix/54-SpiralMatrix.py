# Last updated: 7/26/2026, 3:53:35 PM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []

        while matrix:
            # step 1
            ret += matrix.pop(0)

            # step 2
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())

            # step 3
            if matrix:
                ret += matrix.pop()[::-1]

            # step 4
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        
        return ret