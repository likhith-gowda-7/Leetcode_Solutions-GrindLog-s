# 227. Basic Calculator II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/basic-calculator-ii/)


## 📝 Problem Description

Given a string `s` which represents an expression, *evaluate this expression and return its value*. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2^31, 2^31 - 1]`.

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

 

Example 1:**

```
**Input:** s = "3+2*2"
**Output:** 7

```
Example 2:**

```
**Input:** s = " 3/2 "
**Output:** 1

```
Example 3:**

```
**Input:** s = " 3+5 / 2 "
**Output:** 5

```

 

**Constraints:**

	- `1 <= s.length <= 3 * 10^5`

	- `s` consists of integers and operators `('+', '-', '*', '/')` separated by some number of spaces.

	- `s` represents **a valid expression**.

	- All the integers in the expression are non-negative integers in the range `[0, 2^31 - 1]`.

	- The answer is **guaranteed** to fit in a **32-bit integer**.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 43 ms (Beats 82.9%) |
| 💾 Memory | 22 MB (Beats 80.67%) |
| 📅 Solved | 2025-01-28 |
| 💻 Language | Python |