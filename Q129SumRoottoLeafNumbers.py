# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Tree_Method import TreeNode, buildTree
class Solution:
    def __init__(self):
        self._path_sum = 0

    def sumNumbersRecur(self, root, prev_num):
        cur_num = prev_num*10 + root.val
        if root.left and root.right:
            self.sumNumbersRecur(root.left, cur_num)
            self.sumNumbersRecur(root.right, cur_num)
        elif root.left:
            self.sumNumbersRecur(root.left, cur_num)
        elif root.right:
            self.sumNumbersRecur(root.right, cur_num)
        else:
            self._path_sum += cur_num

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        cur_num = root.val

        if root.left and root.right:
            self.sumNumbersRecur(root.left, cur_num)
            self.sumNumbersRecur(root.right, cur_num)
        elif root.left:
            self.sumNumbersRecur(root.left, cur_num)
        elif root.right:
            self.sumNumbersRecur(root.right, cur_num)
        else:
            self._path_sum += cur_num

        return self._path_sum


if __name__ == '__main__':
    tree = buildTree([1,2,3])
    print(Solution().sumNumbers(tree))

