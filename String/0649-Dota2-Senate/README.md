# 649. Dota2 Senate


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Queue](https://img.shields.io/badge/Queue-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/dota2-senate/)


## 📝 Problem Description

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise **one** of the two rights:

	- **Ban one senator's right:** A senator can make another senator lose all his rights in this and all the following rounds.

	- **Announce the victory:** If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.

Given a string `senate` representing each senator's party belonging. The character `'R'` and `'D'` represent the Radiant party and the Dire party. Then if there are `n` senators, the size of the given string will be `n`.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be `"Radiant"` or `"Dire"`.

 

Example 1:**

```

**Input:** senate = "RD"
**Output:** "Radiant"
**Explanation:** 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

```

Example 2:**

```

**Input:** senate = "RDD"
**Output:** "Dire"
**Explanation:** 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

```

 

**Constraints:**

	- `n == senate.length`

	- `1 <= n <= 10^4`

	- `senate[i]` is either `'R'` or `'D'`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a greedy approach to simulate the voting process. By maintaining two queues for the Radiant and Dire parties, it efficiently determines the outcome of the voting process.

**Approach**
1. Initialize two queues, `r` and `d`, to store the indices of senators from the Radiant and Dire parties, respectively.
2. Iterate through the `senate` string to populate the queues with the indices of senators from each party.
3. While both queues are not empty, compare the indices of the first senators in each queue.
4. If the Radiant senator's index is smaller, add the Radiant senator's index to the end of the Radiant queue and remove the Dire senator from the Dire queue.
5. Otherwise, add the Dire senator's index to the end of the Dire queue and remove the Radiant senator from the Radiant queue.
6. Repeat steps 3-5 until one of the queues is empty.
7. If the Radiant queue is not empty, return "Radiant" as the winning party; otherwise, return "Dire".

**Time Complexity**
O(n), where n is the length of the `senate` string. This is because each senator is processed at most twice (once when added to the queue and once when removed).

**Space Complexity**
O(n), where n is the length of the `senate` string. This is because in the worst case, all senators are added to their respective queues.

**Key Insight**
The key insight is that the outcome of the voting process depends only on the relative order of the senators' indices. By maintaining the queues in this way, we can efficiently determine the winning party without having to simulate the entire voting process.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 82.34%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-03-29 |
| 💻 Language | Python |