> 📌 **Cross-listed:** Primary location is [Two Pointers/0344-Reverse-String](../../Two-Pointers/0344-Reverse-String). This problem also appears under: **Two Pointers**, **String**

# 344. Reverse String


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reverse-string/)


## 📝 Problem Description

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with `O(1)` extra memory.

 

Example 1:**

```
**Input:** s = ["h","e","l","l","o"]
**Output:** ["o","l","l","e","h"]

```
Example 2:**

```
**Input:** s = ["H","a","n","n","a","h"]
**Output:** ["h","a","n","n","a","H"]

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s[i]` is a [printable ascii character](https://en.wikipedia.org/wiki/ASCII#Printable_characters).

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pointer approach to reverse the string in-place, taking advantage of the fact that we can swap elements without using extra memory.

**Approach**
1. Initialize two pointers, `l` and `r`, to the start and end of the string, respectively.
2. While `l` is less than `r`, swap the elements at indices `l` and `r`.
3. Increment `l` and decrement `r` to move the pointers towards the center of the string.
4. Repeat steps 2-3 until `l` meets or crosses `r`, at which point the string is reversed.

**Time Complexity**
O(n/2) = O(n), where n is the length of the string. This is because we're swapping elements in a single pass through the string.

**Space Complexity**
O(1), as we're modifying the input array in-place without using any extra memory.

**Key Insight**
The key insight is that we can use two pointers to swap elements in a single pass, taking advantage of the fact that we're working in-place. This approach avoids the need for extra memory and makes the solution efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 23.1 MB (Beats 99.9%) |
| 📅 Solved | 2025-01-22 |
| 💻 Language | Python |