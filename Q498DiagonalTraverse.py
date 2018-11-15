class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        result = []

        if not matrix:
            return result
        if len(matrix) == 1:
            for item in matrix[0]:
                result.append(item)
            return result
        if len(matrix[0]) == 1:
            for item in matrix:
                result.append(item[0])
            return result

        posi = [0, 0]
        max_index_row = len(matrix) - 1
        max_index_col = len(matrix[0]) - 1

        result.append(matrix[0][0])

        # even right-up, odd left-down
        direction = 0
        adjust_flag = False
        while posi[0] != max_index_row or posi[1] != max_index_col:
            # up-bottom border
            if posi[0] in [0, max_index_row] and not adjust_flag:
                if posi[1] < max_index_col:
                    posi[1] += 1
                else:
                    posi[0] += 1
                result.append(matrix[posi[0]][posi[1]])
                direction += 1
                adjust_flag = True
            # left-right border
            elif posi[1] in [0, max_index_col] and not adjust_flag:
                if posi[0] < max_index_row:
                    posi[0] += 1
                else:
                    posi[1] += 1
                result.append(matrix[posi[0]][posi[1]])
                direction += 1
                adjust_flag = True
            # central area
            else:
                if direction % 2 == 0:
                    posi[0] -= 1
                    posi[1] += 1
                else:
                    posi[0] += 1
                    posi[1] -= 1
                result.append(matrix[posi[0]][posi[1]])
                adjust_flag = False

        return result





if __name__ == "__main__":
    print(Solution().findDiagonalOrder([[2,3]]))