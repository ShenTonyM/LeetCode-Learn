import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
        opposite_stones = [-x for x in stones]
        heapq.heapify(opposite_stones)

        while len(opposite_stones) > 1:
            stone_1 = heapq.heappop(opposite_stones)
            stone_2 = heapq.heappop(opposite_stones)

            res = -abs(stone_1 - stone_2)
            if res != 0:
                heapq.heappush(opposite_stones, res)

        if len(opposite_stones) == 1:
            return -opposite_stones[0]
        else:
            return 0

if __name__ == "__main__":
    print(Solution().lastStoneWeight([2,2]))
