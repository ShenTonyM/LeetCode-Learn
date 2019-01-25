class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        # TODO: to be continued
        posi_candi = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        proba_array = [([0] * N) for i in range(N)]
        print(proba_array)

        for m in range(K):
            temp_array = list(proba_array)
            for i in range(N):
                for j in range(N):
                    for p in range(8):
                        pass


if __name__ == '__main__':
    print(Solution().knightProbability(3,2,0,0))