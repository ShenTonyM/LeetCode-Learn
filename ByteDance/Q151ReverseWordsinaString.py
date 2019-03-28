class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = []
        words = []

        cur_w = ""

        for i in range(len(s)):
            # print(s[i], end='_')
            if s[i] != ' ':
                cur_w += s[i]
            else:
                if cur_w != '':
                    words.append(cur_w)
                cur_w = ''

        if cur_w != '':
            words.append(cur_w)
        # words = s.split(' ')
        # print(words)
        for i in range(len(words) -1, -1, -1):
            res.append(words[i])

        res_str = " ".join(res)
        # res_str = res_str.strip()

        return res_str


if __name__ == "__main__":
    print(Solution().reverseWords("a good   example"))