class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        index = 1
        while index < len(nums):
            if nums[index] == nums[index - 1]:
                nums.pop(index)
                index -= 1
            index += 1
        return len(nums)


if __name__ == '__main__':
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))