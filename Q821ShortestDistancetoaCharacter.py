class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        index_C = []

        for i in range(len(S)):
            if S[i] == C:
                index_C.append(i)

        flags = []

        for i in range(len(index_C) - 1):
            flags.append((index_C[i] + index_C[i+1]) // 2)
        flags.append(len(S))

        result = []
        index = 0
        for i in range(len(S)):
            if i <= flags[index]:
                result.append(abs(index_C[index] - i))
            else:
                index += 1
                result.append(abs(index_C[index] - i))

        return result


if __name__ == '__main__':
    print(Solution().shortestToChar("loveleetcode", "e"))