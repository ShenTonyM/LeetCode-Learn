import copy


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for new_item in nums:
            old_result = []
            for exist_subset in result:
                old_result.append(copy.deepcopy(exist_subset))
                exist_subset.append(new_item)
            result.extend(old_result)

        return result

if __name__ == '__main__':
    print(Solution().subsets([1,2,3]))