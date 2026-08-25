> 📌 **Cross-listed:** Primary location is [Array/1872-Stone-Game-VIII](../../Array/1872-Stone-Game-VIII). This problem also appears under: **Array**, **Math**, **Dynamic Programming**, **Minimax**, **Prefix Sum**, **Game Theory**, **Zero-Sum Game**

# 1872. Stone Game VIII


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Minimax](https://img.shields.io/badge/Minimax-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/stone-game-viii/)


## 📝 Problem Description

Alice and Bob take turns playing a game, with **Alice starting first**.

There are `n` stones arranged in a row. On each player's turn, while the number of stones is **more than one**, they will do the following:

	- Choose an integer `x > 1`, and **remove** the leftmost `x` stones from the row.

	- Add the **sum** of the **removed** stones' values to the player's score.

	- Place a **new stone**, whose value is equal to that sum, on the left side of the row.

The game stops when **only** **one** stone is left in the row.

The **score difference** between Alice and Bob is `(Alice's score - Bob's score)`. Alice's goal is to **maximize** the score difference, and Bob's goal is the **minimize** the score difference.

Given an integer array `stones` of length `n` where `stones[i]` represents the value of the `i^th` stone **from the left**, return *the **score difference** between Alice and Bob if they both play **optimally**.*

 

Example 1:**

```

**Input:** stones = [-1,2,-3,4,-5]
**Output:** 5
**Explanation:**
- Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
  value 2 on the left. stones = [2,-5].
- Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
  the left. stones = [-3].
The difference between their scores is 2 - (-3) = 5.

```

Example 2:**

```

**Input:** stones = [7,-6,5,10,5,-2,-6]
**Output:** 13
**Explanation:**
- Alice removes all stones, adds 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 to her score, and places a
  stone of value 13 on the left. stones = [13].
The difference between their scores is 13 - 0 = 13.

```

Example 3:**

```

**Input:** stones = [-10,-12]
**Output:** -22
**Explanation:**
- Alice can only make one move, which is to remove both stones. She adds (-10) + (-12) = -22 to her
  score and places a stone of value -22 on the left. stones = [-22].
The difference between their scores is (-22) - 0 = -22.

```

 

**Constraints:**

	- `n == stones.length`

	- `2 <= n <= 10^5`

	- `-10^4 <= stones[i] <= 10^4`

## 🧠 Solution Explanation

**Intuition**  
When a player removes the leftmost `x` stones, the new stone’s value equals the sum of those stones.  
Thus, after any move the leftmost stone’s value is the *prefix sum* of the original array up to the current position.  
The game can be viewed as repeatedly choosing a split point in the prefix sums; the score difference depends only on the chosen split, not on the exact stones removed.

**Approach**  
1. Compute prefix sums `s[i] = sum(A[0..i])`.  
2. Define `maxDiff(i)` as the maximum score difference the current player can force when the leftmost stone corresponds to prefix `s[i]`.  
3. Base case: if `i == n-1` (only one stone left), the current player takes the whole sum, so `maxDiff(i) = s[n-1]`.  
4. Recurrence: the player can either keep the current stone (`maxDiff(i+1)`) or take the current stone and give the opponent the rest, yielding `s[i] - maxDiff(i+1)`.  
   Hence `maxDiff(i) = max(maxDiff(i+1), s[i] - maxDiff(i+1))`.  
5. Memoize `maxDiff` with `@cache` and compute `maxDiff(1)` (since Alice starts after the first stone is already on the board).  
6. Return the result.

**Time Complexity**  
Each `maxDiff(i)` is computed once, and each computation is O(1).  
Total time: **O(n)**.

**Space Complexity**  
Prefix sum array: O(n).  
Memoization cache holds at most `n` entries: O(n).  
Total space: **O(n)**.

**Key Insight**  
The game’s state can be represented solely by the current prefix sum index; the optimal play reduces to a simple recurrence on prefix sums, turning a seemingly complex game into a linear DP.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 944 ms (Beats 5.88%) |
| 💾 Memory | 249.9 MB (Beats 5.29%) |
| 📅 Solved | 2026-08-24 |
| 💻 Language | Python |