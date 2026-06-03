> 📌 **Cross-listed:** Primary location is [String/3407-Substring-Matching-Pattern](../../String/3407-Substring-Matching-Pattern). This problem also appears under: **String**, **String Matching**

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

## 🧠 Solution Explanation

**Intuition**
The solution works by splitting the pattern string `p` into two parts at the `'*'` character. It then checks if the first part is a substring of `s` and if the second part is a substring of `s` starting from the end of the first part. This approach leverages the fact that the `'*'` in `p` can be replaced with any sequence of zero or more characters.

**Approach**
1. Split the pattern string `p` into two parts at the `'*'` character using the `split()` method.
2. Find the index of the `'*'` character in `p` using the `index()` method.
3. Find the index of the first part of `p` in `s` using the `find()` method.
4. Find the index of the second part of `p` in `s` starting from the end of the first part using the `find()` method with a starting index.
5. Return `True` if both indices are not `-1`, indicating that both parts of `p` are substrings of `s`.

**Time Complexity**
O(n + m), where n is the length of `s` and m is the length of `p`. This is because we are using the `find()` method, which has a time complexity of O(n) in the worst case.

**Space Complexity**
O(1), as we are only using a constant amount of space to store the indices and the parts of `p`.

**Key Insight**
The key insight is that we can split the pattern string `p` into two parts at the `'*'` character and then check if both parts are substrings of `s`. This approach allows us to take advantage of the fact that the `'*'` in `p` can be replaced with any sequence of zero or more characters.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 29.23%) |
| 📅 Solved | 2026-03-01 |
| 💻 Language | Python |