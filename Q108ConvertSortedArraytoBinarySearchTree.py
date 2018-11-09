# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBSTRecur(self, nums, father_node, left_right_flag):
        if not nums:
            if left_right_flag == 'left':
                father_node.left = None
            elif left_right_flag == 'right':
                father_node.right = None
            return

        mid_index = len(nums) // 2
        mid_node = TreeNode(nums[mid_index])

        if left_right_flag == 'left':
            father_node.left = mid_node
        elif left_right_flag == 'right':
            father_node.right = mid_node


        self.sortedArrayToBSTRecur(nums[: mid_index], mid_node, 'left')
        if mid_index < len(nums):
            self.sortedArrayToBSTRecur(nums[mid_index + 1:], mid_node, 'right')


    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return None

        root_index = len(nums) // 2
        root_node = TreeNode(nums[root_index])

        self.sortedArrayToBSTRecur(nums[: root_index], root_node, 'left')
        self.sortedArrayToBSTRecur(nums[root_index + 1:], root_node, 'right')

        return root_node



    def traverseTree(self, root):
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
    root = Solution().sortedArrayToBST([-10,-3,0,5,9])
    Solution().traverseTree(root)