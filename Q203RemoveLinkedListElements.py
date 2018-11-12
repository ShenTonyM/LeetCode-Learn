# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self == None:
            return None
        else:
            return str(self.val) + '->' + repr(self.next)

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        # 去除头部的几点
        while head:
            if head.val == val:
                head = head.next
            else:
                break

        node = head

        if not head:
            return None

        while node.next and node.next.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next


        if node.next and node.next.val == val:
            node.next = None

        return head


if __name__ == '__main__':
    m1 = ListNode(1)
    m2 = ListNode(2)
    m3 = ListNode(2)
    m4 = ListNode(1)
    m5 = ListNode(4)
    m6 = ListNode(5)
    m7 = ListNode(6)
    m1.next = m2
    m2.next = m3
    m3.next = m4
    # m4.next = m5
    # m5.next = m6
    # m6.next = m7

    m8 = ListNode(1)

    print(Solution().removeElements(m1, 2))