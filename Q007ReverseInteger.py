class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        digits = []
        if x > 0:
            while x != 0:
                digit = x % 10
                digits.append(digit)
                x = x // 10

            num = 0
            for digit in digits:
                num = num * 10
                num += digit

            if num < -2 ** 31 or num > 2 ** 31 + 1:
                return 0

            return num
        else:
            x = -x
            while x != 0:
                digit = x % 10
                digits.append(digit)
                x = x // 10

            num = 0
            for digit in digits:
                num = num * 10
                num += digit

            num = -num

            if num < -2 ** 31 or num > 2 ** 31 + 1:
                return 0
            return num


if __name__ == "__main__":
    print(Solution.reverse(Solution,1534236469))