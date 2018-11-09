# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        node_stack = deque()
        node_stack.append({"tree_node":root,"level":0})
        display = []
        current_level = -1
        while node_stack:
            item = node_stack.popleft()
            " Add nodes to node_stack"
            if item["tree_node"].left:
                node_stack.append({"tree_node":item["tree_node"].left, "level":item["level"] + 1})
            if item["tree_node"].right:
                node_stack.append({"tree_node":item["tree_node"].right, "level":item["level"] + 1})

            "Add result to display"
            if item["level"] != current_level:
                display.append([item["tree_node"].val])
                current_level += 1
            else:
                display[-1].append(item["tree_node"].val)

        return display


    def buildTree(self, tree_data):
        """
        :type tree_data: list
        :rtype: TreeNode
        """

        tree_node_list = []
        for i in range(len(tree_data)):
            if tree_data[i] != 'null':
                tree_node_list.append(TreeNode(tree_data[i]))
            else:
                tree_node_list.append(None)

        for i in range(len(tree_data)):
            if tree_node_list[i]:
                if 2 * i + 2 < len(tree_data):
                    tree_node_list[i].left = tree_node_list[2 * i + 1]
                    tree_node_list[i].right = tree_node_list[2 * i + 2]
                else:
                    tree_node_list[i].left = None
                    tree_node_list[i].right = None

        return tree_node_list[0]


if __name__ == "__main__":
    tree = Solution().buildTree([1, 2, 2, 3, 4, 4, 3])
    # Solution().traverseTree(tree)
    print(Solution().levelOrder(tree))