import Tree_Method
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        if self is None:
            return None
        return "val:{} -> next:{}".format(self.val, repr(self.next))

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        if root.left and root.right:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)


if __name__ == "__main__":
    tree = Tree_Method.buildTree([1,2,3,4,5,6,7])
    # Solution().connect(tree)
