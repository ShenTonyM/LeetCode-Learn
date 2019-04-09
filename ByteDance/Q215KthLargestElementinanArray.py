import heapq
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # hp = heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]

if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))