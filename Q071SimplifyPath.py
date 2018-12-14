class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for tok in path.split('/'):
            if tok == "..":
                if stack:
                    stack.pop()
            elif tok and tok != '.':
                stack.append(tok)
        return '/'+'/'.join(stack)

if __name__ == '__main__':
    print(Solution().simplifyPath("/a/./b/../../c/"))