class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        prev_2 = 0
        prev_1 = nums[0]

        for item in nums[1:]:
            prev_2, prev_1 = prev_1,  max(prev_2 + item, prev_1)

        return prev_1



if __name__ == "__main__":
    print(Solution().rob([1,2,3,1]))