from collections import Counter
from functools import reduce
from operator import xor, add, sub
class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        return [x[0] for x in sorted(Counter(nums).items(), key=lambda m:m[1], reverse=True)][:2]


class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """ the result all_xor is an integer """
        all_xor = reduce(xor, nums)

        """ m is a string: "0b110" """
        m = bin(all_xor)

        """ 这样减去位数之后，取出的是最高位的二进制，如5(110) -> 1(1), 3(10) -> 0(0) """
        bits_eliminate = len(m) - 3

        res = [0, 0]

        for num in nums:
            if num >> bits_eliminate & 1:
                res[0] ^= num
            else:
                res[1] ^= num

        return [res[0], res[1]]



if __name__ == '__main__':
    print(Solution2().singleNumber([1,2,1,3,2,5]))