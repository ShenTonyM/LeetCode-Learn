class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        if len(A) < 3:
            return False

        flag = 'left'
        left_flag = False

        for i in range(len(A) - 1):
            if flag == 'left':
                if A[i + 1] < A[i]:
                    flag = 'right'
                elif A[i + 1] == A[i]:
                    return False
                else:
                    left_flag = True
            elif flag == 'right':
                if A[i + 1] >= A[i]:
                    return False

        if flag == 'right' and left_flag:
            return True
        else:
            return False






if __name__ == '__main__':
    print(Solution().validMountainArray([0,3,2,1]))
