class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        lookup = {}
        for index, item1 in enumerate(list1):
            lookup[item1] = index

        smallest_index_sum = float('inf')
        result = []
        for index, item2 in enumerate(list2):
            if index > smallest_index_sum:
                break
            if item2 in lookup:
                index_sum = index + lookup[item2]
                if index_sum < smallest_index_sum:
                    smallest_index_sum = index_sum
                    result = [item2]
                elif index_sum == smallest_index_sum:
                    result.append(item2)

        return result


if __name__ == "__main__":
    print(Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]))