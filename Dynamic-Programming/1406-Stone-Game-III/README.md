> 📌 **Cross-listed:** Primary location is [Array/1406-Stone-Game-III](../../Array/1406-Stone-Game-III). This problem also appears under: **Array**, **Math**, **Dynamic Programming**, **Minimax**, **Game Theory**, **Zero-Sum Game**

# 1406. Stone Game III


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Minimax](https://img.shields.io/badge/Minimax-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/stone-game-iii/)


## 📝 Problem Description

Alice and Bob continue their games with piles of stones. There are several stones **arranged in a row**, and each stone has an associated value which is an integer given in the array `stoneValue`.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take `1`, `2`, or `3` stones from the **first** remaining stones in the row.

The score of each player is the sum of the values of the stones taken. The score of each player is `0` initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob **play optimally**.

Return `"Alice"`* if Alice will win, *`"Bob"`* if Bob will win, or *`"Tie"`* if they will end the game with the same score*.

 

Example 1:**

```

**Input:** stoneValue = [1,2,3,7]
**Output:** "Bob"
**Explanation:** Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.

```

Example 2:**

```

**Input:** stoneValue = [1,2,3,-9]
**Output:** "Alice"
**Explanation:** Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.

```

Example 3:**

```

**Input:** stoneValue = [1,2,3,6]
**Output:** "Tie"
**Explanation:** Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.

```

 

**Constraints:**

	- `1 <= stoneValue.length <= 5 * 10^4`

	- `-1000 <= stoneValue[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution uses dynamic programming and minimax algorithm to determine the outcome of the game. The key idea is to calculate the maximum difference in scores that Alice can achieve by taking 1, 2, or 3 stones from the current position. If Alice can achieve a positive difference, she will win; if Bob can achieve a positive difference, he will win; otherwise, it's a tie.

**Approach**
1. Initialize a memoization table `maxDiff` to store the maximum difference in scores for each position.
2. Define a recursive function `maxDiff(i)` that calculates the maximum difference in scores for the current position `i`.
3. For each position `i`, consider three possible moves: taking 1, 2, or 3 stones.
4. For each move, calculate the maximum difference in scores by recursively calling `maxDiff` for the next position.
5. Return the maximum difference in scores for the current position.
6. Call `maxDiff(0)` to calculate the maximum difference in scores for the initial position.
7. Determine the outcome of the game based on the maximum difference in scores.

**Time Complexity**
O(n^2), where n is the number of stones. The recursive function `maxDiff` is called for each position, and for each position, it recursively calls itself up to 3 times. The memoization table helps to avoid redundant calculations, but the overall time complexity is still O(n^2).

**Space Complexity**
O(n), where n is the number of stones. The memoization table stores the maximum difference in scores for each position, which requires O(n) space.

**Key Insight**
The key insight is to use the minimax algorithm to determine the outcome of the game. By calculating the maximum difference in scores for each position, we can determine whether Alice or Bob will win, or whether it's a tie. This approach allows us to solve the problem efficiently using dynamic programming.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 890 ms (Beats 52.28%) |
| 💾 Memory | 220.4 MB (Beats 20.29%) |
| 📅 Solved | 2026-08-03 |
| 💻 Language | Python |