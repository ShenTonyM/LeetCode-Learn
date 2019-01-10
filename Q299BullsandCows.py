from collections import defaultdict
class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        lookup = defaultdict(int)
        visited = [False]*len(secret)
        bulls, cows = 0, 0

        for letter in secret:
            lookup[letter] += 1

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                lookup[guess[i]] -= 1
                visited[i] = True

        for i in range(len(secret)):
            if not visited[i]:
                if lookup[guess[i]]:
                    cows += 1
                    lookup[guess[i]] -= 1

        return str(bulls) + 'A' + str(cows) + 'B'

if __name__ == '__main__':
    print(Solution().getHint("1123","0111"))