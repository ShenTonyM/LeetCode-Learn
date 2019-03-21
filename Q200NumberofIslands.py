class Solution1(object):

    def point_judge(self, posi, grid, visited, island):
        height, width = len(grid), len(grid[0])
        i, j = posi[0], posi[1]
        if 0 <= i < height and 0 <= j < width and not visited[i][j] and grid[i][j] == "1":
            visited[i][j] = True
            island.append((i, j))

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        height, width = len(grid), len(grid[0])

        res = 0
        visited = [[False for j in range(width)] for i in range(height)]

        for i in range(height):
            for j in range(width):
                if not visited[i][j] and grid[i][j] == "1":
                    visited[i][j] = True

                    island = []
                    island.append((i, j))
                    while island:
                        (tempi, tempj) = island.pop()

                        self.point_judge((tempi - 1, tempj), grid, visited, island)
                        self.point_judge((tempi, tempj - 1), grid, visited, island)
                        self.point_judge((tempi + 1, tempj), grid, visited, island)
                        self.point_judge((tempi, tempj + 1), grid, visited, island)

                    res += 1
                else:
                    continue

        return res


class Solution2(object):
    # todo: use union find method to solve the problem
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        pass



if __name__ == '__main__':
    print(Solution1().numIslands([["1","1","0","0","0"],
                                 ["1","1","0","0","0"],
                                 ["0","0","1","0","0"],
                                 ["0","0","0","1","1"]]))