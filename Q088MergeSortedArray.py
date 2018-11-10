class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        n1_remain = m
        n2_remain = n

        while n1_remain or n2_remain:
            if n1_remain and n2_remain:
                if nums1[n1_remain - 1] > nums2[n2_remain - 1]:
                    nums1[n1_remain + n2_remain - 1] = nums1[n1_remain - 1]
                    n1_remain -= 1
                else:
                    nums1[n1_remain + n2_remain - 1] = nums2[n2_remain - 1]
                    n2_remain -= 1
            elif n2_remain:
                nums1[:n2_remain] = nums2[:n2_remain]
                return nums1
            else:
                return nums1

if __name__ == "__main__":

    print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))