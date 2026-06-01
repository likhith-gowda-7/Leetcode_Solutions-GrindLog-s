> 📌 **Cross-listed:** Primary location is [Array/0309-Best-Time-to-Buy-and-Sell-Stock-with-Cooldown](../../Array/0309-Best-Time-to-Buy-and-Sell-Stock-with-Cooldown). This problem also appears under: **Array**, **Dynamic Programming**

# 309. Best Time to Buy and Sell Stock with Cooldown


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)


## 📝 Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

	- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:**

```

**Input:** prices = [1,2,3,0,2]
**Output:** 3
**Explanation:** transactions = [buy, sell, cooldown, buy, sell]

```

Example 2:**

```

**Input:** prices = [1]
**Output:** 0

```

 

**Constraints:**

	- `1 <= prices.length <= 5000`

	- `0 <= prices[i] <= 1000`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.6 MB (Beats 60.89%) |
| 📅 Solved | 2026-04-20 |
| 💻 Language | Python |