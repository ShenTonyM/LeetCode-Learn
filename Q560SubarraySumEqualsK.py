from  collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        accumulation = 0
        sums = defaultdict(int)
        sums[0] = 1
        result = 0

        for i in range(len(nums)):
            accumulation += nums[i]
            result += sums[accumulation - k]
            sums[accumulation] += 1

        return result




if __name__ == '__main__':
    print(Solution().subarraySum([1,2,1,2,1], 3))