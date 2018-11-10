# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version >= 4

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_false = 0
        min_true = n

        while max_false < min_true - 1:
            mid_point = (min_true - max_false) // 2 + max_false
            result = isBadVersion(mid_point)

            if result:
                min_true = mid_point
            else:
                max_false = mid_point

        return min_true

if __name__ == "__main__":

    print(Solution().firstBadVersion(5))