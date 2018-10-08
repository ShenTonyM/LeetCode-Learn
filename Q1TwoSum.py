class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """ brutal """
        # length = len(nums)
        # for i in range(length):
        #     for j in range(i+1, length):
        #         if nums[i] + nums[j] == target:
        #             return i, j

        """ use dict (hashtable) """

        lookup = {}

        # enumerate 可以同时返回index和item
        for index, item in enumerate(nums):
            if target - item in lookup:
                return lookup[target - item], index
            else:
                lookup[item] = index
if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15],9))