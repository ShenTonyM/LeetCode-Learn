# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        node = node_nlast = head

        # 两个定位点
        m = n
        while m != 0 and node_nlast.next:
            node_nlast = node_nlast.next
            m -= 1

        # 要删除的就是头结点
        if m != 0:
            head = head.next
            return head
        else:
            while node_nlast and node_nlast.next:
                node = node.next
                node_nlast = node_nlast.next


            # 删除node
            if node.next.next:
                node.next = node.next.next
            else:
                node.next = None
            return head


if __name__ == '__main__':
    m = ListNode(1)
    # m.next = ListNode(5)
    result = Solution().removeNthFromEnd(m, 1)
    # result = m
    while result:
        print(result.val)
        result = result.next