# 567. Permutation in String


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/permutation-in-string/)


## 📝 Problem Description

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

 

Example 1:**

```

**Input:** s1 = "ab", s2 = "eidbaooo"
**Output:** true
**Explanation:** s2 contains one permutation of s1 ("ba").

```

Example 2:**

```

**Input:** s1 = "ab", s2 = "eidboaoo"
**Output:** false

```

 

**Constraints:**

	- `1 <= s1.length, s2.length <= 10^4`

	- `s1` and `s2` consist of lowercase English letters.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 18 ms (Beats 93.78%) |
| 💾 Memory | 12.9 MB (Beats 17.36%) |
| 📅 Solved | 2025-04-02 |
| 💻 Language | Python |