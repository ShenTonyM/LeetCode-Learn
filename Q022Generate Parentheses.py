class Solution(object):
    def generateParenthesisReccur(self,n, left, right, parenthese, result):
        if left == n and right == n:
            result.append(parenthese)
            return
        elif left == n:
            self.generateParenthesisReccur(n, left, right+1, parenthese + ')', result)
            return

        if left == right:
            self.generateParenthesisReccur(n, left + 1, right, parenthese + '(', result)
            return
        else:
            self.generateParenthesisReccur(n, left + 1, right, parenthese + '(', result)

            self.generateParenthesisReccur(n, left, right + 1, parenthese + ')', result)
            return

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []

        self.generateParenthesisReccur(n, 0, 0, '', result)

        return result



if __name__ == '__main__':
    print(Solution().generateParenthesis(3))