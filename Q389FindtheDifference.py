from functools import reduce
import operator
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """


        return chr(reduce(operator.xor, map(ord, s), 0) ^ reduce(operator.xor, map(ord, t), 0))


if __name__ == '__main__':
    print(Solution().findTheDifference("abcd","abcde"))