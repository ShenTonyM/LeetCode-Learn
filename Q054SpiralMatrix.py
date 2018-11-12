class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])

        result = []

        directions_data = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        posi = [0, 0]
        direction = 0

        first_flag = True
        while n + 1 and m:
            direction %= 4
            if direction % 2 == 0:
                if first_flag:
                    for i in range(n):
                        result.append(matrix[posi[0]][posi[1]])
                        posi[0] += directions_data[direction][0]
                        posi[1] += directions_data[direction][1]

                    posi[0] -= directions_data[direction][0]
                    posi[1] -= directions_data[direction][1]
                    first_flag = False

                    n -= 1
                    direction += 1
                else:
                    for i in range(n):
                        posi[0] += directions_data[direction][0]
                        posi[1] += directions_data[direction][1]
                        result.append(matrix[posi[0]][posi[1]])
                    n -=1
                    direction += 1
            else:
                for i in range(m - 1):
                    posi[0] += directions_data[direction][0]
                    posi[1] += directions_data[direction][1]
                    result.append(matrix[posi[0]][posi[1]])
                m -=1
                direction += 1

        return result


if __name__ == "__main__":
    print(Solution().spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))