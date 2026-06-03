# 2410. Maximum Matching of Players With Trainers


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-matching-of-players-with-trainers/)


## 📝 Problem Description

You are given a **0-indexed** integer array `players`, where `players[i]` represents the **ability** of the `i^th` player. You are also given a **0-indexed** integer array `trainers`, where `trainers[j]` represents the **training capacity **of the `j^th` trainer.

The `i^th` player can **match** with the `j^th` trainer if the player's ability is **less than or equal to** the trainer's training capacity. Additionally, the `i^th` player can be matched with at most one trainer, and the `j^th` trainer can be matched with at most one player.

Return *the **maximum** number of matchings between *`players`* and *`trainers`* that satisfy these conditions.*

 

Example 1:**

```

**Input:** players = [4,7,9], trainers = [8,2,5,8]
**Output:** 2
**Explanation:**
One of the ways we can form two matchings is as follows:
- players[0] can be matched with trainers[0] since 4 <= 8.
- players[1] can be matched with trainers[3] since 7 <= 8.
It can be proven that 2 is the maximum number of matchings that can be formed.

```

Example 2:**

```

**Input:** players = [1,1,1], trainers = [10]
**Output:** 1
**Explanation:**
The trainer can be matched with any of the 3 players.
Each player can only be matched with one trainer, so the maximum answer is 1.

```

 

**Constraints:**

	- `1 <= players.length, trainers.length <= 10^5`

	- `1 <= players[i], trainers[j] <= 10^9`

 

**Note:** This question is the same as [ 445: Assign Cookies.](https://leetcode.com/problems/assign-cookies/description/)

## 🧠 Solution Explanation

**Intuition**
The key insight behind this solution is that we can maximize the number of matchings by pairing the players with the trainers in a sorted order. This is because we want to match the players with the trainers who have the highest training capacity that is still sufficient for the player's ability.

**Approach**
1. Sort both the `players` and `trainers` arrays in ascending order.
2. Initialize a counter `c` to keep track of the number of matchings.
3. Iterate through the `trainers` array. For each trainer's capacity `cap`, check if it is greater than or equal to the current player's ability `players[c]`.
4. If the capacity is sufficient, increment the counter `c` and move to the next player.
5. Continue this process until we have matched all players or we have exhausted the trainers.

**Time Complexity**
O(n log n) due to the sorting step, where n is the number of players (or trainers).

**Space Complexity**
O(1) since we are only using a constant amount of space to store the counter and indices.

**Key Insight**
The key insight is that by sorting the players and trainers, we can efficiently find the maximum number of matchings by pairing the players with the trainers in a greedy manner. This approach takes advantage of the fact that the players and trainers are sorted, allowing us to quickly find the best match for each player.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 61 ms (Beats 99.65%) |
| 💾 Memory | 33.7 MB (Beats 98.58%) |
| 📅 Solved | 2025-07-13 |
| 💻 Language | Python |