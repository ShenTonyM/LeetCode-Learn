class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        oriLen  = len(nums)
        newIndex = 0

        for i in range(oriLen):
            if nums[i] != val:
                nums[newIndex] = nums[i]
                newIndex += 1
        return newIndex

if __name__ == "__main__":
    print(Solution().removeElement([3,2,2,3],3))
