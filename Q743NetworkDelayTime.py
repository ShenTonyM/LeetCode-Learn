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




if __name__ == '__main__':
    print(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
