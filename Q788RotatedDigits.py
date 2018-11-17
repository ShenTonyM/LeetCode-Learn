class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        accept_nums = [0, 1, 8]
        necessary_nums = [2, 5, 6, 9]

        good_number = 0

        for i in range(1, N + 1):
            examine_flag = False
            examine_num = i
            while examine_num:
                digit = examine_num % 10
                if digit not in accept_nums and digit not in necessary_nums:
                    examine_flag = False
                    break
                elif digit in necessary_nums:
                    examine_flag = True

                examine_num = examine_num // 10

            if examine_flag:
                good_number += 1

        return good_number

# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        INVALID, SAME, DIFF = 0, 1, 2
        same, diff = [0, 1, 8], [2, 5, 6, 9]
        dp = [0] * (N+1)
        dp[0] = SAME
        for i in range(N//10+1):
            if dp[i] != INVALID:
                for j in same:
                    if i*10+j <= N:
                        dp[i*10+j] = max(SAME, dp[i])
                for j in diff:
                    if i*10+j <= N:
                        dp[i*10+j] = DIFF
        return dp.count(DIFF)

if __name__ == '__main__':
    print(Solution2().rotatedDigits(857))
