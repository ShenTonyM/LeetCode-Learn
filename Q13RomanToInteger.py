class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        codeTable = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        prev = float('inf')
        total = 0

        for letter in s:
            n = codeTable[letter]
            if n <= prev:
                total += n
            else:
                total = total + n - 2* prev
            prev = n
        return total

if __name__ == '__main__':
    print(Solution.romanToInt(Solution, "IV"))