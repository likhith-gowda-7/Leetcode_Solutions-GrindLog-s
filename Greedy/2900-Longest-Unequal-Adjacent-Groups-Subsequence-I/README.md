> 📌 **Cross-listed:** Primary location is [Array/2900-Longest-Unequal-Adjacent-Groups-Subsequence-I](../../Array/2900-Longest-Unequal-Adjacent-Groups-Subsequence-I). This problem also appears under: **Array**, **String**, **Dynamic Programming**, **Greedy**

# 2900. Longest Unequal Adjacent Groups Subsequence I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/)


## 📝 Problem Description

You are given a string array `words` and a **binary** array `groups` both of length `n`.

A subsequence of `words` is **alternating** if for any two *consecutive* strings in the sequence, their corresponding elements at the *same* indices in `groups` are **different** (that is, there *cannot* be consecutive 0 or 1).

Your task is to select the **longest alternating** subsequence from `words`.

Return *the selected subsequence. If there are multiple answers, return **any** of them.*

**Note:** The elements in `words` are distinct.

 

Example 1:**

**Input:** words = ["e","a","b"], groups = [0,0,1]

**Output:** ["e","b"]

**Explanation:** A subsequence that can be selected is `["e","b"]` because `groups[0] != groups[2]`. Another subsequence that can be selected is `["a","b"]` because `groups[1] != groups[2]`. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is `2`.

Example 2:**

**Input:** words = ["a","b","c","d"], groups = [1,0,1,1]

**Output:** ["a","b","c"]

**Explanation:** A subsequence that can be selected is `["a","b","c"]` because `groups[0] != groups[1]` and `groups[1] != groups[2]`. Another subsequence that can be selected is `["a","b","d"]` because `groups[0] != groups[1]` and `groups[1] != groups[3]`. It can be shown that the length of the longest subsequence of indices that satisfies the condition is `3`.

 

**Constraints:**

	- `1 <= n == words.length == groups.length <= 100`

	- `1 <= words[i].length <= 10`

	- `groups[i]` is either `0` or `1.`

	- `words` consists of **distinct** strings.

	- `words[i]` consists of lowercase English letters.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-05-15 |
| 💻 Language | Python |