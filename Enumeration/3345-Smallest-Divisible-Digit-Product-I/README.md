> 📌 **Cross-listed:** Primary location is [Math/3345-Smallest-Divisible-Digit-Product-I](../../Math/3345-Smallest-Divisible-Digit-Product-I). This problem also appears under: **Math**, **Enumeration**

# 3345. Smallest Divisible Digit Product I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/smallest-divisible-digit-product-i/)


## 📝 Problem Description

You are given two integers `n` and `t`. Return the **smallest** number greater than or equal to `n` such that the **product of its digits** is divisible by `t`.

 

Example 1:**

**Input:** n = 10, t = 2

**Output:** 10

**Explanation:**

The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

Example 2:**

**Input:** n = 15, t = 3

**Output:** 16

**Explanation:**

The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.

 

**Constraints:**

	- `1 <= n <= 100`

	- `1 <= t <= 10`

## 🧠 Solution Explanation

**Intuition**
The solution iterates through numbers starting from `n` to find the smallest number whose product of digits is divisible by `t`. This approach is feasible because the constraints ensure that the search space is relatively small.

**Approach**
1. Initialize a variable `i` to start from `n` and iterate up to 100.
2. For each `i`, calculate the product of its digits by repeatedly taking the last digit (`num % 10`), multiplying it with the current product (`curr * last`), and removing the last digit from the number (`num //= 10`).
3. Check if the product of digits (`curr`) is divisible by `t` by using the modulo operator (`curr % t == 0`).
4. If the product is divisible by `t`, return the current number `i`.

**Time Complexity**
O(100 - n) = O(100) because we are iterating from `n` to 100. Although the number of iterations is dependent on `n`, the maximum possible value of `n` is 100, so we can simplify the time complexity to O(100).

**Space Complexity**
O(1) because we are using a constant amount of space to store the variables `i`, `curr`, and `num`. The space usage does not grow with the input size.

**Key Insight**
The key insight is that we can efficiently calculate the product of digits by repeatedly taking the last digit and multiplying it with the current product. This approach avoids the need to store the individual digits, making it space-efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 32.93%) |
| 📅 Solved | 2026-08-06 |
| 💻 Language | Python |