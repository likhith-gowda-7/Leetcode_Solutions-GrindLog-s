# 1742. Maximum Number of Balls in a Box


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-number-of-balls-in-a-box/)


## 📝 Problem Description

You are working in a ball factory where you have `n` balls numbered from `lowLimit` up to `highLimit` **inclusive** (i.e., `n == highLimit - lowLimit + 1`), and an infinite number of boxes numbered from `1` to `infinity`.

Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number `321` will be put in the box number `3 + 2 + 1 = 6` and the ball number `10` will be put in the box number `1 + 0 = 1`.

Given two integers `lowLimit` and `highLimit`, return* the number of balls in the box with the most balls.*

 

Example 1:**

```

**Input:** lowLimit = 1, highLimit = 10
**Output:** 2
**Explanation:**
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
Box 1 has the most number of balls with 2 balls.
```

Example 2:**

```

**Input:** lowLimit = 5, highLimit = 15
**Output:** 2
**Explanation:**
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
Boxes 5 and 6 have the most number of balls with 2 balls in each.

```

Example 3:**

```

**Input:** lowLimit = 19, highLimit = 28
**Output:** 2
**Explanation:**
Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
Box 10 has the most number of balls with 2 balls.

```

 

**Constraints:**

	- `1 <= lowLimit <= highLimit <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The problem requires counting the number of balls in the box with the most balls. Each ball's number is put in a box based on the sum of its digits. The key insight is to use a hash table to store the count of balls in each box, where the box number is the sum of the digits of the ball's number.

**Approach**
1. Define a helper function `summing(num)` to calculate the sum of digits of a given number `num`.
2. Initialize a hash table `h1` to store the count of balls in each box.
3. Iterate through the range of ball numbers from `lowLimit` to `highLimit` (inclusive).
4. For each ball number, calculate the sum of its digits using the `summing(num)` function.
5. Increment the count of the corresponding box in the hash table `h1`.
6. After iterating through all ball numbers, return the maximum count in the hash table `h1`.

**Time Complexity**
O(n), where n is the number of balls (highLimit - lowLimit + 1). This is because we are iterating through each ball number once.

**Space Complexity**
O(max(sum of digits of ball numbers)), which is O(highLimit). This is because in the worst case, the sum of digits of a ball number can be equal to the ball number itself, and we are storing the count of each box in the hash table.

**Key Insight**
The key insight is to use a hash table to store the count of balls in each box, where the box number is the sum of the digits of the ball's number. This allows us to efficiently count the number of balls in each box and find the box with the most balls.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 199 ms (Beats 70.02%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-07 |
| 💻 Language | Python |