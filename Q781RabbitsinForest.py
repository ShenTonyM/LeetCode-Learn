from collections import defaultdict
from math import ceil
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """

        category = defaultdict(int)

        for num in answers:
            category[num] += 1

        result = 0

        for item in category:
            # if category[item] <= item + 1:
            #     result += item + 1
            # else:
            #     while category[item] > item + 1:
            #         result += item + 1
            #         category[item] -= (item + 1)
            #     result += item + 1
            result += int(ceil(category[item] / (item + 1)) * (item + 1))

        return result




if __name__ == '__main__':
    print(Solution().numRabbits([0,0,1,1,1]))