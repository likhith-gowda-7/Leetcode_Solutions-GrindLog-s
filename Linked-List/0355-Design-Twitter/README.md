> 📌 **Cross-listed:** Primary location is [Hash Table/0355-Design-Twitter](../../Hash-Table/0355-Design-Twitter). This problem also appears under: **Hash Table**, **Linked List**, **Design**, **Heap (Priority Queue)**

# 355. Design Twitter


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Design](https://img.shields.io/badge/Design-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/design-twitter/)


## 📝 Problem Description

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the `10` most recent tweets in the user's news feed.

Implement the `Twitter` class:

	- `Twitter()` Initializes your twitter object.

	- `void postTweet(int userId, int tweetId)` Composes a new tweet with ID `tweetId` by the user `userId`. Each call to this function will be made with a unique `tweetId`.

	- `List<Integer> getNewsFeed(int userId)` Retrieves the `10` most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be **ordered from most recent to least recent**.

	- `void follow(int followerId, int followeeId)` The user with ID `followerId` started following the user with ID `followeeId`.

	- `void unfollow(int followerId, int followeeId)` The user with ID `followerId` started unfollowing the user with ID `followeeId`.

 

Example 1:**

```

**Input**
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
**Output**
[null, null, [5], null, null, [6, 5], null, [5]]

**Explanation**
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

```

 

**Constraints:**

	- `1 <= userId, followerId, followeeId <= 500`

	- `0 <= tweetId <= 10^4`

	- All the tweets have **unique** IDs.

	- At most `3 * 10^4` calls will be made to `postTweet`, `getNewsFeed`, `follow`, and `unfollow`.

	- A user cannot follow himself.

## 🧠 Solution Explanation

**Intuition**
The solution uses a combination of hash tables and a min heap to efficiently manage user tweets and news feeds. The key insight is to store tweets in a hash table and use a min heap to keep track of the most recent tweets for each user.

**Approach**
1. Initialize a hash table `self.map` to store user followings, a hash table `self.tweets` to store user tweets, and a counter `self.count` to keep track of the most recent tweet ID.
2. In `postTweet`, append the new tweet to the user's tweet list and decrement the counter.
3. In `getNewsFeed`, add the user's ID to their following list and iterate through their followings to collect their tweets.
4. For each following user, add their most recent tweet to a min heap, along with their ID and tweet index.
5. Pop tweets from the min heap and add them to the news feed until it reaches the 10-tweet limit.
6. In `follow`, add the followee ID to the follower's following list.
7. In `unfollow`, remove the followee ID from the follower's following list.

**Time Complexity**
- `postTweet`: O(1) since it's a simple append operation.
- `getNewsFeed`: O(n log n) where n is the number of followings, since we're iterating through followings and pushing/popping from the min heap.
- `follow` and `unfollow`: O(1) since it's a simple set operation.

**Space Complexity**
- O(n) for the hash tables to store user followings and tweets, where n is the number of users.
- O(n log n) for the min heap to store the most recent tweets for each user.

**Key Insight**
The key insight is to use a min heap to efficiently keep track of the most recent tweets for each user, allowing us to retrieve the 10 most recent tweets in the user's news feed in O(n log n) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 12 ms (Beats 67.51%) |
| 💾 Memory | 27.6 MB (Beats 92.47%) |
| 📅 Solved | 2025-07-13 |
| 💻 Language | Python |