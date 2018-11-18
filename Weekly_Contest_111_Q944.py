class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        nsample = len(A)
        nlength = len(A[0])

        wrong_str = 0

        for j in range(nlength):
            for i in range(nsample - 1):
                if A[i][j] > A[i + 1][j]:
                    wrong_str += 1
                    break

        return wrong_str


if __name__ == '__main__':
    print(Solution().minDeletionSize(["zyx","wvu","tsr"]))
