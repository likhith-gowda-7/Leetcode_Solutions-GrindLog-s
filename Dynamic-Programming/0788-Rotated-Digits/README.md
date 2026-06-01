> 📌 **Cross-listed:** Primary location is [Math/0788-Rotated-Digits](../../Math/0788-Rotated-Digits). This problem also appears under: **Math**, **Dynamic Programming**

# 788. Rotated Digits


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rotated-digits/)


## 📝 Problem Description

An integer `x` is a **good** if after rotating each digit individually by 180 degrees, we get a valid number that is different from `x`. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

	- `0`, `1`, and `8` rotate to themselves,

	- `2` and `5` rotate to each other (in this case they are rotated in a different direction, in other words, `2` or `5` gets mirrored),

	- `6` and `9` rotate to each other, and

	- the rest of the numbers do not rotate to any other number and become invalid.

Given an integer `n`, return *the number of **good** integers in the range *`[1, n]`.

 

Example 1:**

```

**Input:** n = 10
**Output:** 4
**Explanation:** There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

```

Example 2:**

```

**Input:** n = 1
**Output:** 0

```

Example 3:**

```

**Input:** n = 2
**Output:** 1

```

 

**Constraints:**

	- `1 <= n <= 10^4`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 27 ms (Beats 57.26%) |
| 💾 Memory | 19.4 MB (Beats 31.06%) |
| 📅 Solved | 2026-05-02 |
| 💻 Language | Python |