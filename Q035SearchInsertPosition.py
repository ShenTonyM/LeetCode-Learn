class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            if nums[i] >= target:
                return i
        return length

if __name__ == '__main__':
    print(Solution().searchInsert([1,3,5,6],5))