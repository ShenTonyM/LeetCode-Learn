class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0和1的数量
        counts = [0] * 2

        result = 0

        for i in range(32):
            for num in nums:
                counts[(num >> i) & 1] += 1
            result += counts[0] * counts[1]
            counts = [0] * 2

        return result





if __name__ == '__main__':
    print(Solution().totalHammingDistance([4,14,2]))