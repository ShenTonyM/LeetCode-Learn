import operator


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        result = []
        i = 0

        while i < len(nums):
            if i == 0 or nums[i] != nums[i - 1]:
                m = i + 1
                n = len(nums) - 1
                while m < n:
                    if nums[i] + nums[m] + nums[n] < 0:
                        m += 1
                    elif nums[i] + nums[m] + nums[n] > 0:
                        n -= 1
                    else:
                        result.append([nums[i], nums[m], nums[n]])
                        m += 1
                        n -= 1
                        while m < n and nums[m] == nums[m - 1]:
                            m += 1
                        while m < n and nums[n] == nums[n + 1]:
                            n -= 1
            i += 1

        return result
if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))