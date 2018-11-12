class Solution(object):
    def isValid(self, ans, N, K):
        if N == 1:
            return ans == 0

        if ans == 0:
            if K % 2 == 0:
                return self.isValid(1, N - 1, K // 2)
            else:
                return self.isValid(0, N - 1, (K + 1) // 2)
        else:
            if K % 2 == 0:
                return self.isValid(0, N - 1, K // 2)
            else:
                return self.isValid(1, N - 1, (K + 1) // 2)



    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        
        # 验证法，假设结果是0
        return 0 if self.isValid(0, N, K) else 1



if __name__ == '__main__':
    print(Solution().kthGrammar(4, 5))