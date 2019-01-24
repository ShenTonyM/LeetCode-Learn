from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)

def buildTree(tree_data):
    """
    :type tree_data: list
    :rtype: TreeNode
    """

    # convert the list representation to TreeNode
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

def level_order_traversal(root):
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
        print(root)

    return