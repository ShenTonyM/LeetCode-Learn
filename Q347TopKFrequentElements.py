from collections import Counter
# Counter method
class Solution1(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [k for k,v in Counter(nums).most_common(k)]


if __name__ == '__main__':
    print(Solution1().topKFrequent([1,1,1,2,2,3], 2))