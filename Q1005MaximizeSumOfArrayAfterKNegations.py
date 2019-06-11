class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        A_sort = sorted(A)

        count = 0
        for i in range(len(A_sort)):
            if A_sort[i] < 0:
                A_sort[i] = -A_sort[i]
                count += 1
            if count == K:
                return sum(A_sort)

        return sum(A_sort) - (K-count) % 2 * min(A_sort) * 2

if __name__ == '__main__':
    print(Solution().largestSumAfterKNegations([4,2,3],1))