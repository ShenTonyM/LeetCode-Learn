class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for chr in s:
            if chr in ['(', '[', '{']:
                stack.append(chr)
            else:
                if len(stack) <= 0:
                    return False
                else:
                    left = stack.pop()
                    if chr == ')' and left != '(':
                        return False
                    elif chr == ']' and left != '[':
                        return False
                    elif chr == '}' and left != '{':
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
if __name__ == '__main__':
    print(Solution().isValid("(]"))