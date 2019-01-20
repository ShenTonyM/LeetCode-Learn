import time
from collections import defaultdict,Counter

class User:
    def __init__(self):
        self.followee = set()
        self.tweet = dict()

    def postTweet(self, tweetId):
        time.sleep(0.0001)
        self.tweet[time.time()] = tweetId

    def follow(self, followeeId):
        self.followee.add(followeeId)

    def unfollow(self, followeeId):
        self.followee.discard(followeeId)

    def getNewsFeedSelf(self):
        return self.tweet

    def getfolloweeSelf(self):
        return self.followee


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._users = defaultdict(User)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self._users[userId].postTweet(tweetId)

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int :rtype: List[int]
        """
        total_tweet = dict()

        total_tweet.update(self._users[userId].getNewsFeedSelf())

        for followee in self._users[userId].getfolloweeSelf():
            total_tweet.update(self._users[followee].getNewsFeedSelf())

        latest_tweets = sorted(total_tweet.items(), key= lambda x:x[0], reverse=True)

        # latest_tweets = Counter(total_tweet).most_common()
        print(latest_tweets)

        result = []
        if len(latest_tweets) >= 10:
            for i in range(10):
                result.append(latest_tweets[i][1])
        else:
            for i in range(len(latest_tweets)):
                result.append(latest_tweets[i][1])

        return result



    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self._users[followerId].follow(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self._users[followerId].unfollow(followeeId)


if __name__ == '__main__':
    # Your Twitter object will be instantiated and called as such:
    # obj = Twitter()
    # obj.postTweet(userId=1, tweetId=5)
    # param_2 = obj.getNewsFeed(userId=1)
    # print(param_2)
    #
    # obj.follow(followerId=1, followeeId=2)
    # obj.postTweet(userId=2, tweetId=6)
    # param_2 = obj.getNewsFeed(userId=1)
    # print(param_2)
    # obj.postTweet(userId=1, tweetId=7)
    # param_2 = obj.getNewsFeed(userId=1)
    # print(param_2)
    #
    # obj.unfollow(followerId=1, followeeId=2)
    # param_2 = obj.getNewsFeed(userId=1)
    # print(param_2)

    obj = Twitter()
    obj.postTweet(userId=1, tweetId=5)
    obj.postTweet(userId=1, tweetId=3)

    param_2 = obj.getNewsFeed(userId=1)
    print(param_2)

