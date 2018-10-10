class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        string = str.lstrip()

        candidate = ''
        for index, chr in enumerate(string):
            if chr in ['-', '+']:
                if index == 0:
                    candidate += chr
                else:
                    break
            elif chr.isdigit():
                candidate += chr
            else:
                break


        if candidate in ['', '+', '-']:
            return 0
        else:
            number = int(candidate)
            if number > 2**31 - 1:
                return 2**31 - 1
            elif number < -2**31:
                return -2**31
            else:
                return number


if __name__ == "__main__":
    s = "-4193 with words"
    print(Solution().myAtoi(s))