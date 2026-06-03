# 122. Best Time to Buy and Sell Stock II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)


## 📝 Problem Description

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can sell and buy the stock multiple times on the **same day**, ensuring you never hold more than one share of the stock.

Find and return *the **maximum** profit you can achieve*.

 

Example 1:**

```

**Input:** prices = [7,1,5,3,6,4]
**Output:** 7
**Explanation:** Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

```

Example 2:**

```

**Input:** prices = [1,2,3,4,5]
**Output:** 4
**Explanation:** Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

```

Example 3:**

```

**Input:** prices = [7,6,4,3,1]
**Output:** 0
**Explanation:** There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

```

 

**Constraints:**

	- `1 <= prices.length <= 3 * 10^4`

	- `0 <= prices[i] <= 10^4`

## 🧠 Solution Explanation

## Intuition
This approach works by iterating through the list of stock prices and checking if the current price is higher than the previous one. If it is, we add the difference to our total profit. The key idea here is to accumulate all the positive differences between consecutive prices, effectively simulating the process of buying and selling the stock multiple times. This greedy strategy takes advantage of every opportunity to make a profit.

## Approach
1. Initialize variables to keep track of the maximum profit.
2. Iterate through the list of stock prices, starting from the second day.
3. For each day, calculate the potential profit by subtracting the previous day's price from the current day's price.
4. If the potential profit is positive, add it to the total profit.
5. After iterating through all the days, return the total profit.

## Time Complexity
The time complexity is O(n), where n is the number of days (i.e., the length of the prices list). This is because we make a single pass through the list of prices.

## Space Complexity
The space complexity is O(1), as we only use a constant amount of space to store the maximum profit and other variables, regardless of the size of the input.

## Key Insight
The key insight behind this solution is that we can maximize our profit by accumulating all the positive differences between consecutive prices, without worrying about the overall trend of the stock prices. This greedy approach works because we can buy and sell the stock multiple times, allowing us to take advantage of every opportunity to make a profit.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 4 ms (Beats 26.3%) |
| 💾 Memory | 20.2 MB (Beats 84.65%) |
| 📅 Solved | 2026-04-17 |
| 💻 Language | Python |