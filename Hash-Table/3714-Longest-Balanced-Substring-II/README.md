# 3714. Longest Balanced Substring II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-balanced-substring-ii/)


## 📝 Problem Description

You are given a string `s` consisting only of the characters `'a'`, `'b'`, and `'c'`.

A **substring** of `s` is called **balanced** if all **distinct** characters in the **substring** appear the **same** number of times.

Return the **length of the longest balanced substring** of `s`.

 

Example 1:**

**Input:** s = "abbac"

**Output:** 4

**Explanation:**

The longest balanced substring is `"abba"` because both distinct characters `'a'` and `'b'` each appear exactly 2 times.

Example 2:**

**Input:** s = "aabcc"

**Output:** 3

**Explanation:**

The longest balanced substring is `"abc"` because all distinct characters `'a'`, `'b'` and `'c'` each appear exactly 1 time.

Example 3:**

**Input:** s = "aba"

**Output:** 2

**Explanation:**

One of the longest balanced substrings is `"ab"` because both distinct characters `'a'` and `'b'` each appear exactly 1 time. Another longest balanced substring is `"ba"`.

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` contains only the characters `'a'`, `'b'`, and `'c'`.

## 🧠 Solution Explanation

**Intuition**
The solution works by breaking down the problem into three cases: when all characters are the same, when two characters are the same, and when three characters are the same. For each case, it uses a hash table to store the count of characters and their positions, and then finds the maximum length of the balanced substring.

**Approach**

1. The `mono` function handles the case when all characters are the same. It initializes a counter `cnt` to 1 and iterates through the string, incrementing `cnt` if the current character is the same as the previous one, and resetting `cnt` to 1 otherwise. It keeps track of the maximum value of `cnt` and returns it.
2. The `duo` function handles the case when two characters are the same. It uses a hash table `pos` to store the count of characters and their positions. It iterates through the string, updating the count of characters and their positions, and checks if the current count is in the hash table. If it is, it updates the maximum length of the balanced substring. If not, it adds the current count to the hash table.
3. The `trio` function handles the case when three characters are the same. It uses a hash table `pos` to store the count of characters and their positions. It iterates through the string, updating the count of characters and their positions, and checks if the current count is in the hash table. If it is, it updates the maximum length of the balanced substring. If not, it adds the current count to the hash table.
4. The `longestBalanced` function calls the `mono`, `duo`, and `trio` functions for each case and returns the maximum length of the balanced substring.

**Time Complexity**
The time complexity of the solution is O(n), where n is the length of the string. This is because each function iterates through the string once, and the hash table operations take constant time.

**Space Complexity**
The space complexity of the solution is O(n), where n is the length of the string. This is because the hash table can store up to n elements in the worst case.

**Key Insight**
The key insight behind the solution is to break down the problem into three cases and use a hash table to store the count of characters and their positions. This allows us to efficiently find the maximum length of the balanced substring for each case.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 803 ms (Beats 93.83%) |
| 💾 Memory | 45.2 MB (Beats 87.22%) |
| 📅 Solved | 2026-02-13 |
| 💻 Language | Python |