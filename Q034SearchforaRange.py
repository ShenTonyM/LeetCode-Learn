class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 0:
            return [-1, -1]

        left_bound, right_bound = float('inf'), float('-inf')

        # find left bound
        i,j = 0, len(nums) - 1
        while i <= j:
            median_index = (i + j) // 2
            if nums[median_index] < target:
                i = median_index + 1
            elif nums[median_index] > target:
                j = median_index - 1
            else:
                j = median_index - 1
                left_bound = min(median_index, left_bound)

        # find right bound
        i,j = 0, len(nums) - 1
        while i <= j:
            median_index = (i + j) // 2
            if nums[median_index] < target:
                i = median_index + 1
            elif nums[median_index] > target:
                j = median_index - 1
            else:
                i = median_index + 1
                right_bound = max(median_index, right_bound)

        left_bound = -1 if left_bound == float('inf') else left_bound
        right_bound = -1 if right_bound == float('-inf') else right_bound

        return [left_bound, right_bound]

if __name__ == '__main__':
    print(Solution().searchRange([1], 1))