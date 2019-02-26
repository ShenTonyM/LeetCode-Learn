# class Solution1:
#
#     def nextGreaterElement(self, n: int) -> int:
#         num_str = str(n)
#
#         if n >= 2**31:
#             return -1
#
#         last_num = float('-inf')
#         for i in range(len(num_str) - 1, -1, -1):
#             if int(num_str[i]) < last_num:
#                 num_rest = sorted(num_str[i:])
#                 num_rest = ''.join(num_rest)
#                 for j in range(len(num_rest)):
#                     if int(num_rest[j]) > int(num_str[i]):
#                         if j != len(num_rest) - 1:
#                             num_adjust = num_rest[j] + num_rest[:j] + num_rest[j+1:]
#                         else:
#                             num_adjust = num_rest[j] + num_rest[:j]
#                         result = int(num_str[:i] + num_adjust)
#                         return result
#
#             last_num = int(num_str[i])
#
#         return -1


class Solution2(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(map(int, list(str(n))))
        start = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]: #从后往前一直升序，找到第一个降序的
                #如1,2,6,5,4,3，则nums[start] = 2
                start = i - 1
                break
        if start == -1:#整个序列降序，无下一个排列
            return -1
        for i in range(len(nums) - 1, start, -1):
            if nums[i] > nums[start]: #在刚刚的子序列里找到第一个大于nums[start]的
                nums[i], nums[start] = nums[start], nums[i] #交换
                break
        nums[start + 1:] = sorted(nums[start + 1:])
        tmp = int(''.join(list(map(str, nums))))
        return tmp if tmp <= 2 ** 31 - 1 else -1





if __name__ == '__main__':
    print(Solution2().nextGreaterElement(1234))