> 📌 **Cross-listed:** Primary location is [Hash Table/3170-Lexicographically-Minimum-String-After-Removing-Stars](../../Hash-Table/3170-Lexicographically-Minimum-String-After-Removing-Stars). This problem also appears under: **Hash Table**, **String**, **Stack**, **Greedy**, **Heap (Priority Queue)**

# 3170. Lexicographically Minimum String After Removing Stars


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/)


## 📝 Problem Description

You are given a string `s`. It may contain any number of `'*'` characters. Your task is to remove all `'*'` characters.

While there is a `'*'`, do the following operation:

	- Delete the leftmost `'*'` and the **smallest** non-`'*'` character to its *left*. If there are several smallest characters, you can delete any of them.

Return the lexicographically smallest resulting string after removing all `'*'` characters.

 

Example 1:**

**Input:** s = "aaba*"

**Output:** "aab"

**Explanation:**

We should delete one of the `'a'` characters with `'*'`. If we choose `s[3]`, `s` becomes the lexicographically smallest.

Example 2:**

**Input:** s = "abc"

**Output:** "abc"

**Explanation:**

There is no `'*'` in the string.

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists only of lowercase English letters and `'*'`.

	- The input is generated such that it is possible to delete all `'*'` characters.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 562 ms (Beats 40.37%) |
| 💾 Memory | 21.7 MB (Beats 99.38%) |
| 📅 Solved | 2025-06-07 |
| 💻 Language | Python |