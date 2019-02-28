class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        num_str = str(num)
        num_list = list(map(int, num_str))

        num_place = [[i, item] for i, item in enumerate(num_list)]

        num_sort = sorted(num_place, key=lambda x:(x[1], -x[0]), reverse=True)

        cur_index = 0

        for i in range(len(num_sort)):
            item = num_sort[i]
            if item[0] != cur_index:
                for j in range(i, len(num_sort)):
                    if num_sort[j][1] != item[1]:
                        num_list[cur_index], num_list[num_sort[j-1][0]] = num_list[num_sort[j-1][0]], num_list[cur_index]
                        return int(''.join(map(str, num_list)))
            else:
                cur_index += 1

        return num

if __name__ == '__main__':
    print(Solution().maximumSwap(1993))