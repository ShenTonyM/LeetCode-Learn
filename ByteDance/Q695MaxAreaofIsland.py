class Solution:
    def maxAreaOfIsland(self, grid) -> int:

        nrows = len(grid)
        if not nrows:
            return 0

        ncols = len(grid[0])
        if not ncols:
            return 0

        max_area = 0
        unvisited = [[True] * ncols for _ in range(nrows)]

        curr_nodes = []
        curr_area = 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] and unvisited[i][j]:
                    curr_nodes.append((i, j))
                    curr_area += 1
                    unvisited[i][j] = False
                else:
                    continue

                while curr_nodes:
                    posi = curr_nodes.pop()
                    x, y = posi[0], posi[1]

                    if x - 1 >= 0 and grid[x-1][y] and unvisited[x-1][y]:
                        curr_nodes.append((x-1, y))
                        curr_area += 1
                        unvisited[x-1][y] = False
                    if x + 1 < nrows and grid[x+1][y] and unvisited[x+1][y]:
                        curr_nodes.append((x+1, y))
                        curr_area += 1
                        unvisited[x + 1][y] = False
                    if y - 1 >= 0 and grid[x][y-1] and unvisited[x][y-1]:
                        curr_nodes.append((x, y-1))
                        curr_area += 1
                        unvisited[x][y - 1] = False
                    if y + 1 < ncols and grid[x][y+1] and unvisited[x][y+1]:
                        curr_nodes.append((x, y+1))
                        curr_area += 1
                        unvisited[x][y + 1] = False

                max_area = max(max_area, curr_area)
                curr_area = 0
        return max_area



print(Solution().maxAreaOfIsland([[0],[1]]))