class Solution:
    def binarySearch(self,arr, x):
        min_i, max_i = 0, len(arr) - 1
        while min_i <= max_i:
            mid_index = (min_i + max_i) // 2
            if arr[mid_index] < x:
                min_i = mid_index + 1
            elif arr[mid_index] > x:
                max_i = mid_index - 1
            else:
                return mid_index

        return min_i

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        if k == len(arr):
            return arr

        min_index = max_index = self.binarySearch(arr, x)

        while min_index != 0 and max_index != len(arr) - 1 and max_index - min_index < k:
            if abs(arr[min_index] - x) <= abs(arr[max_index] - x):
                min_index -= 1
            else:
                max_index += 1

        print(min_index, max_index)

        if min_index == 0:
            if abs(arr[0] - x) <= abs(arr[k] - x):
                return arr[:k]
            else:
                return arr[1:k+1]


        if max_index == len(arr) - 1:
            if abs(arr[-k - 1] - x) <= abs(arr[-1] - x):
                return arr[-k - 1: - 1]
            else:
                return arr[-k:]

        if abs(arr[min_index] - x) <= abs(arr[max_index] - x):
            return arr[min_index: max_index]
        else:
            return arr[min_index + 1: max_index + 1]








if __name__ == '__main__':
    print(Solution().findClosestElements([1],1,1))