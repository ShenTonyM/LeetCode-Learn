# class Solution1:
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         sorted_nums = sorted(nums)
#         for i in range(len(nums)//2):
#             if sorted_nums[i*2] != sorted_nums[i*2+1]:
#                 return sorted_nums[i*2]
#         return sorted_nums[len(nums)-1]

# 异或运算

import operator
from functools import reduce
class Solution2:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor,nums)

if __name__ == '__main__':
    print(Solution2().singleNumber([2,2,1]))