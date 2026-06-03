# 28. Find the Index of the First Occurrence in a String


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![String Matching](https://img.shields.io/badge/String%20Matching-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)


## 📝 Problem Description

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

 

Example 1:**

```

**Input:** haystack = "sadbutsad", needle = "sad"
**Output:** 0
**Explanation:** "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

```

Example 2:**

```

**Input:** haystack = "leetcode", needle = "leeto"
**Output:** -1
**Explanation:** "leeto" did not occur in "leetcode", so we return -1.

```

 

**Constraints:**

	- `1 <= haystack.length, needle.length <= 10^4`

	- `haystack` and `needle` consist of only lowercase English characters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a simple iterative approach to find the first occurrence of the `needle` string within the `haystack` string. It checks each substring of the `haystack` with the same length as the `needle` and returns the index of the first match.

**Approach**
1. Check if the `needle` is an empty string. If so, return 0 as per the problem constraints.
2. Iterate over the `haystack` string, considering substrings of the same length as the `needle`.
3. For each substring, check if it matches the `needle` string.
4. If a match is found, return the index of the first character of the matched substring.
5. If no match is found after iterating over the entire `haystack`, return -1.

**Time Complexity**
O(n*m), where n is the length of the `haystack` and m is the length of the `needle`. This is because in the worst case, we need to check every substring of the `haystack` with the same length as the `needle`.

**Space Complexity**
O(1), as we only use a constant amount of space to store the indices and the current substring being checked.

**Key Insight**
The key insight here is that we can efficiently find the first occurrence of the `needle` by checking substrings of the `haystack` with the same length as the `needle`. This approach avoids the need for more complex string matching algorithms, making it suitable for this problem.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 21.46%) |
| 💾 Memory | 17.5 MB (Beats 100%) |
| 📅 Solved | 2025-12-06 |
| 💻 Language | Python |