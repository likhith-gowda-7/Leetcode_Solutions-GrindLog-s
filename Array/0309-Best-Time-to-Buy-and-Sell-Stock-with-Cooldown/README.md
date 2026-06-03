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

## 🧠 Solution Explanation

### Intuition
The problem can be solved using dynamic programming, where we maintain a state of whether we are holding a stock or not, and consider the maximum profit we can get by either selling, holding, or buying the stock at each step. The cooldown restriction adds an extra layer of complexity, requiring us to keep track of the previous state to ensure we don't buy immediately after selling.

### Approach
1. Initialize a deque `dp` with three states: `[0, 0]`, representing the maximum profit when holding and not holding the stock, respectively.
2. Iterate over the prices in reverse order, updating the `dp` deque at each step.
3. For each state (holding or not holding), calculate the maximum profit by considering the options to sell, hold, or buy the stock.
4. Update the `dp` deque with the maximum profit for each state.

### Time Complexity
The time complexity is O(n), where n is the number of days (i.e., the length of the `prices` array), since we iterate over the prices once.

### Space Complexity
The space complexity is O(1), as the size of the `dp` deque remains constant (three states), regardless of the input size.

### Key Insight
The key insight is to use a deque to efficiently keep track of the previous state, allowing us to enforce the cooldown restriction and calculate the maximum profit at each step. This approach enables us to solve the problem in linear time and constant space.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.6 MB (Beats 60.89%) |
| 📅 Solved | 2026-04-20 |
| 💻 Language | Python |