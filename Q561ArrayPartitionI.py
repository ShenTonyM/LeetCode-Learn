class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s_nums = sorted(nums,reverse=True)

        return sum([s_nums[i] for i in range(len(s_nums)) if i%2 == 1])



if __name__ == '__main__':
    print(Solution().arrayPairSum(nums=[1,4,3,2]))
