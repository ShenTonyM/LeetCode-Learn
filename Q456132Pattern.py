class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        a3 = float('-inf')
        st = []

        for i in reversed(range(len(nums))):
            if nums[i] < a3:
                return True
            else:
                while st and nums[i] > st[-1]:
                    a3 = st.pop()
                st.append(nums[i])

        return False



if __name__ == '__main__':
    print(Solution().find132pattern([4,1,3,2]))