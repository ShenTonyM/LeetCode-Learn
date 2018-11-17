from Tree_Method import TreeNode, level_order_traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTreeRecur(self, inorder, postorder, father_node, left_right_flag):
        root_val = postorder[-1]
        root_inorder_index = inorder.index(root_val)

        root_node = TreeNode(root_val)

        if left_right_flag == 'left':
            father_node.left = root_node
        else:
            father_node.right = root_node

        if root_inorder_index != 0:
            left_inorder_list = inorder[:root_inorder_index]
            left_postorder_list = postorder[:root_inorder_index]
            self.buildTreeRecur(left_inorder_list, left_postorder_list, root_node, 'left')
        else:
            root_node.left = None

        if root_inorder_index != len(inorder) - 1:
            right_inorder_list = inorder[root_inorder_index + 1:]
            right_postorder_list = postorder[root_inorder_index:-1]
            self.buildTreeRecur(right_inorder_list, right_postorder_list, root_node, 'right')
        else:
            root_node.right = None

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if not inorder:
            return None

        root_val = postorder[-1]
        root_inorder_index = inorder.index(root_val)

        root_node = TreeNode(root_val)

        if root_inorder_index != 0:
            left_inorder_list = inorder[:root_inorder_index]
            left_postorder_list = postorder[:root_inorder_index]
            self.buildTreeRecur(left_inorder_list, left_postorder_list, root_node, 'left')
        else:
            root_node.left = None

        if root_inorder_index != len(inorder) - 1:
            right_inorder_list = inorder[root_inorder_index + 1:]
            right_postorder_list = postorder[root_inorder_index:-1]
            self.buildTreeRecur(right_inorder_list, right_postorder_list, root_node, 'right')
        else:
            root_node.right = None

        return root_node


if __name__ == '__main__':
    tree = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    level_order_traversal(tree)
