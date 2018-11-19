import collections
from collections import deque


class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        nodes = {i: set() for i in range(N)}

        for i in range(len(times)):
            start_node = times[i][0]
            end_node = times[i][1]
            time = times[i][2]

            nodes[start_node].add((end_node, time))

        next_nodes = deque()
        next_nodes.append(K)

        propagade_times = [float('inf')] * N
        propagade_times[K] = 0

        while next_nodes:
            node_num = next_nodes.popleft()
            for item in nodes[node_num]:
                next_node_num = item[0]
                if next_node_num in nodes:
                    pass


class Solution2:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        K -= 1
        nodes = collections.defaultdict(list)
        for u, v, w in times:
            nodes[u - 1].append((v - 1, w))
        dist = [float('inf')] * N
        dist[K] = 0
        done = set()
        for _ in range(N):
            smallest = min((d, i) for (i, d) in enumerate(dist) if i not in done)[1]
            for v, w in nodes[smallest]:
                if v not in done and dist[smallest] + w < dist[v]:
                    dist[v] = dist[smallest] + w
            done.add(smallest)
        return -1 if float('inf') in dist else max(dist)





if __name__ == '__main__':
    print(Solution2().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
