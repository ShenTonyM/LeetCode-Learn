class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not len(matrix):
            return False
        if not len(matrix[0]):
            return False

        i, j = 0, len(matrix[0]) - 1

        while i != len(matrix) and j != -1:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False



if __name__ == '__main__':
    print(Solution().searchMatrix(
        [[1,4,7,11,15],
         [2,5,8,12,19],
         [3,6,9,16,22],
         [10,13,14,17,24],
         [18,21,23,26,30]],5))