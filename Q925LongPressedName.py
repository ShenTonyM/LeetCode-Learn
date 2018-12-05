class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """

        i = 0
        j = 0

        while i != len(name) and j != len(typed):
            char_name = name[i]
            count_char_name = 0
            while i != len(name) and name[i] == char_name:
                i += 1
                count_char_name += 1

            char_typed = typed[j]
            count_char_typed = 0
            while j != len(typed)and typed[j] == char_typed:
                j += 1
                count_char_typed += 1

            if char_name != char_typed or count_char_name > count_char_typed:
                return False

        if i != len(name) or j != len(typed):
            return False
        else:
            return True



if __name__ == '__main__':
    print(Solution().isLongPressedName("saeed", "ssaaedd"))