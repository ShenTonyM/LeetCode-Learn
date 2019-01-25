from Tree_Method import buildTree
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        last_layer_flag = False

        cur_layer = [root]

        while cur_layer:
            next_layer = []

            for node in cur_layer:
                if not node:
                    last_layer_flag = True
                    continue
                if last_layer_flag:
                    return False

                next_layer.append(node.left)
                next_layer.append(node.right)

            cur_layer = next_layer
        return True





if __name__ == '__main__':
    tree = buildTree([1,2,3,4,5,6])
    print(Solution().isCompleteTree(tree))