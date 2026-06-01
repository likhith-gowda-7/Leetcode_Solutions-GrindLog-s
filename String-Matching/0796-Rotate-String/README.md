> 📌 **Cross-listed:** Primary location is [String/0796-Rotate-String](../../String/0796-Rotate-String). This problem also appears under: **String**, **String Matching**

# 796. Rotate String


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![String Matching](https://img.shields.io/badge/String%20Matching-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rotate-string/)


## 📝 Problem Description

Given two strings `s` and `goal`, return `true` *if and only if* `s` *can become* `goal` *after some number of **shifts** on* `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

	- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

 

Example 1:**

```
**Input:** s = "abcde", goal = "cdeab"
**Output:** true

```
Example 2:**

```
**Input:** s = "abcde", goal = "abced"
**Output:** false

```

 

**Constraints:**

	- `1 <= s.length, goal.length <= 100`

	- `s` and `goal` consist of lowercase English letters.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 17.72%) |
| 📅 Solved | 2026-05-03 |
| 💻 Language | Python |