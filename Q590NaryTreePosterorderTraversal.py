"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        stack = []
        output = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)

            for item in node.children:
                stack.append(item)

        return output[::-1]