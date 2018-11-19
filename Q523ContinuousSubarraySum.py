class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """


        lookup = {0: -1}
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if k != 0:
                count %= k
            if count in lookup:
                if lookup[count] < i - 1:
                    return  True
            else:
                lookup[count] = i

        return False


if __name__ == '__main__':
    print(Solution().checkSubarraySum([23,2,4,6,7], 6))