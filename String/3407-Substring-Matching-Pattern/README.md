# 3407. Substring Matching Pattern


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![String Matching](https://img.shields.io/badge/String%20Matching-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/substring-matching-pattern/)


## 📝 Problem Description

You are given a string `s` and a pattern string `p`, where `p` contains **exactly one** `'*'` character.

The `'*'` in `p` can be replaced with any sequence of zero or more characters.

Return `true` if `p` can be made a substring of `s`, and `false` otherwise.

 

Example 1:**

**Input:** s = "leetcode", p = "ee*e"

**Output:** true

**Explanation:**

By replacing the `'*'` with `"tcod"`, the substring `"eetcode"` matches the pattern.

Example 2:**

**Input:** s = "car", p = "c*v"

**Output:** false

**Explanation:**

There is no substring matching the pattern.

Example 3:**

**Input:** s = "luck", p = "u*"

**Output:** true

**Explanation:**

The substrings `"u"`, `"uc"`, and `"uck"` match the pattern.

 

**Constraints:**

	- `1 <= s.length <= 50`

	- `1 <= p.length <= 50 `

	- `s` contains only lowercase English letters.

	- `p` contains only lowercase English letters and exactly one `'*'`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 28.09%) |
| 📅 Solved | 2026-03-01 |
| 💻 Language | Python |