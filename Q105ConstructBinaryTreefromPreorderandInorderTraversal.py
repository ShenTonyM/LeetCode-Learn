from Tree_Method import TreeNode, level_order_traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTreeRecur(self, preorder, inorder, father_node, left_right_flag):
        if not preorder:
            if left_right_flag == 'left':
                father_node.left = None
            else:
                father_node.right = None
        else:
            root_val = preorder[0]
            root = TreeNode(root_val)

            if left_right_flag == 'left':
                father_node.left = root
            else:
                father_node.right = root


            root_index_inorder = inorder.index(root_val)

            if len(preorder) > 1:
                self.buildTreeRecur(preorder[1:root_index_inorder + 1], inorder[:root_index_inorder], root, 'left')
            else:
                self.buildTreeRecur([], [], root, 'left')
            if root_index_inorder < len(preorder) - 1:
                self.buildTreeRecur(preorder[root_index_inorder + 1:], inorder[root_index_inorder + 1:], root, 'right')
            else:
                self.buildTreeRecur([], [], root, 'right')


    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        root_index_inorder = inorder.index(root_val)

        if len(preorder) > 1:
            self.buildTreeRecur(preorder[1:root_index_inorder + 1], inorder[:root_index_inorder], root, 'left')
        else:
            self.buildTreeRecur([], [], root, 'left')
        if root_index_inorder < len(preorder) - 1:
            self.buildTreeRecur(preorder[root_index_inorder + 1:], inorder[root_index_inorder + 1:], root, 'right')
        else:
            self.buildTreeRecur([], [], root, 'right')


        return root






if __name__ == '__main__':
    tree = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
    level_order_traversal(tree)