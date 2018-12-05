from collections import deque
from Tree_Method import TreeNode,buildTree
class Solution:
    def dfs(self, node, i, depth, leftmosts):
        if not node:
            return 0
        if depth >= len(leftmosts):
            leftmosts.append(i)
        return max(i - leftmosts[depth] + 1, self.dfs(node.left, i * 2, depth + 1, leftmosts),self.dfs(node.right, i * 2 + 1, depth + 1, leftmosts))
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leftmosts = []
        return self.dfs(root, 1, 0, leftmosts)


if __name__ == '__main__':
    # tree = buildTree([1,1,1,1,'null','null',1,1,'null','null','null','null','null','null',1])
    tree = buildTree([1,3,2,5,3,'null',9])
    print(Solution().widthOfBinaryTree(tree))