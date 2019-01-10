from collections import defaultdict
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lookup = defaultdict(int)

        for item in nums:
            lookup[item] += 1

        result = []
        for item in lookup:
            if lookup[item] > len(nums) / 3:
                result.append(item)

        return result


if __name__ == '__main__':
    print(Solution().majorityElement([1,1,1,3,3,2,2,2]))