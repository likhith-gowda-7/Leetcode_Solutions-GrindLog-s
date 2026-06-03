> 📌 **Cross-listed:** Primary location is [Array/0322-Coin-Change](../../Array/0322-Coin-Change). This problem also appears under: **Array**, **Dynamic Programming**, **Breadth-First Search**

# 322. Coin Change


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/coin-change/)


## 📝 Problem Description

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the fewest number of coins that you need to make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:**

```

**Input:** coins = [1,2,5], amount = 11
**Output:** 3
**Explanation:** 11 = 5 + 5 + 1

```

Example 2:**

```

**Input:** coins = [2], amount = 3
**Output:** -1

```

Example 3:**

```

**Input:** coins = [1], amount = 0
**Output:** 0

```

 

**Constraints:**

	- `1 <= coins.length <= 12`

	- `1 <= coins[i] <= 2^31 - 1`

	- `0 <= amount <= 10^4`

## 🧠 Solution Explanation

### Intuition
This solution works by using dynamic programming to build up a table of the minimum number of coins needed to make up each amount from 0 to the target amount. The key idea is to iterate over each amount and each coin, and update the minimum number of coins needed for the current amount if using the current coin results in a smaller number of coins. 
The dynamic programming approach allows us to avoid redundant calculations and ensure that we consider all possible combinations of coins.

### Approach
1. Initialize a dynamic programming table `dp` with `amount + 1` elements, all set to infinity, except for `dp[0]` which is set to 0 (since we need 0 coins to make up an amount of 0).
2. Iterate over each amount from 1 to the target amount.
3. For each amount, iterate over each coin and check if the coin is less than or equal to the current amount.
4. If the coin is less than or equal to the current amount, update the minimum number of coins needed for the current amount by taking the minimum of the current value and the number of coins needed for the amount minus the coin value.
5. However, there seems to be an issue with the provided code as it adds 1 to `dp[amt]` after the inner loop, which is incorrect. The correct approach should be to update `dp[amt]` with the minimum value found in the inner loop, without adding 1.

### Time Complexity
The time complexity is O(amount * len(coins)), where amount is the target amount and len(coins) is the number of different coin denominations. This is because we have two nested loops, one iterating over each amount and the other iterating over each coin.

### Space Complexity
The space complexity is O(amount), as we need to store the minimum number of coins needed for each amount from 0 to the target amount in the dynamic programming table.

### Key Insight
The key insight here is that we can use dynamic programming to break down the problem into smaller sub-problems and solve each sub-problem only once, avoiding redundant calculations and ensuring that we consider all possible combinations of coins. However, the provided code has a logical error and should be corrected to properly update the `dp` table.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 719 ms (Beats 31.79%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-12-03 |
| 💻 Language | Python |