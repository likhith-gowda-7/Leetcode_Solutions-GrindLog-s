> 📌 **Cross-listed:** Primary location is [Hash Table/3713-Longest-Balanced-Substring-I](../../Hash-Table/3713-Longest-Balanced-Substring-I). This problem also appears under: **Hash Table**, **String**, **Counting**, **Enumeration**

# 3713. Longest Balanced Substring I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Counting](https://img.shields.io/badge/Counting-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-balanced-substring-i/)


## 📝 Problem Description

You are given a string `s` consisting of lowercase English letters.

A **substring** of `s` is called **balanced** if all **distinct** characters in the **substring** appear the **same** number of times.

Return the **length** of the **longest balanced substring** of `s`.

 

Example 1:**

**Input:** s = "abbac"

**Output:** 4

**Explanation:**

The longest balanced substring is `"abba"` because both distinct characters `'a'` and `'b'` each appear exactly 2 times.

Example 2:**

**Input:** s = "zzabccy"

**Output:** 4

**Explanation:**

The longest balanced substring is `"zabc"` because the distinct characters `'z'`, `'a'`, `'b'`, and `'c'` each appear exactly 1 time.​​​​​​​

Example 3:**

**Input:** s = "aba"

**Output:** 2

**Explanation:**

**​​​​​​​**One of the longest balanced substrings is `"ab"` because both distinct characters `'a'` and `'b'` each appear exactly 1 time. Another longest balanced substring is `"ba"`.

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach to find the longest balanced substring. It maintains a frequency count of characters within the current window and checks if all characters appear the same number of times. If they do, it updates the result with the length of the current window.

**Approach**
1. Initialize a variable `res` to store the length of the longest balanced substring found so far.
2. Iterate over the string `s` using a sliding window approach, where the window starts at index `i` and expands to the right.
3. For each window, maintain a frequency count of characters using a hash table `h1`.
4. Update the maximum frequency `maxi` and minimum frequency `mini` within the current window.
5. Check if the minimum frequency `mini` is equal to the maximum frequency `maxi`. If they are equal, it means all characters in the current window appear the same number of times.
6. If the window is balanced, update the result `res` with the length of the current window.
7. Repeat steps 2-6 until the end of the string is reached.

**Time Complexity**
O(n^2), where n is the length of the string `s`. This is because the solution uses a nested loop structure, where the outer loop iterates over the string and the inner loop expands the window to the right.

**Space Complexity**
O(n), where n is the length of the string `s`. This is because the solution uses a hash table `h1` to store the frequency count of characters within the current window.

**Key Insight**
The key insight is to use a sliding window approach to efficiently check all possible substrings of the input string. By maintaining a frequency count of characters within the current window, we can quickly determine if the window is balanced and update the result accordingly.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2211 ms (Beats 63.86%) |
| 💾 Memory | 19.3 MB (Beats 62.58%) |
| 📅 Solved | 2026-02-12 |
| 💻 Language | Python |