# 2110. Number of Smooth Descent Periods of a Stock


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/)


## 📝 Problem Description

You are given an integer array `prices` representing the daily price history of a stock, where `prices[i]` is the stock price on the `i^th` day.

A **smooth descent period** of a stock consists of **one or more contiguous** days such that the price on each day is **lower** than the price on the **preceding day** by **exactly** `1`. The first day of the period is exempted from this rule.

Return *the number of **smooth descent periods***.

 

Example 1:**

```

**Input:** prices = [3,2,1,4]
**Output:** 7
**Explanation:** There are 7 smooth descent periods:
[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
Note that a period with one day is a smooth descent period by the definition.

```

Example 2:**

```

**Input:** prices = [8,6,7,7]
**Output:** 4
**Explanation:** There are 4 smooth descent periods: [8], [6], [7], and [7]
Note that [8,6] is not a smooth descent period as 8 - 6 &ne; 1.

```

Example 3:**

```

**Input:** prices = [1]
**Output:** 1
**Explanation:** There is 1 smooth descent period: [1]

```

 

**Constraints:**

	- `1 <= prices.length <= 10^5`

	- `1 <= prices[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The problem asks for the number of smooth descent periods in a stock's price history. A smooth descent period consists of one or more contiguous days where the price decreases by exactly 1. The approach involves calculating the number of combinations of days that can form a smooth descent period.

**Approach**
1. Initialize variables to store the result and the length of the current smooth descent period.
2. Iterate through the price history, starting from the second day.
3. For each day, calculate the difference in price with the previous day.
4. If the difference is not 1, it means the current smooth descent period has ended.
5. Calculate the number of combinations of days in the current period using the formula `length*(length+1)//2`.
6. Add the combinations to the result and update the length of the current period.
7. After iterating through the entire price history, calculate the combinations for the last period and add it to the result.

**Time Complexity**
O(n), where n is the number of days in the price history. This is because we only need to iterate through the price history once.

**Space Complexity**
O(1), as we only use a constant amount of space to store the result and the length of the current period.

**Key Insight**
The key insight is that the number of combinations of days in a smooth descent period can be calculated using the formula `length*(length+1)//2`. This formula is derived from the fact that the number of combinations of n items taken k at a time is given by `n!/(k!(n-k)!)`, which simplifies to `n*(n-1)*...*(n-k+1)/k!`. In this case, we can simplify the formula to `length*(length+1)//2` because the number of combinations is always an integer and we can ignore the factorial term.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 57 ms (Beats 85.4%) |
| 💾 Memory | 29.7 MB (Beats 100%) |
| 📅 Solved | 2025-12-16 |
| 💻 Language | Python |