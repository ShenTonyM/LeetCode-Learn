from Tree_Method import buildTree, TreeNode,level_order_traversal
class Solution:
    def flipEquivRecur(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        # 确保左右子树都存在
        if root1.left and root1.right and root2.left and root2.right:
            if root1.left.val == root2.left.val and root1.right.val == root2.right.val:
                return self.flipEquivRecur(root1.left, root2.left) and self.flipEquivRecur(root1.right, root2.right)
            elif root1.right.val == root2.left.val and root1.left.val == root2.right.val:
                return self.flipEquivRecur(root1.right, root2.left) and self.flipEquivRecur(root1.left, root2.right)
            else:
                return False

        elif root1.left:
            if root2.left and not root2.right:
                if root1.left.val == root2.left.val:
                    return self.flipEquivRecur(root1.left, root2.left)
                else:
                    return False
            elif root2.right and not root2.left:
                if root1.left.val == root2.right.val:
                    return self.flipEquivRecur(root1.left, root2.right)
                else:
                    return False
            else:
                return False
        elif root1.right:
            if root2.left and not root2.right:
                if root1.right.val == root2.left.val:
                    return self.flipEquivRecur(root1.right, root2.left)
                else:
                    return False
            elif root2.right and not root2.left:
                if root1.right.val == root2.right.val:
                    return self.flipEquivRecur(root1.right, root2.right)
                else:
                    return False
            else:
                return False
        else:
            if not root2.left and not root2.right:
                return True
            else:
                return False



    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        elif root1 and not root2:
            return False
        elif root2 and not root1:
            return False
        elif root1.val == root2.val:
            return self.flipEquivRecur(root1, root2)
        else:
            return False



if __name__ == '__main__':
    tree1 = buildTree([0,2,1,'null',3,'null',5,'null',4])
    tree2 = buildTree([0,'null',2,3,'null','null',4])
    # level_order_traversal(tree1)
    # level_order_traversal(tree2)
    print(Solution().flipEquiv(tree1, tree2))