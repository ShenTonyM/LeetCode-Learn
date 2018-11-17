class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """

        left_right_flag = 1
        plus_minus_flag = 1
        x_coeff = 0
        constant_coeff = 0

        i = 0

        while i != len(equation):
            item = ''
            while i != len(equation) and equation[i] not in ['+', '-', '=']:
                item += equation[i]
                i += 1

            # first position minus
            if not item:
                plus_minus_flag = -1
            # normal x_coeff
            elif item[-1] == 'x':
                if len(item) == 1:
                    curr_coeff = 1
                else:
                    curr_coeff = int(item[:-1])
                x_coeff += left_right_flag * plus_minus_flag * curr_coeff
            # constant_coeff
            else:
                curr_coeff = int(item)
                constant_coeff += left_right_flag * plus_minus_flag * curr_coeff

            if i == len(equation):
                break

            if equation[i] == '-':
                plus_minus_flag = -1
            elif equation[i] == '+':
                plus_minus_flag = 1
            elif equation[i] == '=':
                left_right_flag = -1
                plus_minus_flag = 1

            i += 1

        if not x_coeff and not constant_coeff:
            return "Infinite solutions"
        if not x_coeff:
            return "No solution"

        return 'x=' + str(-constant_coeff // x_coeff)


if __name__ == '__main__':
    print(Solution().solveEquation("-x=-1"))