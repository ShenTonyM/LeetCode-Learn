# 每次判断一个数字能不能用在当前的集合中
class Solution1(object):
    def canSumTarget(self, nums, visited, start_index, cur_sum, target, k, numbers_used):
        if cur_sum > target:
            return False
        if cur_sum == target and k != 0:
            return self.canSumTarget(nums, visited, 0, 0, target, k - 1, numbers_used)
        if k == 0 and numbers_used == len(nums):
            return True

        for i in range(start_index, len(nums)):
            if not visited[i]:
                # 尝试这个数行不行
                visited[i] = True
                if self.canSumTarget(nums, visited, i + 1, cur_sum + nums[i], target, k, numbers_used + 1):
                        return True
                visited[i] = False
        return False


    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if k == 1:
            return True

        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False

        target = nums_sum // k
        visited = [False] * len(nums)

        start_index = 0
        cur_sum = 0
        numbers_used = 0

        return self.canSumTarget(nums, visited, start_index, cur_sum, target, k, numbers_used)




if __name__ == '__main__':
    print(Solution1().canPartitionKSubsets([4,15,1,1,1,1,3,11,1,10], 3))