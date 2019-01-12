from collections import defaultdict
class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """

        offsets = defaultdict(int)

        for x1 in range(len(A)):
            for y1 in range(len(A)):
                if A[x1][y1] == 1:
                    for x2 in range(len(B)):
                        for y2 in range(len(B)):
                            if B[x2][y2] == 1:
                                delta = (x2 - x1, y2 - y1)
                                offsets[delta] += 1
        if offsets:
            return max(offsets.values())
        else:
            return 0

if __name__ == '__main__':
    # print(Solution().largestOverlap(
    #     [[1,1,0],
    #      [0,1,0],
    #      [0,1,0]],
    #     [[0,0,0],
    #      [0,1,1],
    #      [0,0,1]]))
    print(Solution().largestOverlap(
        [[0]],
        [[0]]))
