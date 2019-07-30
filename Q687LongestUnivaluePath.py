from Tree_Method import TreeNode


class Solution:
    def __init__(self):
        self.max_len = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not TreeNode:
            return 0

        self.longestUnivaluePathRecurr(root)

        return self.max_len

    def longestUnivaluePathRecurr(self, root):
        if not root:
            return 0

        left_path, right_path = 0, 0

        if root.left:
            left_sub_path = self.longestUnivaluePathRecurr(root.left)
            if root.left.val == root.val:
                left_path = left_sub_path + 1
            else:
                left_path = 0

        if root.right:
            right_sub_path = self.longestUnivaluePathRecurr(root.right)
            if root.right.val == root.val:
                right_path = right_sub_path + 1
            else:
                right_path = 0

        if left_path + right_path> self.max_len:
            self.max_len = left_path + right_path

        return max(left_path, right_path)


if __name__ == "__main__":
    TreeNode0_0 = TreeNode(1)
    TreeNode1_0 = TreeNode(4)
    TreeNode1_1 = TreeNode(5)
    TreeNode2_0 = TreeNode(4)
    TreeNode2_1 = TreeNode(4)
    TreeNode2_3 = TreeNode(5)

    TreeNode0_0.left = TreeNode1_0
    TreeNode0_0.right = TreeNode1_1
    TreeNode1_0.left = TreeNode2_0
    TreeNode1_0.right = TreeNode2_1
    TreeNode1_1.right = TreeNode2_3

    print(Solution().longestUnivaluePath(TreeNode0_0))
