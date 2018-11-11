class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        diff = []

        for i in range(len(A)):
            if A[i] != B[i]:
                diff.append((A[i], B[i]))
                if len(diff) > 2:
                    return False

        if len(diff) == 1:
            return False
        elif len(diff) == 0:
            return len(set(A)) != len(A)
        else:
            return diff[0] == (diff[1][1],  diff[1][0])



if __name__ == "__main__":
    print(Solution().buddyStrings("ab", "ba"))