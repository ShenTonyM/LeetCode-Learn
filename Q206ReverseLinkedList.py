# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        head_node = head
        next_node = head.next

        # 现将末尾的next置为None
        head_node.next = None

        while next_node:
            temp_next_node = next_node
            next_node = next_node.next
            temp_next_node.next = head_node
            head_node = temp_next_node

        return head_node


class Solution2:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next


if __name__ == '__main__':
    m = ListNode(1)
    n = ListNode(2)
    p = ListNode(3)
    q = ListNode(4)
    m.next = n
    n.next = p
    p.next = q
    result = Solution2().reverseList(m)

    while result:
        print(result.val)
        result = result.next