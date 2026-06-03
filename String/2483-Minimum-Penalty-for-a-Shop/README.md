# 2483. Minimum Penalty for a Shop


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-penalty-for-a-shop/)


## 📝 Problem Description

You are given the customer visit log of a shop represented by a **0-indexed** string `customers` consisting only of characters `'N'` and `'Y'`:

	- if the `i^th` character is `'Y'`, it means that customers come at the `i^th` hour

	- whereas `'N'` indicates that no customers come at the `i^th` hour.

If the shop closes at the `j^th` hour (`0 <= j <= n`), the **penalty** is calculated as follows:

	- For every hour when the shop is open and no customers come, the penalty increases by `1`.

	- For every hour when the shop is closed and customers come, the penalty increases by `1`.

Return* the **earliest** hour at which the shop must be closed to incur a **minimum** penalty.*

**Note** that if a shop closes at the `j^th` hour, it means the shop is closed at the hour `j`.

 

Example 1:**

```

**Input:** customers = "YYNY"
**Output:** 2
**Explanation:** 
- Closing the shop at the 0^th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1^st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2^nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3^rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4^th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2^nd or 4^th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

```

Example 2:**

```

**Input:** customers = "NNNNN"
**Output:** 0
**Explanation:** It is best to close the shop at the 0^th hour as no customers arrive.
```

Example 3:**

```

**Input:** customers = "YYYY"
**Output:** 4
**Explanation:** It is best to close the shop at the 4^th hour as customers arrive at each hour.

```

 

**Constraints:**

	- `1 <= customers.length <= 10^5`

	- `customers` consists only of characters `'Y'` and `'N'`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a prefix sum approach to efficiently calculate the minimum penalty for a shop. By maintaining a running count of customers and non-customers, we can quickly compute the penalty for each possible closing hour. The key insight is to recognize that the penalty is determined by the difference between the total number of customers and the number of customers that arrive during the shop's operating hours.

**Approach**
1. Initialize variables to store the total number of customers, the minimum penalty, and the corresponding closing hour.
2. Iterate through the customer visit log, maintaining a running count of customers (`curr`) and non-customers (`No`).
3. For each hour, compute the penalty as the sum of non-customers (`No`) and the difference between the total number of customers and the current count of customers (`Yes`).
4. Update the minimum penalty and corresponding closing hour if a lower penalty is found.
5. Return the closing hour with the minimum penalty.

**Time Complexity**
O(n), where n is the length of the customer visit log. This is because we iterate through the log once, performing a constant amount of work for each hour.

**Space Complexity**
O(1), since we only use a few variables to store the necessary information, regardless of the input size.

**Key Insight**
The solution relies on the fact that the penalty is determined by the difference between the total number of customers and the number of customers that arrive during the shop's operating hours. By maintaining a running count of customers and non-customers, we can efficiently compute the penalty for each possible closing hour, allowing us to find the minimum penalty in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 90 ms (Beats 36.22%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-12-26 |
| 💻 Language | Python |