class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        pos = 0

        for i in range(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1

        for i in range(pos, len(nums)):
            nums[i] = 0

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print(nums)