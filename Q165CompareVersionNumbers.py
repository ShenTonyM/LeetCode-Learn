class Solution:
    def compareVersion(self, version1: 'str', version2: 'str') -> 'int':
        v_split_1, v_split_2 = version1.split('.'), version2.split('.')

        i, j = 0, 0

        while i != len(v_split_1) and j != len(v_split_2):
            v1, v2 = int(v_split_1[i]), int(v_split_2[i])
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

            i += 1
            j += 1

        if len(v_split_1) == len(v_split_2):
            return 0
        elif i == len(v_split_1):
            v2_rest = int(''.join(v_split_2[j:]))
            if v2_rest:
                return -1
            else:
                return 0
        elif j == len(v_split_2):
            v1_rest = int(''.join(v_split_1[i:]))
            if v1_rest:
                return 1
            else:
                return 0




if __name__ == '__main__':
    print(Solution().compareVersion(version1 = "1.0", version2 = "1.0.0"))