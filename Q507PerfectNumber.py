import math
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 0:
            return False

        accumul = 1
        n = 2

        while n < math.sqrt(num):
            if num % n == 0:
                accumul += n
                accumul += num // n
            n += 1

        mid = math.sqrt(num)

        if math.ceil(mid) == math.floor(mid):
            accumul += int(mid)

        return accumul == num




if __name__ == '__main__':
    print(Solution().checkPerfectNumber(2))