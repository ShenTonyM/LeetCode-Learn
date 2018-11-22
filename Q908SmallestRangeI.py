class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        max_num, min_num = max(A), min(A)

        return max(max_num - min_num - 2 * K, 0)


if __name__ == '__main__':
    print(Solution().smallestRangeI( [10,7,1], 3))
