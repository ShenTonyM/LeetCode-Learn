class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        rows = [B,D,F,H]
        cols = [A,C,E,G]

        area1 = abs((C-A)*(D-B))
        area2 = abs((G-E)*(H-F))

        if  F >= D or H <= B or E >= C or G <= A:
            return area1 + area2


        rows = sorted(rows)
        cols = sorted(cols)

        up, down = rows[1], rows[2]
        left, right = cols[1], cols[2]

        area_overlap = abs((down-up)*(right-left))

        return area1 + area2 - area_overlap



if __name__ == '__main__':
    print(Solution().computeArea(-2,-2,2,2,3,3,4,4))