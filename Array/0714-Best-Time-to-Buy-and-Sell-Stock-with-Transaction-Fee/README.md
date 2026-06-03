# 714. Best Time to Buy and Sell Stock with Transaction Fee


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)


## 📝 Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day, and an integer `fee` representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

**Note:**

	- You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

	- The transaction fee is only charged once for each stock purchase and sale.

 

Example 1:**

```

**Input:** prices = [1,3,2,8,4,9], fee = 2
**Output:** 8
**Explanation:** The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

```

Example 2:**

```

**Input:** prices = [1,3,7,5,10,3], fee = 3
**Output:** 6

```

 

**Constraints:**

	- `1 <= prices.length <= 5 * 10^4`

	- `1 <= prices[i] < 5 * 10^4`

	- `0 <= fee < 5 * 10^4`

## 🧠 Solution Explanation

**Intuition**
This solution uses a greedy approach to maximize profit by buying and selling stocks at optimal times, considering the transaction fee. The key insight is to maintain a running balance of the maximum profit that can be achieved, taking into account the transaction fee for each trade.

**Approach**
1. Initialize `profit` to 0 and `buy` to the price of the first stock.
2. Iterate through the prices array starting from the second price.
3. If the current price is less than the `buy` price, update `buy` to the current price.
4. If the current price is greater than the `buy` price plus the transaction fee, calculate the profit for this trade and add it to the total profit. Update `buy` to the current price minus the transaction fee.

**Time Complexity**
O(n), where n is the number of prices. This is because we only iterate through the prices array once.

**Space Complexity**
O(1), since we only use a constant amount of space to store the `profit` and `buy` variables.

**Key Insight**
The key to this solution is to recognize that we can always buy the stock at the current price if it's lower than the previous buy price, and sell the stock at the current price if it's higher than the previous buy price plus the transaction fee. This greedy approach ensures that we maximize the profit while considering the transaction fee.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 35 ms (Beats 97.62%) |
| 💾 Memory | 26.2 MB (Beats 75.89%) |
| 📅 Solved | 2026-04-30 |
| 💻 Language | Python |