# from collections import deque
# class Solution(object):
#     def minAddToMakeValid(self, S):
#         """
#         :type S: str
#         :rtype: int
#         """
#
#         if not S:
#             return 0
#
#         result = 0
#         stack = []
#
#         for item in S:
#             if len(stack) == 0:
#                 stack.append(item)
#             else:
#                 if stack[-1] == '(':
#                     if item == ')':
#                         stack.pop()
#                     else:
#                         stack.append('(')
#                 else:
#                     if item == '(':
#                         stack.pop()
#                         stack.append(item)
#                         result += 1
#                     else:
#                         stack.pop()
#                         result += 2
#
#         result += len(stack)
#
#         return result

from collections import deque
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """

        if not S:
            return 0

        result = 0
        left_bracket = 0

        for item in S:
            if item == '(':
                left_bracket += 1
            else:
                if left_bracket:
                    left_bracket -= 1
                else:
                    result += 1

        return left_bracket + result


if __name__ == "__main__":
    print(Solution().minAddToMakeValid("()))(("))