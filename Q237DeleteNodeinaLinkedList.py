# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        q = node.next
        p.val = q.val
        p.next = q.next
        del q



if __name__ == '__main__':
    print(Solution().deleteNode([4,5,1,9]))