from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBSTRecurrent(self, root, min_number, max_number):

        if not root:
            return True

        return root.val < max_number and root.val > min_number and \
               self.isValidBSTRecurrent(root.left, min_number, root.val) and \
               self.isValidBSTRecurrent(root.right, root.val, max_number)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTRecurrent(root, float('-inf'), float('inf'))

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

        # for item in tree_node_list:
        #     print(item.val)

        return tree_node_list[0]


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
    tree = Solution().buildTree([2,1,3])
    # Solution().traverseTree(tree)
    print(Solution().isValidBST(tree))