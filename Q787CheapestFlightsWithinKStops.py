import heapq

import collections


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        print(adj)

        best = collections.defaultdict(lambda: collections.defaultdict(lambda: float("inf")))

        min_heap = [(0, src, K + 1)]
        while min_heap:
            result, u, k = heapq.heappop(min_heap)
            if k < 0 or best[u][k] < result:
                continue
            if u == dst:
                return result
            for v, w in adj[u]:
                if result + w < best[v][k - 1]:
                    best[v][k - 1] = result + w
                    heapq.heappush(min_heap, (result + w, v, k - 1))
        return -1



if __name__ == '__main__':
    print(Solution().findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))