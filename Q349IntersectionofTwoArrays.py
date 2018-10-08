class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        inter_num = []
        for item in set_nums1:
            if item in set_nums2:
                inter_num.append(item)

        return list(set_nums1 & set_nums2)

if __name__ == '__main__':
    print(Solution().intersection([1,2,2,1],[2,2]))