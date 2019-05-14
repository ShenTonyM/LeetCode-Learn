from collections import deque
class Solution:
    def updateMatrix(self, matrix):
        if not len(matrix) or not len(matrix[0]):
            return None

        nrows, ncols = len(matrix), len(matrix[0])

        res = [[0] * ncols for i in range(nrows)]

        queue = deque()

        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))
                else:
                    res[i][j] = float('inf')

        directions = [[-1, 0],[0, 1], [1, 0], [0, -1]]

        while queue:
            cell = queue.popleft()
            for  direct in directions:
                i, j = cell[0] + direct[0], cell[1] + direct[1]
                if not 0 <= i < nrows or not 0 <= j < ncols or res[i][j] <= res[cell[0]][cell[1]] + 1:
                    continue

                res[i][j] = res[cell[0]][cell[1]] + 1
                queue.append((i, j))

        return res



if __name__ == '__main__':
    print(Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))

