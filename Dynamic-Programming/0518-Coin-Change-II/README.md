> 📌 **Cross-listed:** Primary location is [Array/0518-Coin-Change-II](../../Array/0518-Coin-Change-II). This problem also appears under: **Array**, **Dynamic Programming**

# 518. Coin Change II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/coin-change-ii/)


## 📝 Problem Description

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the number of combinations that make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `0`.

You may assume that you have an infinite number of each kind of coin.

The answer is **guaranteed** to fit into a signed **32-bit** integer.

 

Example 1:**

```

**Input:** amount = 5, coins = [1,2,5]
**Output:** 4
**Explanation:** there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

```

Example 2:**

```

**Input:** amount = 3, coins = [2]
**Output:** 0
**Explanation:** the amount of 3 cannot be made up just with coins of 2.

```

Example 3:**

```

**Input:** amount = 10, coins = [10]
**Output:** 1

```

 

**Constraints:**

	- `1 <= coins.length <= 300`

	- `1 <= coins[i] <= 5000`

	- All the values of `coins` are **unique**.

	- `0 <= amount <= 5000`

## 🧠 Solution Explanation

**Intuition**
The problem can be solved using dynamic programming, where we build up a table of solutions to subproblems. The key insight is that the number of combinations that make up a certain amount is the sum of the number of combinations that make up the amount minus each coin denomination.

**Approach**
1. Initialize a dynamic programming table `dp` of size `amount + 1` with all elements set to 0, except for `dp[0]` which is set to 1 (since there is exactly one way to make up an amount of 0, which is to not use any coins).
2. Iterate over each coin denomination `coin` in the `coins` array.
3. For each coin denomination, iterate over the range from `coin` to `amount` (inclusive).
4. For each amount `i` in this range, update `dp[i]` by adding the number of combinations that make up `i - coin`, which is stored in `dp[i - coin]`. This represents the number of combinations that make up `i` by using the current coin denomination.
5. After iterating over all coin denominations and amounts, return `dp[amount]`, which represents the total number of combinations that make up the given amount.

**Time Complexity**
O(n*amount), where n is the number of coin denominations. This is because we have two nested loops: one that iterates over the coin denominations (O(n)) and another that iterates over the amounts (O(amount)).

**Space Complexity**
O(amount), which is the size of the dynamic programming table. This is because we need to store the number of combinations that make up each amount up to the given amount.

**Key Insight**
The key insight is that the number of combinations that make up a certain amount is the sum of the number of combinations that make up the amount minus each coin denomination. This is because we can always add a coin of the current denomination to each combination that makes up the amount minus the coin denomination, resulting in a new combination that makes up the current amount.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 187 ms (Beats 98.8%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-12-09 |
| 💻 Language | Python |