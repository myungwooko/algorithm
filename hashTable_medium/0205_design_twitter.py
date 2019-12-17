"""
355. Design Twitter
Medium

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
"""
class Twitter:
    """
    process:
    1. we have to make our data structure.
    2. we have to consder tweet, user, relationship
    3. user can tweet oneself
    4. user can make relationship for following and unfollowing
    5. getnewsfeed retrieve max 10 feeds user tweet including relations feeds => orderby newest one

    **
    in unfollow function, if follower is followee, you don't need to anything.

    if followerId is followeeId:
        return
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = []
        self.userFollowees = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets.insert(0, (userId, tweetId))
        if not self.userFollowees.get(userId, None):
            self.userFollowees[userId] = [userId]

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if self.userFollowees.get(userId, None):
            followees = self.userFollowees[userId]
        else:
            return
        res = []
        for i in self.tweets:
            if i[0] in followees:
                res.append(i[1])
            if len(res) == 10:
                return res
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if not self.userFollowees.get(followerId, None):
            self.userFollowees[followerId] = [followerId, followeeId]
        else:
            if followeeId not in self.userFollowees[followerId]:
                self.userFollowees[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId is followeeId:
            return
        if self.userFollowees.get(followerId, None):
            self.userFollowees[followerId] = list(set(self.userFollowees[followerId]))
            if followeeId in self.userFollowees[followerId]:
                self.userFollowees[followerId].remove(followeeId)
        return

