class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return None

        nums_sort = sorted(nums)
        a = nums_sort[-3] * nums_sort[-2] * nums_sort[-1]
        b = nums_sort[0] * nums_sort[1] * nums_sort[-1]

        return max(a, b)


if __name__ == '__main__':
    print(Solution().maximumProduct([1,2,3]))