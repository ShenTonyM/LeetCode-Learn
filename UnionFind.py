class QuickFind:
    def __init__(self, N):
        self.count = N
        self.id = [i for i in range(N)]

    def find(self, p):
        return self.id[p]

    def getCount(self):
        return self.count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pid, qid = self.find(p), self.find(q)

        if pid == qid:
            return

        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid

        self.count -= 1

        return

class UnionFind():
    def __init__(self, N):
        self.count = N
        self.id = [i for i in range(N)]
        # the number of nodes that rooted by this node
        self.weight = [1 for _ in range(N)]

    def find(self, p):
        if self.id[p] != p:
            self.id[p] = self.find(self.id[p])
        return self.id[p]

        # path compression

        # node = p
        # while self.id[node] != node:
        #     if self.id[self.id[node]] != self.id[node]:
        #         self.id[node] = self.id[self.id[node]]
        #     node = self.id[node]
        #
        # return self.id[node]

    def getCount(self):
        return self.count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root, q_root = self.find(p), self.find(q)

        if p_root == q_root:
            return

        # small tree is set the subtree of the large tree
        if self.weight[p_root] < self.weight[q_root]:
            self.id[p_root] = q_root
            self.weight[p_root] += self.weight[q_root]
        else:
            self.id[q_root] = p_root
            self.weight[q_root] += self.weight[p_root]
        self.count -= 1
        return


if __name__ == '__main__':
    # N为节点数目 M为输入关系系的数目
    N, M = tuple(map(int, input().split(' ')))
    # qf = QuickFind(N)
    uf = UnionFind(N)

    for i in range(M):
        p, q = tuple(map(int, input().split(' ')))
        uf.union(p, q)

    print(uf.getCount())

