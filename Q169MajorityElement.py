class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        m = dict()

        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1

        max_times = 0
        max_num = 0

        for key in m:
            if m[key] > max_times:
                max_num = key
                max_times = m[key]

        return max_num


if __name__ == '__main__':
    print(Solution().majorityElement([3,2,3]))