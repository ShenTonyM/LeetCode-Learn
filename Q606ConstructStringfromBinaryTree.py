from Tree_Method import TreeNode, buildTree
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ""
        s = str(t.val)
        if t.left or t.right:
            s += "(" + self.tree2str(t.left) + ")"
        if t.right:
            s += "(" + self.tree2str(t.right) + ")"
        return s



if __name__ == '__main__':
    tree = buildTree([1,2,3,'null',4])
    print(Solution().tree2str(tree))