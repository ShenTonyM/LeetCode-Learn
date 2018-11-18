class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        result = [0] * (len(S) + 1)

        last_I = 0

        for i in range(1, len(S) + 1):
            if S[i - 1] == 'I':
                result[i] = i
                last_I = i
            else:
                result[last_I + 1:i + 1] = result[last_I:i]
                result[last_I] = i

        return result


if __name__ == '__main__':
    print(Solution().diStringMatch("IDID"))