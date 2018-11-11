class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        minimum_path = []

        height = len(triangle)
        minimum_path.append([triangle[0][0]])

        for i in range(1, height):
            minimum_path.append([])
            for j in range(i + 1):
                if j == 0:
                    minimum_path[i].append(minimum_path[i - 1][j] + triangle[i][j])
                elif j == i:
                    minimum_path[i].append(minimum_path[i - 1][j - 1] + triangle[i][j])
                else:
                    minimum_path[i].append(min(minimum_path[i - 1][j - 1],minimum_path[i - 1][j]) + triangle[i][j])

        return min(minimum_path[height - 1])

if __name__ == "__main__":
    print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))