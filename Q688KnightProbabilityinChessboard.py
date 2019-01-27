class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """

        posi_candi = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        proba_array = [([0] * N) for i in range(N)]
        proba_array[r][c] = 1
        print(proba_array)

        for m in range(K):
            temp_array = [([0] * N) for i in range(N)]
            for i in range(N):
                for j in range(N):
                    src_posi = (i, j)
                    candidate_dst_posi = []
                    for p in range(8):
                        dst_posi = (src_posi[0] + posi_candi[p][0], src_posi[1] + posi_candi[p][1])
                        if 0 <= dst_posi[0] < N and 0 <= dst_posi[1] < N:
                            candidate_dst_posi.append(dst_posi)
                    for next_posi in candidate_dst_posi:
                        temp_array[next_posi[0]][next_posi[1]] += proba_array[src_posi[0]][src_posi[1]] / 8

            proba_array = temp_array

        return sum(map(sum, proba_array))

if __name__ == '__main__':
    print(Solution().knightProbability(3,2,0,0))