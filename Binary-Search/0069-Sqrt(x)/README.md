> 📌 **Cross-listed:** Primary location is [Math/0069-Sqrt(x)](../../Math/0069-Sqrt(x)). This problem also appears under: **Math**, **Binary Search**

# 69. Sqrt(x)


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/sqrtx/)


## 📝 Problem Description

Given a non-negative integer `x`, return *the square root of *`x`* rounded down to the nearest integer*. The returned integer should be **non-negative** as well.

You **must not use** any built-in exponent function or operator.

	- For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

 

Example 1:**

```

**Input:** x = 4
**Output:** 2
**Explanation:** The square root of 4 is 2, so we return 2.

```

Example 2:**

```

**Input:** x = 8
**Output:** 2
**Explanation:** The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

```

 

**Constraints:**

	- `0 <= x <= 2^31 - 1`

## 🧠 Solution Explanation

**Intuition**
The solution uses a binary search approach to find the square root of a given number. It iteratively narrows down the search space by checking if the midpoint squared is greater than, less than, or equal to the target number. This process continues until the midpoint squared is less than the target number, at which point the previous midpoint is the largest perfect square less than or equal to the target number.

**Approach**
1. Initialize two pointers, `l` and `r`, to 1 and `x` respectively, representing the search space.
2. While `l` is less than or equal to `r`, calculate the midpoint `mid` as the average of `l` and `r`.
3. Check if `mid` squared is greater than `x`. If true, update `r` to `mid - 1` to narrow the search space.
4. Check if `mid` squared is less than `x`. If true, update `l` to `mid + 1` to narrow the search space.
5. If `mid` squared is equal to `x`, return `mid` as the square root.
6. Repeat steps 2-5 until `l` is greater than `r`. At this point, `r` will be the largest perfect square less than or equal to `x`, so return `r`.

**Time Complexity**
O(log x) - The binary search approach reduces the search space by half at each iteration, resulting in a logarithmic time complexity.

**Space Complexity**
O(1) - The solution only uses a constant amount of space to store the pointers `l` and `r`, so the space complexity is O(1).

**Key Insight**
The key insight is to use binary search to find the largest perfect square less than or equal to the target number, which can be done in logarithmic time complexity. This approach avoids the need for explicit looping or exponentiation, making it efficient and elegant.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-21 |
| 💻 Language | Python |