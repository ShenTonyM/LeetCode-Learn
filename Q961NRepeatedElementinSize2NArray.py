class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        for i in range(2, len(A)):
            if A[i-2] == A[i] or A[i-1] == A[i]:
                return A[i]

        return A[0]


if __name__ == '__main__':
    print(Solution().repeatedNTimes([1,2,3,3]))