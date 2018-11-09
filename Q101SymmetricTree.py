# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def isEqual(self, left_tree, right_tree):
        if not left_tree and not right_tree:
            return True
        elif not left_tree or not right_tree or left_tree.val != right_tree.val:
            return False

        return self.isEqual(left_tree.right, right_tree.left) and self.isEqual(left_tree.left, right_tree.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.isEqual(root.left, root.right)



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


class Solution2(object):
    def isSymmetric(self, root):
        if not root:
            return True

        stack = []
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            p, q = stack.pop(), stack.pop()

            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False

            stack.append(p.left)
            stack.append(q.right)

            stack.append(p.right)
            stack.append(q.left)

        return True


if __name__ == "__main__":
    tree = Solution1().buildTree([1, 2, 2, 3, 4, 4, 3])
    # Solution().traverseTree(tree)
    print(Solution2().isSymmetric(tree))