class Solution1(object):
    def isValid(self, nums, m, max_sum):
        """
        :rtype: bool
        """
        count = 0
        accumu = 0
        for i in range(len(nums)):
            accumu += nums[i]
            if accumu > max_sum:
                count += 1
                if count >= m:
                    return False

                accumu = nums[i]
        return True

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        result_max, result_min = sum(nums), max(nums)

        left, right = result_min, result_max

        while left < right:
            mid = (left + right) // 2
            if self.isValid(nums, m, mid):
                right = mid
            else:
                left = mid + 1

        return left







if __name__ == '__main__':
    print(Solution1().splitArray([7,2,5,10,8], 2))