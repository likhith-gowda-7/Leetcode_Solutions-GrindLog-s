# 1653. Minimum Deletions to Make String Balanced


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Stack](https://img.shields.io/badge/Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/)


## 📝 Problem Description

You are given a string `s` consisting only of characters `'a'` and `'b'`​​​​.

You can delete any number of characters in `s` to make `s` **balanced**. `s` is **balanced** if there is no pair of indices `(i,j)` such that `i < j` and `s[i] = 'b'` and `s[j]= 'a'`.

Return *the **minimum** number of deletions needed to make *`s`* **balanced***.

 

Example 1:**

```

**Input:** s = "aababbab"
**Output:** 2
**Explanation:** You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

```

Example 2:**

```

**Input:** s = "bbaaaaabb"
**Output:** 2
**Explanation:** The only solution is to delete the first two characters.

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s[i]` is `'a'` or `'b'`​​.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 141 ms (Beats 88.9%) |
| 💾 Memory | 20.1 MB (Beats 74.2%) |
| 📅 Solved | 2026-02-07 |
| 💻 Language | Python |