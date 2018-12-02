class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """

        first, second, third, fourth = 0,0,0,0

        under_one = []
        two = []
        under_three = []
        under_five = []

        for num in A:
            if num <= 1:
                under_one.append(num)
            elif num == 2:
                two.append(num)

            if num <= 3:
                under_three.append(num)

            if num <= 5:
                under_five.append(num)


        if len(two) >= 1 and len(under_three) >= 2 and len(under_five) >= 3:
            first = 2

            under_three.remove(first)
            second = max(under_three)

            under_five.remove(first)
            under_five.remove(second)
            third = max(under_five)

            A.remove(first)
            A.remove(second)
            A.remove(third)
            fourth = A[0]

            return str(first) + str(second) + ':' + str(third) + str(fourth)

        elif len(under_one) >= 1 and len(under_five) >= 2:
            first = max(under_one)

            A.remove(first)
            second = max(A)

            under_five.remove(first)
            if second <= 5:
                under_five.remove(second)
            third = max(under_five)

            A.remove(second)
            A.remove(third)
            fourth = A[0]

            return str(first) + str(second) + ':' + str(third) + str(fourth)

        else:
            return ''


if __name__ == '__main__':
    print(Solution().largestTimeFromDigits([1,9,0,6]))