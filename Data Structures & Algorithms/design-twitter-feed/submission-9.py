import heapq

class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.getUser(userId)
        user["posts"].append((self.time, tweetId))
        self.updateFeed(user["feed"], tweetId)
        for follower in user["followers"]:
            self.updateFeed(self.getUser(follower)["feed"], tweetId)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        sort = list(self.getUser(userId)["feed"])
        sort.sort(key=lambda p: -p[0])
        if userId == 2: print(self.users)
        return [p[1] for p in sort]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        
        user = self.getUser(followerId)
        followee = self.getUser(followeeId)
        if followeeId in user["following"]: return
        user["following"].add(followeeId)
        followee["followers"].add(followerId)
        
        feed = user["feed"]
        for post in followee["posts"]:
            heapq.heappush(feed, post)
            if len(feed) > 10:
                heapq.heappop(feed)



    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        
        user = self.getUser(followerId)
        followee = self.getUser(followeeId)
        user["following"].discard(followeeId)
        followee["followers"].discard(followerId)

        user["feed"] = list(user["posts"])
        heapq.heapify(user["feed"])
        feed = user["feed"]
        for following in user["following"]:
            for post in following["posts"]:
                heapq.heappush(feed, post)
                if len(feed) > 10:
                    heapq.heappop(feed)


    def updateFeed(self, feed, postId) -> None:
        heapq.heappush(feed, (self.time, postId))
        if len(feed) > 10:
            heapq.heappop(feed)

    def getUser(self, userId) -> dict:
        if userId not in self.users:
            feed = []
            heapq.heapify(feed)
            self.users[userId] = {
                "followers": set(),
                "following": set(),
                "feed": feed,
                "posts": []
            }
        return self.users[userId]
        
