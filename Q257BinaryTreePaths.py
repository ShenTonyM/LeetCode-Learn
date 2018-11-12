from Tree_Method import buildTree, level_order_traversal
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePathsRec(self, root, path, result):

        if not root.left and not root.right:
            path_str = ''
            for node in path[:-1]:
                path_str = path_str + str(node.val) + '->'
            path_str += str(root.val)
            result.append(path_str)

        if root.left:
            path.append(root.left)
            self.binaryTreePathsRec(root.left, path, result)
            path.pop()

        if root.right:
            path.append(root.right)
            self.binaryTreePathsRec(root.right, path, result)
            path.pop()



    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        result = []
        path = []
        path.append(root)

        self.binaryTreePathsRec(root, path, result)

        return result

if __name__ == '__main__':
    tree = buildTree([1,2,3,"null",5])
    print(Solution().binaryTreePaths(tree))