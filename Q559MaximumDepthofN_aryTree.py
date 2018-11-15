# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        max_children = 0
        for child in root.children:
            child_depth = self.maxDepth(child)
            if max_children < child_depth:
                max_children = child_depth
        return max_children + 1
