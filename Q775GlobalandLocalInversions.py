class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True

        for i in range(len(A)):
            if abs(A[i] - i) >= 2:
                return False

        return True


if __name__ == '__main__':
    print(Solution().isIdealPermutation([0]))