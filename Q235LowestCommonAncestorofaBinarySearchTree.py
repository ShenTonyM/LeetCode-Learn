from Tree_Method import TreeNode, buildTree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFatherRecur(self, root, p, q):
        if (root.val < p.val and root.val > q.val or root.val > p.val and root.val < q.val):
            return root
        if root.val == p.val or root.val == q.val:
            return root

        if root.val < p.val and root.val < q.val:
            return self.findFatherRecur(root.right, p, q)
        else:
            return self.findFatherRecur(root.left, p, q)
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        return self.findFatherRecur(root, p, q)




if __name__ == '__main__':
    tree = buildTree([6,2,8,0,4,7,9,'null','null',3,5])
    p, q = TreeNode(2), TreeNode(8)
    print(Solution().lowestCommonAncestor(tree,p,q))