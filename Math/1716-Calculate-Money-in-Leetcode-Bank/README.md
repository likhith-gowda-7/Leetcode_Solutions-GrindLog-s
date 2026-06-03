# 1716. Calculate Money in Leetcode Bank


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)


## 📝 Problem Description

Hercy wants to save money for his first car. He puts money in the Leetcode bank **every day**.

He starts by putting in `$1` on Monday, the first day. Every day from Tuesday to Sunday, he will put in `$1` more than the day before. On every subsequent Monday, he will put in `$1` more than the **previous Monday**. 

Given `n`, return *the total amount of money he will have in the Leetcode bank at the end of the *`n^th`* day.*

 

Example 1:**

```

**Input:** n = 4
**Output:** 10
**Explanation:** After the 4^th day, the total is 1 + 2 + 3 + 4 = 10.

```

Example 2:**

```

**Input:** n = 10
**Output:** 37
**Explanation:** After the 10^th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2^nd Monday, Hercy only puts in $2.

```

Example 3:**

```

**Input:** n = 20
**Output:** 96
**Explanation:** After the 20^th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.

```

 

**Constraints:**

	- `1 <= n <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution calculates the total money in the LeetCode bank by breaking down the problem into two parts: the total money earned from the full weeks and the additional money earned from the remaining days. This approach takes advantage of the fact that the money earned per week increases by $1 each week.

**Approach**
1. Calculate the total number of full weeks (`total_weeks`) by integer dividing `n` by 7.
2. Calculate the number of remaining days (`pay_days`) by finding the remainder of `n` divided by 7.
3. Initialize `inc` to 1, which represents the increment of money earned per week.
4. For each full week, calculate the total money earned by adding `28 + (inc * 7)` to `total_money` and increment `inc` by 1.
5. After the full weeks, increment `inc` by 1 to account for the additional increment on the next Monday.
6. For each remaining day, add `inc` to `total_money` and increment `inc` by 1.
7. Return `total_money` as the total amount of money earned.

**Time Complexity**
O(n), where n is the input number of days. This is because the solution iterates over the full weeks and remaining days, which is proportional to the input size.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the variables `total_weeks`, `pay_days`, `inc`, and `total_money`.

**Key Insight**
The key insight is to break down the problem into two parts: the total money earned from the full weeks and the additional money earned from the remaining days. This allows us to take advantage of the fact that the money earned per week increases by $1 each week, making the solution more efficient and easier to understand.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-10-26 |
| 💻 Language | Python |