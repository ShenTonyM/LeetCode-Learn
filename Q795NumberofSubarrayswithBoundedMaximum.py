class Solution(object):
    def numSubarrayRightBoundedMax(self, A, R):
        result = 0
        accumulate = 0
        for i, item in enumerate(A):
            if item > R:
                accumulate = 0
            else:
                accumulate += 1
                result += accumulate

        return result

    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """

        return self.numSubarrayRightBoundedMax(A, R) - self.numSubarrayRightBoundedMax(A, L - 1)



class Solution2(object):

    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """

        result = 0
        accumulate = 0
        left = 0

        for right in range(len(A)):
            if A[right] <= R and A[right] >= L:
                accumulate = right - left + 1
                result += accumulate
            elif A[right] < L:
                result += accumulate
            else:
                left = right + 1
                accumulate = 0

        return result




if __name__ == '__main__':
    print(Solution2().numSubarrayBoundedMax([2,1,4,3],2,3))