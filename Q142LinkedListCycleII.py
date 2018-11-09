# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        intersect = None
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

            if slow is fast:
                intersect = slow
                break

        if intersect:
            node_1 = head
            node_2 = intersect
            while node_1.next:
                if node_1 is node_2:
                    return node_1
                node_1 = node_1.next
                node_2 = node_2.next

            return node_1





if __name__ == "__main__":
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a1.next = a2
    a2.next = a3
    a3.next = a2
    print(Solution().detectCycle(a1).val)