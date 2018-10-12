# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next

        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] != nums[end]:
                return False

            start += 1
            end -= 1

        return True


if __name__ == "__main__":
    m = ListNode(0)
    n = ListNode(0)
    # p = ListNode(1)
    # q = ListNode(0)
    m.next = n
    # n.next = p
    # p.next = q
    print(Solution().isPalindrome(m))
    # result = Solution().isPalindrome(m)
    #
    # while result:
    #     print(result.val)
    #     result = result.next