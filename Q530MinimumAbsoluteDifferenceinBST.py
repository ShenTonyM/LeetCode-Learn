from Tree_Method import TreeNode, buildTree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifferenceRecur(self, root, data):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return

        self.getMinimumDifferenceRecur(root.left, data)
        data.append(root.val)
        self.getMinimumDifferenceRecur(root.right, data)


    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        data = []

        self.getMinimumDifferenceRecur(root, data)

        min_diff = float('inf')

        for i in range(1, len(data)):
            if data[i] - data[i - 1] < min_diff:
                min_diff = data[i] - data[i - 1]

        return min_diff

if __name__ == '__main__':
    nums= [1,'null',3,2]
    root = buildTree(nums)
    print(Solution().getMinimumDifference(root))
