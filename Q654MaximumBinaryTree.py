# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTreeRecur(self, nums, father_node, left_right_flag):
        if not nums:
            if left_right_flag == 'left':
                father_node.left = None
            elif left_right_flag == 'right':
                father_node.right = None
            return

        max_number = max(nums)
        max_node = TreeNode(max_number)
        max_index = nums.index(max_number)

        if left_right_flag == 'left':
            father_node.left = max_node
        elif left_right_flag == 'right':
            father_node.right = max_node

        self.constructMaximumBinaryTreeRecur(nums[: max_index], max_node, 'left')
        if max_index < len(nums):
            self.constructMaximumBinaryTreeRecur(nums[max_index + 1:], max_node, 'right')

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return None

        root_number = max(nums)
        root_node = TreeNode(root_number)
        root_index = nums.index(root_number)

        self.constructMaximumBinaryTreeRecur(nums[:root_index], root_node, "left")
        self.constructMaximumBinaryTreeRecur(nums[root_index + 1:], root_node, "right")

        return root_node


    def level_order_traverse(self, root):
        """
        :type root: TreeNode
        :rtype: None
        """
        tree_node_list = deque()
        tree_node_list.append(root)

        while tree_node_list:
            root = tree_node_list.popleft()
            if root.left:
                tree_node_list.append(root.left)
            if root.right:
                tree_node_list.append(root.right)
            print(root.val)

        return

if __name__ == "__main__":
    tree = Solution().constructMaximumBinaryTree([3,2,1,6,0,5])
    Solution().level_order_traverse(tree)