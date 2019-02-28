class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        MAXNUM = 10 ** 9 + 7
        A = sorted(set(A))

        res = 0 
        root_tree_num = {}
        
        for num in A:
            root_new = 1
                      
            for prev_num in root_tree_num:
                if num % prev_num == 0 and num / prev_num in root_tree_num:
                    root_new += root_tree_num[prev_num] * root_tree_num[num / prev_num]

            root_tree_num[num] = root_new
            res += root_new

        return res % MAXNUM

if __name__ == '__main__':
    print(Solution().numFactoredBinaryTrees([46,144,5040,4488,544,380,4410,34,11,5,3063808,5550,34496,12,540,28,18,13,2,1056,32710656,31,91872,23,26,240,18720,33,49,4,38,37,1457,3,799,557568,32,1400,47,10,20774,1296,9,21,92928,8704,29,2162,22,1883700,49588,1078,36,44,352,546,19,523370496,476,24,6000,42,30,8,16262400,61600,41,24150,1968,7056,7,35,16,87,20,2730,11616,10912,690,150,25,6,14,1689120,43,3128,27,197472,45,15,585,21645,39,40,2205,17,48,136]))