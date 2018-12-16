from Tree_Method import TreeNode, buildTree, level_order_traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        root.right, root.left = root.left, root.right

        if root and root.left:
            self.invertTree(root.left)

        if root and root.right:
            self.invertTree(root.right)

        return root

if  __name__ == '__main__':
    tree = buildTree([4,2,7,1,3,6,9])
    tree_reverse = Solution().invertTree(tree)
    level_order_traversal(tree_reverse)