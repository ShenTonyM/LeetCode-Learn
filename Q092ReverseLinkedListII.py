from List_Method import ListNode, display_ListNode, build_list
class Solution1:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if m == n:
            return head

        virtual_head = ListNode(-1)
        virtual_head.next = head


        index = 1
        node = virtual_head
        while index != m:
            node = node.next
            index += 1

        prev = node
        node1_head, node1_tail = node.next, node.next
        node2 = node.next.next
        succ =  node.next.next.next

        while True:
            prev.next = node2
            node2.next = node1_head
            node1_tail.next = succ

            index += 1
            if index == n:
                break

            prev = prev
            node1_head, node1_tail = node2, node1_tail
            node2 = succ
            succ = succ.next


        return virtual_head.next


class Solution2:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        diff, dummy, cur = n - m + 1, ListNode(-1), head
        dummy.next = head

        last_unswapped = dummy
        while cur and m > 1:
            cur, last_unswapped, m = cur.next, cur, m - 1

        prev, first_swapped = last_unswapped, cur
        while cur and diff > 0:
            cur.next, prev, cur, diff = prev, cur, cur.next, diff - 1

        last_unswapped.next, first_swapped.next = prev, cur

        return dummy.next


if __name__ == '__main__':

    head = build_list(5)
    # while node:
    #     if node.next:
    #         print(str(node.val) + '->', end='')
    #     else:
    #         print(str(node.val))
    #     node = node.next
    display_ListNode(head)

    new_head = Solution1().reverseBetween(head, 2, 4)

    display_ListNode(new_head)