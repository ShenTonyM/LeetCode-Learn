# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        lengthA = 0
        lengthB = 0

        nodeA = headA
        nodeB = headB

        while nodeA:
            lengthA += 1
            nodeA = nodeA.next
        while nodeB:
            lengthB += 1
            nodeB = nodeB.next

        nodeA = headA
        nodeB = headB

        if lengthA > lengthB:
            diff = lengthA - lengthB
            while diff:
                nodeA = nodeA.next
                diff -= 1
        elif lengthA < lengthB:
            diff = lengthB - lengthA
            while diff:
                nodeB = nodeB.next
                diff -= 1

        while nodeA and nodeB:
            if nodeA is nodeB:
                return nodeA
            else:
                nodeA = nodeA.next
                nodeB = nodeB.next

        return None