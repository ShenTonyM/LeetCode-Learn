class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        if not edges:
            return [0]

        sides = {i:set() for i in range(n)}

        # manage the sides
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            sides[node1].add(node2)
            sides[node2].add(node1)

        # find lead nodes
        leaf_nodes =set()
        for node in sides:
            if len(sides[node]) == 1:
                leaf_nodes.add(node)

        candidate_root = {i for i in range(n)}

        while len(candidate_root) > 2:
            next_leaf_nodes = set()
            for node in leaf_nodes:
                candidate_root.remove(node)
                for adjacent in sides[node]:
                    if adjacent in candidate_root:
                        sides[adjacent].remove(node)
                        if len(sides[adjacent]) == 1:
                            next_leaf_nodes.add(adjacent)
                sides.pop(node)

            leaf_nodes = next_leaf_nodes


        return list(candidate_root)





if __name__ == "__main__":
    print(Solution().findMinHeightTrees(7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]))