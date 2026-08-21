> 📌 **Cross-listed:** Primary location is [Array/1140-Stone-Game-II](../../Array/1140-Stone-Game-II). This problem also appears under: **Array**, **Math**, **Dynamic Programming**, **Minimax**, **Prefix Sum**, **Game Theory**, **Zero-Sum Game**

# 1140. Stone Game II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Minimax](https://img.shields.io/badge/Minimax-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/stone-game-ii/)


## 📝 Problem Description

Alice and Bob continue their games with piles of stones. There are a number of piles **arranged in a row**, and each pile has a positive integer number of stones `piles[i]`. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take **all the stones** in the **first** `X` remaining piles, where `1 <= X <= 2M`. Then, we set `M = max(M, X)`. Initially, M = 1.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 

Example 1:**

**Input:** piles = [2,7,9,4,4]

**Output:** 10

**Explanation:**

	- If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get `2 + 4 + 4 = 10` stones in total.

	- If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get `2 + 7 = 9` stones in total.

So we return 10 since it's larger.

Example 2:**

**Input:** piles = [1,2,3,4,5,100]

**Output:** 104

 

**Constraints:**

	- `1 <= piles.length <= 100`

	- `1 <= piles[i] <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution uses dynamic programming and memoization to calculate the maximum number of stones Alice can get. The key insight is to consider the game as a zero-sum game, where the maximum number of stones Alice can get is equal to the total number of stones minus the maximum number of stones Bob can get.

**Approach**
1. The solution first calculates the prefix sum of the `piles` array, where each element is the sum of the current element and the next element.
2. The `dfs` function is a recursive function that takes two parameters: `i` (the current index) and `M` (the maximum number of piles Alice can take).
3. If `i + M * 2 >= len(piles)`, it means that there are not enough piles left for Bob to take, so Alice can take all the remaining piles.
4. Otherwise, the function returns the maximum number of stones Alice can get by taking all the stones in the first `j` piles, where `j` ranges from 1 to `M * 2`.
5. The `min` function is used to find the minimum number of stones Bob can get by taking all the stones in the first `j` piles.
6. The `dfs` function is memoized using the `@cache` decorator to avoid redundant calculations.

**Time Complexity**
O(n^3), where n is the length of the `piles` array. The reason is that the `dfs` function has a time complexity of O(n^2) due to the nested loops, and it is called recursively n times.

**Space Complexity**
O(n), where n is the length of the `piles` array. The reason is that the `dfs` function uses a memoization cache to store the results of subproblems, which requires O(n) space.

**Key Insight**
The key insight is to consider the game as a zero-sum game, where the maximum number of stones Alice can get is equal to the total number of stones minus the maximum number of stones Bob can get. This allows us to use dynamic programming and memoization to calculate the maximum number of stones Alice can get.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 317 ms (Beats 20.49%) |
| 💾 Memory | 34.5 MB (Beats 5.19%) |
| 📅 Solved | 2026-08-21 |
| 💻 Language | Python |