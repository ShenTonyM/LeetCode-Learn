# naive model O(n) = n^2, exceed time limit
class Solution1:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = float('-inf')
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                cur_area = min(height[j], height[i]) * (j - i)
                if cur_area > max_area:
                    max_area = cur_area

        return max_area

# DP
class Solution2:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0
        left, right = 0, len(height) - 1

        while left != right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area




if __name__ == '__main__':
    print(Solution2().maxArea([1,8,6,2,5,4,8,3,7]))