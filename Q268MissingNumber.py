class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        expect_sum = (1 + n) * n // 2

        for num in nums:
            expect_sum -= num

        return expect_sum


if __name__ == '__main__':
    print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))