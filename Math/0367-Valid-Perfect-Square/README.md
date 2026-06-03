# 367. Valid Perfect Square


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/valid-perfect-square/)


## 📝 Problem Description

Given a positive integer num, return `true` *if* `num` *is a perfect square or* `false` *otherwise*.

A **perfect square** is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as `sqrt`.

 

Example 1:**

```

**Input:** num = 16
**Output:** true
**Explanation:** We return true because 4 * 4 = 16 and 4 is an integer.

```

Example 2:**

```

**Input:** num = 14
**Output:** false
**Explanation:** We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

```

 

**Constraints:**

	- `1 <= num <= 2^31 - 1`

## 🧠 Solution Explanation

**Intuition**
This solution uses a binary search approach to find the square root of the given number. The key insight is that we can use the property of perfect squares to narrow down the search space. Since the square of any integer is always non-decreasing, we can use a binary search to find the largest integer whose square is less than or equal to the given number.

**Approach**
1. Initialize two pointers, `l` and `r`, to the start and end of the search space, respectively. In this case, the search space is the range `[0, num]`.
2. Calculate the midpoint `mid` of the current search space.
3. Check if the square of `mid` is greater than the given number `num`. If so, update the search space to the left half by setting `r` to `mid - 1`.
4. Check if the square of `mid` is less than `num`. If so, update the search space to the right half by setting `l` to `mid + 1`.
5. If the square of `mid` is equal to `num`, return `True`.
6. Repeat steps 2-5 until `l` is greater than `r`. If the loop ends without finding a perfect square, return `False`.

**Time Complexity**
O(log n), where n is the given number. This is because the binary search space is halved at each iteration, resulting in a logarithmic time complexity.

**Space Complexity**
O(1), since the solution only uses a constant amount of space to store the pointers `l` and `r`.

**Key Insight**
The key insight is that we can use the property of perfect squares to narrow down the search space using a binary search. This approach allows us to find the square root of the given number in logarithmic time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-02-22 |
| 💻 Language | Python |