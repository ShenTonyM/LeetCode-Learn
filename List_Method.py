# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


def display_ListNode(head):
    node = head
    while node:
        if node.next:
            print(str(node.val) + '->', end='')
        else:
            print(str(node.val))
        node = node.next


def build_list(n):
    if n == 0:
        return None

    m = ListNode(6 - n)
    m.next = build_list(n - 1)
    return m
