# 3021. Alice and Bob Playing Flower Game


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/alice-and-bob-playing-flower-game/)


## 📝 Problem Description

Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them. There are `x` flowers in the first lane between Alice and Bob, and `y` flowers in the second lane between them.

![](https://assets.leetcode.com/uploads/2025/08/27/3021.png)

The game proceeds as follows:

	- Alice takes the first turn.

	- In each turn, a player must choose either one of the lane and pick one flower from that side.

	- At the end of the turn, if there are no flowers left at all in either lane, the **current** player captures their opponent and wins the game.

Given two integers, `n` and `m`, the task is to compute the number of possible pairs `(x, y)` that satisfy the conditions:

	- Alice must win the game according to the described rules.

	- The number of flowers `x` in the first lane must be in the range `[1,n]`.

	- The number of flowers `y` in the second lane must be in the range `[1,m]`.

Return *the number of possible pairs* `(x, y)` *that satisfy the conditions mentioned in the statement*.

 

Example 1:**

```

**Input:** n = 3, m = 2
**Output:** 3
**Explanation:** The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).

```

Example 2:**

```

**Input:** n = 1, m = 1
**Output:** 0
**Explanation:** No pairs satisfy the conditions described in the statement.

```

 

**Constraints:**

	- `1 <= n, m <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The problem is essentially asking us to find the number of pairs of flowers that Alice can pick to win the game. The key insight is that Alice can win the game if and only if the total number of flowers is even. This is because in each turn, a player must choose either one of the lanes and pick one flower from that side. If the total number of flowers is even, then Alice can always pick a flower from one lane and leave the other lane with an even number of flowers, forcing Bob to pick a flower from the same lane and leaving Alice with an odd number of flowers, which she can then pick to win the game.

**Approach**
1. The solution simply returns the product of `n` and `m` divided by 2.
2. This is because the number of pairs of flowers that Alice can pick to win the game is equal to the total number of flowers divided by 2.

**Time Complexity**
O(1) - The solution has constant time complexity because it only involves a single arithmetic operation, regardless of the input values.

**Space Complexity**
O(1) - The solution has constant space complexity because it only uses a constant amount of space to store the result, regardless of the input values.

**Key Insight**
The key insight is that Alice can win the game if and only if the total number of flowers is even, which is why the solution simply returns the product of `n` and `m` divided by 2.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-08-29 |
| 💻 Language | Python |