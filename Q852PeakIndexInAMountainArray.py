class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        prev = float("-inf")
        status = 'up'
        num = len(A)
        for i in range(num):
            if status == 'up':
                if A[i] < prev:
                    return i-1
                else:
                    prev = A[i]



if __name__ == '__main__':
    print(Solution().peakIndexInMountainArray([0,2,1,0]))