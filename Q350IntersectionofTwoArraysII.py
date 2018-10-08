class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seq_nums1 = sorted(nums1)
        seq_nums2 = sorted(nums2)
        i,j = 0, 0

        inter_list = []
        while i < len(seq_nums1) and j < len(seq_nums2):
            if seq_nums1[i] < seq_nums2[j]:
                i += 1
            elif seq_nums1[i] > seq_nums2[j]:
                j += 1
            else:
                inter_list.append(seq_nums1[i])
                i += 1
                j += 1

        return inter_list


if __name__ == '__main__':
    print(Solution().intersect([1,2,2,1],[2,2]))