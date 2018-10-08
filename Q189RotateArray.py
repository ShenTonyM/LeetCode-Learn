# class Solution1:
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#
#         length = len(nums)
#
#         new_nums = [0 for x in range(length)]
#         for old_index in range(length):
#             new_index = (old_index + k) % length
#             new_nums[new_index] = nums[old_index]
#
#         for i in range(length):
#             nums[i] = new_nums[i]

# 三次翻转
class Solution2:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        k = k % length
        self.reverse(nums, 0, length)
        self.reverse(nums, 0, k)
        self.reverse(nums, k, length)

    def reverse(self,nums, start, end):

        while start < end:
            nums[start],nums[end-1] = nums[end-1], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    Solution2().rotate([1,2,3,4,5,6,7],3)