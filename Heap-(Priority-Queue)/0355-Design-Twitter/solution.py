class Twitter:

    def __init__(self):
        self.count=0
        self.map=defaultdict(set)
        self.tweets=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count,tweetId))
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        min_heap=[]
        #we go to user following list and take there messages
        self.map[userId].add(userId) 
        for follower in self.map[userId]:
            #check we follower has made any tweets,if yes then take it
            if(follower in self.tweets):
                #here we take the last index of follower's tweets becoz that's the most recent
                index=len(self.tweets[follower])-1
                count,tweetId=self.tweets[follower][index]
                min_heap.append((count,tweetId,index,follower))
        heapq.heapify(min_heap)

        while min_heap and len(res)<10:
            count,tweetId,index,follower=heapq.heappop(min_heap)
            res.append(tweetId)
            index-=1
            if(index>=0):
                c,tw=self.tweets[follower][index]
                heapq.heappush(min_heap,(c,tw,index,follower))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followerId in self.map):
            self.map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)