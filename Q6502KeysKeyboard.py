import math
class Solution1:
    def findDivisors(self, num):
        result = []
        for i in range(1, math.floor(num / 2) + 1):
            if num % i == 0:
                result.append(i)
        return result

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp从1开始吧
        dp = [0]*(n+1)
        dp[0] = float('inf')
        dp[1] = 0
        for i in range(2, n + 1):
            min_steps = float('inf')
            divisors = self.findDivisors(i)
            for divisor in divisors:
                min_steps = min(min_steps, dp[divisor] + i // divisor)
            dp[i] = min_steps
        return dp[-1]

class Solution2(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        p = 2
        # the answer is the sum of prime factors
        while p**2 <= n:
            while n % p == 0:
                result += p
                n //= p
            p += 1
        if n > 1:
            result += n
        return result


if __name__ == '__main__':
    print(Solution1().minSteps(9))