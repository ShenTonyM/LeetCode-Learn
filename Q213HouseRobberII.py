class Solution:
    def robRange(self,nums, start, end):
        prev, cur = 0, 0
        for i in range(start, end):
            prev, cur = cur, max(prev + nums[i], cur)

        return cur

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(self.robRange(nums,0,len(nums) - 1), self.robRange(nums, 1, len(nums)))





if __name__ == '__main__':
    print(Solution().rob([1,2,3,1]))