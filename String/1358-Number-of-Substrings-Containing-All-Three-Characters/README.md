> 📌 **Cross-listed:** Primary location is [Hash Table/1358-Number-of-Substrings-Containing-All-Three-Characters](../../Hash-Table/1358-Number-of-Substrings-Containing-All-Three-Characters). This problem also appears under: **Hash Table**, **String**, **Sliding Window**

# 1358. Number of Substrings Containing All Three Characters


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)


## 📝 Problem Description

Given a string `s` consisting only of characters *a*, *b* and *c*.

Return the number of substrings containing **at least** one occurrence of all these characters *a*, *b* and *c*.

 

Example 1:**

```

**Input:** s = "abcabc"
**Output:** 10
**Explanation:** The substrings containing at least one occurrence of the characters *a*, *b* and *c are "*abc*", "*abca*", "*abcab*", "*abcabc*", "*bca*", "*bcab*", "*bcabc*", "*cab*", "*cabc*" *and* "*abc*" *(**again**)*. *

```

Example 2:**

```

**Input:** s = "aaacb"
**Output:** 3
**Explanation:** The substrings containing at least one occurrence of the characters *a*, *b* and *c are "*aaacb*", "*aacb*" *and* "*acb*".** *

```

Example 3:**

```

**Input:** s = "abc"
**Output:** 1

```

 

**Constraints:**

	- `3 <= s.length <= 5 x 10^4`

	- `s` only consists of *a*, *b* or *c *characters.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 98 ms (Beats 66.3%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-03-11 |
| 💻 Language | Python |