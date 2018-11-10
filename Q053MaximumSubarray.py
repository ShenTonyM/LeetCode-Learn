class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)

        max_sub_sum = float('-inf')
        sub_sum = 0
        for item in nums:
            sub_sum = max(sub_sum + item, 0)
            max_sub_sum = max(sub_sum, max_sub_sum)

        return max_sub_sum


if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))