class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        sum_A, sum_B = sum(A), sum(B)
        ele_A, ele_B = set(A), set(B)

        diff = sum_A - sum_B

        for item in ele_A:
            if item - diff // 2 in ele_B:
                return [item, item - diff // 2]



if __name__ == '__main__':
    print(Solution().fairCandySwap([1,1], [2,2]))