# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution(object):
    def preorderRecurr(self, root, result):
        if not root:
            return

        result.append(root.val)
        for child in root.children:
            self.preorderRecurr(child, result)

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        result = []

        self.preorderRecurr(root, result)

        return result





if __name__ == '__main__':
    pass
