morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        word_dict = set()
        for word in words:
            word_decode = ''
            for letter in word:
                loc = ord(letter) - ord('a')
                decode_morse = morse[loc]
                word_decode += decode_morse
            word_dict.add(word_decode)

        return len(word_dict)



if __name__ == '__main__':
    print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))