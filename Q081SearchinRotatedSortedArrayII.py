class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        # todo: to be continued
        i, j = 0, len(nums) - 1
        visited = [False] * len(nums)



        while i != j:
            mid_index = (i + j) // 2
            if nums[mid_index] == target:
                return True
            elif nums[mid_index] > target:
                pass


if __name__ == '__main__':
    print(Solution().search([2,5,6,0,0,1,2], 0))