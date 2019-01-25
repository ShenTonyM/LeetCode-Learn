from Tree_Method import buildTree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquivReccur(self, root1, root2):
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (root1 and not root2):
            return False
        if root1.val != root2.val:
            return False

        return (self.flipEquivReccur(root1.left, root2.left) and self.flipEquivReccur(root1.right, root2.right)) or \
               (self.flipEquivReccur(root1.left, root2.right) and self.flipEquivReccur(root1.right, root2.left))
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.flipEquivReccur(root1, root2)



if __name__ == '__main__':
    tree1 = buildTree([1,2,3,4,5,6,'null','null','null',7,8])
    tree2 = buildTree([1,3,2,'null',6,4,5,'null','null','null','null',8,7])
    print(Solution().flipEquiv(tree1, tree2))