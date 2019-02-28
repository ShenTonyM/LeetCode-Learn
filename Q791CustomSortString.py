from collections import defaultdict
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """


        res = ''
        count = defaultdict(int)
        for i in range(len(T)):
            if T[i] in S:
                count[T[i]] += 1
            else:
                res += T[i]

        for j in  range(len(S)):
            if S[j] in count:
                res += count[S[j]] * S[j]

        return res


if __name__ == '__main__':
    print(Solution().customSortString("cba", "abcd"))