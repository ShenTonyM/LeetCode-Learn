# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from List_Method import ListNode, build_list

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1:
            if l2:
                head = tail = ListNode((l1.val + l2.val) % 10)
                carry = (l1.val + l2.val) // 10
            else:
                head = tail = ListNode(l1.val)

                node = l1.next
                while node:
                    new_node = ListNode(node.val)
                    tail.next = new_node
                    tail = new_node

                return head
        else:
            if l2:
                head = tail = ListNode(l2.val)

                node = l2.next
                while node:
                    new_node = ListNode(node.val)
                    tail.next = new_node
                    tail = new_node

                return head
            else:
                return None





if __name__ == '__main__':
    m1 = build_list([2,4,3])
    m2 = build_list([5,6,4])
    print(Solution().addTwoNumbers(m1, m2))