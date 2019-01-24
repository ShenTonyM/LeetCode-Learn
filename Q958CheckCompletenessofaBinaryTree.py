from Tree_Method import buildTree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """



if __name__ == '__main__':
    tree = buildTree([1,2,3,4,5,6])
    print(Solution().isCompleteTree(tree))