from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTreesRecur(self, t1, t2, father, left_right_flag):
        if t1 and t2:
            t1.val += t2.val
            self.mergeTreesRecur(t1.left, t2.left, t1, "left")
            self.mergeTreesRecur(t1.right, t2.right, t1, "right")
            return
        elif t2:
            if left_right_flag == "left":
                father.left = t2
            elif left_right_flag == "right":
                father.right = t2
            return
        else:
            return

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if not t1 and  not t2:
            return None
        elif not t2:
            return t1
        elif not t1:
            return t2
        else:
            t1.val += t2.val
            self.mergeTreesRecur(t1.left, t2.left, t1, "left")
            self.mergeTreesRecur(t1.right, t2.right, t1, "right")
            return t1

    def level_order_traverse(self, root):
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
                if 2 * i + 1 < len(tree_data):
                    tree_node_list[i].left = tree_node_list[2 * i + 1]
                    if 2 * i + 2 < len(tree_data):
                        tree_node_list[i].right = tree_node_list[2 * i + 2]
                else:
                    tree_node_list[i].left = None
                    tree_node_list[i].right = None

        return tree_node_list[0]


if __name__ == "__main__":
    t1 = Solution().buildTree([1,3,2,5])
    # Solution().level_order_traverse(t1)
    t2 = Solution().buildTree([2,1,3,"null",4,"null",7])
    t_merge = Solution().mergeTrees(t1, t2)
    Solution().level_order_traverse(t_merge)