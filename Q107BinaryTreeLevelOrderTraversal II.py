from Tree_Method import TreeNode, buildTree
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        # 先正向层序遍历
        result_forward = []
        node_current_layer, node_next_layer = deque(), deque()
        node_current_layer.append(root)

        node_current_data = []

        while node_current_layer or node_next_layer:
            node = node_current_layer.popleft()
            node_current_data.append(node.val)
            if node.left:
                node_next_layer.append(node.left)
            if node.right:
                node_next_layer.append(node.right)

            if not node_current_layer:
                node_current_layer = node_next_layer
                node_next_layer = deque()
                result_forward.append(node_current_data)
                node_current_data = []

        return result_forward[::-1]



if __name__ == '__main__':
    tree = buildTree([3,9,20,'null','null',15,7])
    print(Solution().levelOrderBottom(tree))
