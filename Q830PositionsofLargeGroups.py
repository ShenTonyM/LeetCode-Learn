class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        if not S:
            return False

        result = []
        flag = S[0]
        start = 0

        for i in range(1, len(S)):
            if flag != S[i]:
                count = i - start
                if count >= 3:
                    result.append([start, i - 1])
                flag = S[i]
                start = i
        count = len(S) - start
        if count >= 3:
            result.append([start, len(S) - 1])

        return result




if __name__ == '__main__':
    print(Solution().largeGroupPositions("abbxxxxzzy"))