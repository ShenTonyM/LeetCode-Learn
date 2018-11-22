class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        adjust_index = 1
        check_index = 1
        emerge_times = 1
        prev_num = nums[0]

        while check_index != len(nums):
            if nums[check_index] != prev_num:
                emerge_times = 1
                prev_num = nums[check_index]
                nums[adjust_index] = nums[check_index]
                adjust_index += 1
            else:
                emerge_times += 1
                if emerge_times < 3:
                    nums[adjust_index] = nums[check_index]
                    adjust_index += 1

            check_index += 1

        return adjust_index






if __name__ == '__main__':
    nums= [0,0,1,1,1,1,2,3,3]
    print(Solution().removeDuplicates(nums))
