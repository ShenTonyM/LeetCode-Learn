class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)

        # diagnonal flip
        for i in range(size):
            for j in range(i, size):
                # matrix[i][j], matrix[size - j - 1][size - i - 1] = matrix[size - j - 1][size - i - 1], matrix[i][j]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)

        # vertical flip
        for j in range(size//2):
            for i in range(size):
                matrix[i][j], matrix[i][size - j - 1] = matrix[i][size - j - 1], matrix[i][j]

        print(matrix)



if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().rotate(matrix)