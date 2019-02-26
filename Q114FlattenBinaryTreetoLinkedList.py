from Tree_Method import TreeNode,buildTree, level_order_traversal
from List_Method import display_ListNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flattenReccur(self, root:TreeNode):
        if root.left and root.right:
            right_element = root.right

            root.right = root.left
            root.left = None
            tail = self.flattenReccur(root.right)

            tail.right = right_element
            tail.left = None
            return self.flattenReccur(tail.right)
        elif root.left:
            root.right = root.left
            root.left = None
            return self.flattenReccur(root.right)

        elif root.right:
            return self.flattenReccur(root.right)
        else:
            return root

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return None
        return self.flattenReccur(root)


if __name__ == '__main__':
    tree = buildTree([1,2,5,3,4,"null",6])
    new_head = Solution().flatten(tree)
    level_order_traversal(new_head)