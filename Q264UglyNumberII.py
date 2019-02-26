class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        result = []
        result.append(1)
        index2, index3, index5 = 0, 0, 0

        for i in range(1, n):
            result.append(min([result[index2]*2, result[index3]*3, result[index5]*5]))

            if result[i] == result[index2]*2:
                index2 += 1
            if result[i] == result[index3]*3:
                index3 += 1
            if result[i] == result[index5]*5:
                index5 += 1

        return result[-1]




if __name__ == '__main__':
    print(Solution().nthUglyNumber(10))