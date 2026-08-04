> 📌 **Cross-listed:** Primary location is [Array/0877-Stone-Game](../../Array/0877-Stone-Game). This problem also appears under: **Array**, **Math**, **Dynamic Programming**, **Minimax**, **Game Theory**, **Zero-Sum Game**

# 877. Stone Game


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Minimax](https://img.shields.io/badge/Minimax-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/stone-game/)


## 📝 Problem Description

Alice and Bob play a game with piles of stones. There are an **even** number of piles arranged in a row, and each pile has a **positive** integer number of stones `piles[i]`.

The objective of the game is to end with the most stones. The **total** number of stones across all the piles is **odd**, so there are no ties.

Alice and Bob take turns, with **Alice starting first**. Each turn, a player takes the entire pile of stones either from the **beginning** or from the **end** of the row. This continues until there are no more piles left, at which point the person with the **most stones wins**.

Assuming Alice and Bob play optimally, return `true`* if Alice wins the game, or *`false`* if Bob wins*.

 

Example 1:**

```

**Input:** piles = [5,3,4,5]
**Output:** true
**Explanation:** 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.

```

Example 2:**

```

**Input:** piles = [3,7,2,3]
**Output:** true

```

 

**Constraints:**

	- `2 <= piles.length <= 500`

	- `piles.length` is **even**.

	- `1 <= piles[i] <= 500`

	- `sum(piles[i])` is **odd**.

## 🧠 Solution Explanation

**Intuition**
The solution uses dynamic programming and memoization to calculate the maximum difference in stones that Alice can get from the piles, assuming both players play optimally. The key insight is that the maximum difference is the maximum of the difference between the current pile and the maximum difference from the remaining piles on the left, and the difference between the current pile and the maximum difference from the remaining piles on the right.

**Approach**
1. Check if the number of piles is even. If it is, Alice can always win by choosing the middle pile.
2. Define a dynamic programming function `maxDiff(i, j)` that calculates the maximum difference in stones that Alice can get from the piles from index `i` to `j`.
3. If `i == j`, return the value of the current pile.
4. Otherwise, return the maximum of two options:
   - `A[i] - maxDiff(i + 1, j)`: Alice chooses the current pile and takes the maximum difference from the remaining piles on the left.
   - `A[j] - maxDiff(i, j - 1)`: Alice chooses the current pile and takes the maximum difference from the remaining piles on the right.
5. Use memoization to store the results of subproblems to avoid redundant calculations.
6. Return `maxDiff(0, n - 1) >= 0`, which indicates whether Alice can get a positive difference in stones.

**Time Complexity**
O(n^2) where n is the number of piles. This is because the `maxDiff` function is called recursively for each pair of indices from 0 to n-1.

**Space Complexity**
O(n^2) due to the memoization table that stores the results of subproblems.

**Key Insight**
The key insight is that the maximum difference is the maximum of the difference between the current pile and the maximum difference from the remaining piles on the left, and the difference between the current pile and the maximum difference from the remaining piles on the right. This allows us to break down the problem into smaller subproblems and solve them recursively.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 75.42%) |
| 📅 Solved | 2026-08-04 |
| 💻 Language | Python |