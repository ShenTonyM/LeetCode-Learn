from collections import defaultdict
# class Solution1:
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         lookup = defaultdict(list)
#
#         for i in range(len(nums)):
#             lookup[nums[i]].append(i)
#
#         for item in nums:
#             indices = lookup[item]
#             if len(indices) == 1:
#                 continue
#             for i in range(len(indices) - 1):
#                 if indices[i + 1] - indices[i] <= k:
#                     return True
#
#         return False
#

class Solution2:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lookup = {}

        for i, item in enumerate(nums):
            if item in lookup:
                if i - lookup[item] <= k:
                    return True
                else:
                    lookup[item] = i
            else:
                lookup[item] = i
        return False




if __name__ == '__main__':
    print(Solution2().containsNearbyDuplicate([1,2,3,1,2,3], 2))