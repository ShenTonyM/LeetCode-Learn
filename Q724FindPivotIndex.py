class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        total = sum(nums)

        sum_forward = 0
        for i, num in enumerate(nums):
            if sum_forward == total - num - sum_forward:
                return i
            sum_forward += num

        return -1



if __name__ == '__main__':
    print(Solution().pivotIndex([1,7,3,6,5,6]))