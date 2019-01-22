class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self._nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self._nums[i:j+1])

if __name__ == '__main__':
    obj = NumArray([1, 3, 5])
    param_1 = obj.sumRange(0,2)
    obj.update(1, 2)
    param_2 = obj.sumRange(0,2)