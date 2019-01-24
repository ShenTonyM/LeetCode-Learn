class Solution(object):
    def __init__(self):
        self.result = []
    def dfs(self, graph, curr, path):
        if curr == len(graph) - 1:
            self.result.append(list(path))
            return
        for node in graph[curr]:
            path.append(node)
            self.dfs(graph, node, path)
            path.pop()

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        self.result = []
        self.dfs(graph, 0, [0])
        return self.result

if __name__ == '__main__':
    print(Solution().allPathsSourceTarget([[1,2],[3],[3],[]]))