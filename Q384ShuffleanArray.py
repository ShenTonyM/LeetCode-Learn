import random


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums= nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self._nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

        # new list nums not points to self._nums
        nums = list(self._nums)

        for i in range(len(nums)):
            j = random.randint(i, len(nums) - 1)
            nums[i], nums[j] = nums[j], nums[i]

        return nums



if __name__ == "__main__":
    obj = Solution([1,2,3])
    param_2 = obj.shuffle()
    param_1 = obj.reset()
    print(param_2, param_1)
