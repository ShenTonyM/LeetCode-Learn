from collections import defaultdict, Counter
import copy
class Solution1:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return [[]]

        m = Counter(nums)

        total_result = [[]]

        for k, v in m.items():
            prev_subsets = copy.deepcopy(total_result)
            for i in range(v):
                cur_subsets = copy.deepcopy(prev_subsets)
                for subset in cur_subsets:
                    subset.append(k)
                total_result.extend(cur_subsets)
                prev_subsets = copy.deepcopy(cur_subsets)

        return total_result

class Solution2(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        previous_size = 0
        for i in range(len(nums)):
            size = len(result)
            for j in range(size):
                # Only union non-duplicate element or new union set.
                if i == 0 or nums[i] != nums[i - 1] or j >= previous_size:
                    result.append(list(result[j]))
                    result[-1].append(nums[i])
            previous_size = size
        return result








if __name__ == '__main__':
    print(Solution2().subsetsWithDup([1,2,2]))