# 856. Score of Parentheses


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/score-of-parentheses/)


## 📝 Problem Description

Given a balanced parentheses string `s`, return *the **score** of the string*.

The **score** of a balanced parentheses string is based on the following rule:

	- `"()"` has score `1`.

	- `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings.

	- `(A)` has score `2 * A`, where `A` is a balanced parentheses string.

 

Example 1:**

```

**Input:** s = "()"
**Output:** 1

```

Example 2:**

```

**Input:** s = "(())"
**Output:** 2

```

Example 3:**

```

**Input:** s = "()()"
**Output:** 2

```

 

**Constraints:**

	- `2 <= s.length <= 50`

	- `s` consists of only `'('` and `')'`.

	- `s` is a balanced parentheses string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-02-19 |
| 💻 Language | Python |