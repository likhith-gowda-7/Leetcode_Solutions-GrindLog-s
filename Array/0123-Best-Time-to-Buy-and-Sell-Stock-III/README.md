# 123. Best Time to Buy and Sell Stock III


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)


## 📝 Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

Find the maximum profit you can achieve. You may complete **at most two transactions**.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:**

```

**Input:** prices = [3,3,5,0,0,3,1,4]
**Output:** 6
**Explanation:** Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```

Example 2:**

```

**Input:** prices = [1,2,3,4,5]
**Output:** 4
**Explanation:** Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

```

Example 3:**

```

**Input:** prices = [7,6,4,3,1]
**Output:** 0
**Explanation:** In this case, no transaction is done, i.e. max profit = 0.

```

 

**Constraints:**

	- `1 <= prices.length <= 10^5`

	- `0 <= prices[i] <= 10^5`

## 🧠 Solution Explanation

## Intuition
This solution works by maintaining four variables to track the maximum profit after the first buy, first sell, second buy, and second sell. The key idea is to update these variables iteratively based on the current price, ensuring that we consider all possible transactions. By doing so, we can find the maximum profit achievable with at most two transactions.

## Approach
1. Initialize `buy1` and `buy2` to negative infinity, representing the maximum profit after the first and second buy, respectively.
2. Initialize `sell1` and `sell2` to 0, representing the maximum profit after the first and second sell, respectively.
3. Iterate through the `prices` array, updating `buy1`, `sell1`, `buy2`, and `sell2` at each step based on the current price.
4. For `buy1`, choose the maximum between the current `buy1` and `-price`, representing the decision to buy or not.
5. For `sell1`, choose the maximum between the current `sell1` and `buy1 + price`, representing the decision to sell or not after the first buy.
6. For `buy2`, choose the maximum between the current `buy2` and `sell1 - price`, representing the decision to buy or not after the first sell.
7. For `sell2`, choose the maximum between the current `sell2` and `buy2 + price`, representing the decision to sell or not after the second buy.

## Time Complexity
The time complexity is O(n), where n is the number of days (i.e., the length of the `prices` array), since we make a single pass through the array.

## Space Complexity
The space complexity is O(1), as we use a constant amount of space to store the `buy1`, `sell1`, `buy2`, and `sell2` variables, regardless of the input size.

## Key Insight
The key insight is to recognize that we can update the `buy` and `sell` variables iteratively, considering the current price and the previous maximum profits, to find the optimal solution. This approach allows us to avoid explicit recursion and memoization, resulting in an efficient and scalable solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 97 ms (Beats 73.82%) |
| 💾 Memory | 30.8 MB (Beats 72.8%) |
| 📅 Solved | 2026-04-19 |
| 💻 Language | Python |