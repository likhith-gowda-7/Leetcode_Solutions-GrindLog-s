> 📌 **Cross-listed:** Primary location is [Array/0188-Best-Time-to-Buy-and-Sell-Stock-IV](../../Array/0188-Best-Time-to-Buy-and-Sell-Stock-IV). This problem also appears under: **Array**, **Dynamic Programming**

# 188. Best Time to Buy and Sell Stock IV


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)


## 📝 Problem Description

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i^th` day, and an integer `k`.

Find the maximum profit you can achieve. You may complete at most `k` transactions: i.e. you may buy at most `k` times and sell at most `k` times.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:**

```

**Input:** k = 2, prices = [2,4,1]
**Output:** 2
**Explanation:** Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

```

Example 2:**

```

**Input:** k = 2, prices = [3,2,6,5,0,3]
**Output:** 7
**Explanation:** Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

```

 

**Constraints:**

	- `1 <= k <= 100`

	- `1 <= prices.length <= 1000`

	- `0 <= prices[i] <= 1000`

## 🧠 Solution Explanation

## Intuition
This solution works by using dynamic programming to track the maximum profit that can be achieved at each step, considering whether we are currently holding a stock or not, and how many transactions we have made so far. The key idea is to iterate over the prices in reverse order, updating our dynamic programming table with the maximum profit we can get at each step.

## Approach
1. Initialize a dynamic programming table `dp` with two rows (representing whether we are holding a stock or not) and `k+1` columns (representing the number of transactions made so far).
2. Iterate over the prices in reverse order, and for each price, iterate over the two possible states (holding or not holding a stock) and the possible number of transactions made so far.
3. For each state and transaction count, calculate the maximum profit we can get by either buying or selling the stock (if we are not holding it), or by selling or holding the stock (if we are holding it).
4. Update the dynamic programming table with the maximum profit we can get at each step.

## Time Complexity
The time complexity of this solution is O(n*k), where n is the number of days and k is the maximum number of transactions. This is because we are iterating over the prices in reverse order, and for each price, we are iterating over the two possible states and the possible number of transactions made so far.

## Space Complexity
The space complexity of this solution is O(k), as we are using a dynamic programming table with two rows and k+1 columns. However, the given solution has a bug and the space complexity should be O(1) for the variables and O(k) for the dp array, but the array is not correctly implemented.

## Key Insight
The key insight behind this solution is to use dynamic programming to track the maximum profit we can get at each step, considering the two possible states (holding or not holding a stock) and the possible number of transactions made so far. However, the given solution has a bug and does not correctly implement the dynamic programming approach. A correct implementation would use a 2D array with n rows and k+1 columns, where n is the number of days.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 43 ms (Beats 47.9%) |
| 💾 Memory | 19.2 MB (Beats 88.3%) |
| 📅 Solved | 2026-04-29 |
| 💻 Language | Python |