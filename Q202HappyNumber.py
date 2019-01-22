class Solution:
    def isHappyRecur(self, n, visited):
        sum_n = 0
        while n:
            sum_n += (n % 10) ** 2
            n = n // 10

        if sum_n == 1:
            return True
        elif sum_n in visited:
            return False
        else:
            visited.append(sum_n)
            return self.isHappyRecur(sum_n, visited)
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = []

        return self.isHappyRecur(n, visited)

if __name__ == '__main__':
    print(Solution().isHappy(1111111))