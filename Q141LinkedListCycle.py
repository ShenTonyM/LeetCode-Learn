# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         traverse = set()
#         node = head
#         while node.next:
#             if node in traverse:
#                 return False
#
#             traverse.add(node)
#             node = node.next
#         return True

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast, slow = head, head

        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

            if slow is fast:
                return True

        return False


if __name__ == "__main__":
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a1.next = a2
    a2.next = a3
    a3.next = None
    print(Solution().hasCycle(a1))