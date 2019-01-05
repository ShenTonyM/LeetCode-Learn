class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        r_old, c_old = len(nums), len(nums[0])

        if r_old * c_old != r * c:
            return nums

        result = []

        i_old, j_old = 0, 0
        for i in range(r):
            result.append([])
            for j in range(c):
                if j_old == c_old:
                    i_old, j_old = i_old + 1, 0
                result[i].append(nums[i_old][j_old])
                j_old += 1
        return result




if __name__ == '__main__':
    print(Solution().matrixReshape([[1,2],[3,4]],1,4))