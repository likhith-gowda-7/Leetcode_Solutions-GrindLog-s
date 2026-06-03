> 📌 **Cross-listed:** Primary location is [Hash Table/3442-Maximum-Difference-Between-Even-and-Odd-Frequency-I](../../Hash-Table/3442-Maximum-Difference-Between-Even-and-Odd-Frequency-I). This problem also appears under: **Hash Table**, **String**, **Counting**

# 3442. Maximum Difference Between Even and Odd Frequency I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/)


## 📝 Problem Description

You are given a string `s` consisting of lowercase English letters.

Your task is to find the **maximum** difference `diff = freq(a_1) - freq(a_2)` between the frequency of characters `a_1` and `a_2` in the string such that:

	- `a_1` has an **odd frequency** in the string.

	- `a_2` has an **even frequency** in the string.

Return this **maximum** difference.

 

Example 1:**

**Input:** s = "aaaaabbc"

**Output:** 3

**Explanation:**

	- The character `'a'` has an **odd frequency** of `5`, and `'b'` has an **even frequency** of `2`.

	- The maximum difference is `5 - 2 = 3`.

Example 2:**

**Input:** s = "abcabcab"

**Output:** 1

**Explanation:**

	- The character `'a'` has an **odd frequency** of `3`, and `'c'` has an **even frequency** of 2.

	- The maximum difference is `3 - 2 = 1`.

 

**Constraints:**

	- `3 <= s.length <= 100`

	- `s` consists only of lowercase English letters.

	- `s` contains at least one character with an odd frequency and one with an even frequency.

## 🧠 Solution Explanation

**Intuition**
The solution works by utilizing a hash table (Counter in Python) to efficiently count the frequency of each character in the string. It then iterates through the hash table to find the maximum odd frequency and the minimum even frequency, and returns their difference.

**Approach**
1. Create a hash table (Counter) to count the frequency of each character in the string.
2. Initialize variables `even` and `odd` to store the minimum even frequency and the maximum odd frequency, respectively.
3. Iterate through the hash table. For each character:
   - If the frequency is odd, update `odd` to be the maximum of its current value and the current frequency.
   - If the frequency is even, update `even` to be the minimum of its current value and the current frequency.
4. Return the difference between `odd` and `even`.

**Time Complexity**
O(n), where n is the length of the string. This is because we iterate through the string once to count the frequency of each character, and then iterate through the hash table once to find the maximum odd frequency and the minimum even frequency.

**Space Complexity**
O(n), where n is the length of the string. This is because we use a hash table to store the frequency of each character, which requires O(n) space in the worst case.

**Key Insight**
The key insight is that we can use a single pass through the hash table to find both the maximum odd frequency and the minimum even frequency, which allows us to solve the problem efficiently with a time complexity of O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-06-10 |
| 💻 Language | Python |