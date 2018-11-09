# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
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

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

if __name__ == "__main__":
    tree = Solution().buildTree([3,9,20,"null","null",15,7])
    # Solution().traverseTree(tree)
    print(Solution().maxDepth(tree))