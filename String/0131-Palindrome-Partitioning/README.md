# 131. Palindrome Partitioning


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Backtracking](https://img.shields.io/badge/Backtracking-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/palindrome-partitioning/)


## 📝 Problem Description

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return *all possible palindrome partitioning of *`s`.

 

Example 1:**

```
**Input:** s = "aab"
**Output:** [["a","a","b"],["aa","b"]]

```
Example 2:**

```
**Input:** s = "a"
**Output:** [["a"]]

```

 

**Constraints:**

	- `1 <= s.length <= 16`

	- `s` contains only lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a backtracking approach to find all possible palindrome partitions of the given string. It checks every substring of the string to see if it's a palindrome and recursively adds it to the current partition if it is.

**Approach**
1. Initialize an empty list `res` to store the result and an empty list `part` to store the current partition.
2. Define a helper function `palin(l, r)` to check if a substring from index `l` to `r` is a palindrome.
3. Define a recursive helper function `backtrack(start)` to explore all possible partitions.
4. In `backtrack(start)`, if the current start index is equal to the length of the string, it means we've found a complete partition, so append a copy of the current partition to the result list.
5. For every index `i` from `start` to the end of the string, check if the substring from `start` to `i` is a palindrome using `palin(start, i)`.
6. If it's a palindrome, add it to the current partition and recursively call `backtrack(i + 1)`.
7. After the recursive call, remove the last added partition from the current partition to backtrack.
8. Finally, return the result list.

**Time Complexity**
The time complexity is O(2^n * n), where n is the length of the string. This is because we're exploring all possible partitions of the string, and for each partition, we're checking every substring to see if it's a palindrome. The 2^n factor comes from the fact that we're recursively exploring all possible partitions, and the n factor comes from the fact that we're checking every substring.

**Space Complexity**
The space complexity is O(n), which is the maximum depth of the recursion tree. In the worst case, we're exploring all possible partitions, and the maximum depth of the recursion tree is equal to the length of the string.

**Key Insight**
The key insight is to use a backtracking approach to explore all possible partitions of the string. By checking every substring to see if it's a palindrome, we can efficiently find all possible palindrome partitions of the string. The use of a recursive helper function `backtrack(start)` allows us to elegantly explore all possible partitions and avoids the need for explicit loops.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 43 ms (Beats 60.57%) |
| 💾 Memory | 34 MB (Beats 61.88%) |
| 📅 Solved | 2026-01-03 |
| 💻 Language | Python |