# 121. Best Time to Buy and Sell Stock


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)


## 📝 Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

 

Example 1:**

```

**Input:** prices = [7,1,5,3,6,4]
**Output:** 5
**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

```

Example 2:**

```

**Input:** prices = [7,6,4,3,1]
**Output:** 0
**Explanation:** In this case, no transactions are done and the max profit = 0.

```

 

**Constraints:**

	- `1 <= prices.length <= 10^5`

	- `0 <= prices[i] <= 10^4`

## 🧠 Solution Explanation

## Intuition
This approach works by iterating through the list of stock prices and keeping track of the minimum price encountered so far, which represents the best time to buy the stock. It then calculates the potential profit by subtracting the minimum price from the current price, updating the maximum profit if necessary. The key idea is to find the optimal buy and sell points by considering all possible pairs of prices.

## Approach
1. Initialize the minimum buy price (`buy`) to the first price in the list and the maximum profit (`max_profit`) to 0.
2. Iterate through the list of prices starting from the second day.
3. For each price, check if it's lower than the current minimum buy price. If so, update the minimum buy price.
4. Calculate the potential profit by subtracting the minimum buy price from the current price.
5. If the potential profit is greater than the current maximum profit, update the maximum profit.

## Time Complexity
The time complexity is O(n), where n is the number of days (i.e., the length of the `prices` list), because we're making a single pass through the list.

## Space Complexity
The space complexity is O(1), because we're using a constant amount of space to store the minimum buy price and the maximum profit, regardless of the input size.

## Key Insight
The key insight here is that we don't need to consider all possible pairs of buy and sell days. By keeping track of the minimum price encountered so far, we can efficiently find the optimal buy and sell points, reducing the problem to a single pass through the list of prices.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 35 ms (Beats 81.69%) |
| 💾 Memory | 29 MB (Beats 8.26%) |
| 📅 Solved | 2026-03-06 |
| 💻 Language | Python |