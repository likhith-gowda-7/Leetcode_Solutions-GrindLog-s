# 1784. Check if Binary String Has at Most One Segment of Ones


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/)


## 📝 Problem Description

Given a binary string `s` **​​​​​without leading zeros**, return `true`​​​ *if *`s`* contains **at most one contiguous segment of ones***. Otherwise, return `false`.

 

Example 1:**

```

**Input:** s = "1001"
**Output:** false
**Explanation: **The string has two segments of size 1.

```

Example 2:**

```

**Input:** s = "110"
**Output:** true
```

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `s[i]`​​​​ is either `'0'` or `'1'`.

	- `s[0]` is `'1'`.

## 🧠 Solution Explanation

**Intuition**
The key insight here is that we can simply check if the string contains the substring "01", which indicates the presence of two contiguous segments of ones. If it doesn't contain "01", it means there's at most one segment of ones.

**Approach**
1. The solution checks if the string `s` contains the substring "01".
2. If "01" is found, it means there are two contiguous segments of ones, so the function returns `False`.
3. If "01" is not found, it means there's at most one segment of ones, so the function returns `True`.

**Time Complexity**
O(n), where n is the length of the string `s`. This is because we're using the `in` operator to check if the substring "01" exists in `s`, which has a linear time complexity.

**Space Complexity**
O(1), which means the space required does not change with the size of the input string `s`. We're only using a constant amount of space to store the substring "01" and the return value.

**Key Insight**
The key insight here is that the presence of "01" in the string indicates two contiguous segments of ones, and its absence indicates at most one segment of ones. This simple check allows us to solve the problem efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 45.11%) |
| 📅 Solved | 2026-03-06 |
| 💻 Language | Python |