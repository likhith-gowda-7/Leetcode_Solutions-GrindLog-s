> 📌 **Cross-listed:** Primary location is [Math/1510-Stone-Game-IV](../../Math/1510-Stone-Game-IV). This problem also appears under: **Math**, **Dynamic Programming**, **Minimax**, **Game Theory**, **Nim Game**, **Sprague–Grundy Theorem**, **Zero-Sum Game**

# 1510. Stone Game IV


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Minimax](https://img.shields.io/badge/Minimax-purple) ![Game Theory](https://img.shields.io/badge/Game%20Theory-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/stone-game-iv/)


## 📝 Problem Description

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are `n` stones in a pile. On each player's turn, that player makes a *move* consisting of removing **any** non-zero **square number** of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer `n`, return `true` if and only if Alice wins the game otherwise return `false`, assuming both players play optimally.

 

Example 1:**

```

**Input:** n = 1
**Output:** true
**Explanation: **Alice can remove 1 stone winning the game because Bob doesn't have any moves.
```

Example 2:**

```

**Input:** n = 2
**Output:** false
**Explanation: **Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).

```

Example 3:**

```

**Input:** n = 4
**Output:** true
**Explanation:** n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).

```

 

**Constraints:**

	- `1 <= n <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The problem is a variation of the Nim game, where players take turns removing square numbers of stones. The key insight is to recognize that the game can be reduced to a simpler problem by considering the binary representation of the number of stones. If the binary representation has an odd number of 1s, Alice wins; otherwise, Bob wins.

**Approach**
1. Define a recursive function `dfs(i)` that takes the current number of stones `i` as input.
2. If `i` is 0, return False, as the game is over and Bob wins.
3. Iterate over all possible square numbers `j` from 1 to the square root of `i` (inclusive).
4. For each `j`, recursively call `dfs(i - j ** 2)` to simulate Alice's move.
5. If any of the recursive calls return True, it means Alice has a winning move, so return True.
6. If none of the recursive calls return True, it means Bob has a winning move, so return False.
7. Return the result of the recursive function.

**Time Complexity**
O(n * sqrt(n)), where n is the number of stones. The reason is that in the worst case, we need to iterate over all possible square numbers up to the square root of n, and for each square number, we recursively call the function n times.

**Space Complexity**
O(n), as we need to store the recursive call stack, which can go up to n levels deep in the worst case.

**Key Insight**
The key insight is to recognize that the game can be reduced to a simpler problem by considering the binary representation of the number of stones. This allows us to use a recursive function to simulate the game and determine the winner.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1149 ms (Beats 34.85%) |
| 💾 Memory | 161.7 MB (Beats 9.4%) |
| 📅 Solved | 2026-08-10 |
| 💻 Language | Python |