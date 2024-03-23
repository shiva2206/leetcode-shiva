class Twitter:
    def __init__(self):

        self.userfol = defaultdict(set)
        self.usertweets = defaultdict(list)
        self.i=0;

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.usertweets[userId].append((self.i,tweetId))
        self.i-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(self.userfol) 
        # print(self.usertweets)
        pq = []
        self.userfol[userId].add(userId)
        for user in self.userfol[userId]:
           if self.usertweets[user]:
                time,tweet = self.usertweets[user][-1]
                ind = len(self.usertweets[user])-1
                pq.append((time,tweet,user,ind))
        res = []
        heapq.heapify(pq)
        # print(pq)
        while pq and len(res)<10:
            time,tweet,user,ind = heapq.heappop(pq)
            res.append(tweet)
            if ind!=0:
                time,tweet = self.usertweets[user][ind-1]
                heapq.heappush(pq,(time,tweet,user,ind-1)) 
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.userfol[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId  not in self.userfol[followerId]: return 
        self.userfol[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)