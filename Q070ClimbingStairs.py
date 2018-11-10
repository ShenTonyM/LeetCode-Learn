# Time:  O(2^n)
# Space: O(n)

class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        else:
            return self.climbStairs(n - 2) + self.climbStairs(n - 1)


class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # prev, current = 0, 1
        # for i in range(n):
        #     prev, current = current, prev + current,
        # return current

        cs = [None for x in range(n + 1)]
        cs[0] = 1
        cs[1] = 1
        for i in range(2, n + 1):
            cs[i] = cs[i-1] + cs[i-2]

        return cs[n]


if __name__ == "__main__":

    print(Solution2().climbStairs(2))