from collections import Counter
class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        cnts = [Counter(i) for i in ['zero','one','two','three','four','five','six','seven','eight','nine']]
        number_decimal = [0, 2, 4, 6, 8, 5, 3, 7, 1, 9]
        number_represent = ['z', 'w', 'u', 'x', 'g', 'f', 'h', 's', 'o', 'i']

        c = Counter(list(s))
        result = []

        for i in range(len(number_decimal)):
            while c[number_represent[i]] > 0:
                c.subtract(cnts[number_decimal[i]])
                result.append(number_decimal[i])

        return "".join(map(str, sorted(result)))

if __name__ == '__main__':
    print(Solution().originalDigits("owoztneoer"))