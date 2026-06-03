> 📌 **Cross-listed:** Primary location is [Hash Table/0791-Custom-Sort-String](../../Hash-Table/0791-Custom-Sort-String). This problem also appears under: **Hash Table**, **String**, **Sorting**

# 791. Custom Sort String


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/custom-sort-string/)


## 📝 Problem Description

You are given two strings `order` and `s`. All the characters of `order` are **unique** and were sorted in some custom order previously.

Permute the characters of `s` so that they match the order that `order` was sorted. More specifically, if a character `x` occurs before a character `y` in `order`, then `x` should occur before `y` in the permuted string.

Return *any permutation of *`s`* that satisfies this property*.

 

Example 1:**

**Input: **  order = "cba", s = "abcd" 

**Output: **  "cbad" 

**Explanation: ** `"a"`, `"b"`, `"c"` appear in order, so the order of `"a"`, `"b"`, `"c"` should be `"c"`, `"b"`, and `"a"`.

Since `"d"` does not appear in `order`, it can be at any position in the returned string. `"dcba"`, `"cdba"`, `"cbda"` are also valid outputs.

Example 2:**

**Input: **  order = "bcafg", s = "abcd" 

**Output: **  "bcad" 

**Explanation: ** The characters `"b"`, `"c"`, and `"a"` from `order` dictate the order for the characters in `s`. The character `"d"` in `s` does not appear in `order`, so its position is flexible.

Following the order of appearance in `order`, `"b"`, `"c"`, and `"a"` from `s` should be arranged as `"b"`, `"c"`, `"a"`. `"d"` can be placed at any position since it's not in order. The output `"bcad"` correctly follows this rule. Other arrangements like `"dbca"` or `"bcda"` would also be valid, as long as `"b"`, `"c"`, `"a"` maintain their order.

 

**Constraints:**

	- `1 <= order.length <= 26`

	- `1 <= s.length <= 200`

	- `order` and `s` consist of lowercase English letters.

	- All the characters of `order` are **unique**.

## 🧠 Solution Explanation

**Intuition**
The solution works by first creating a hash table to store the custom order of characters in the `order` string. Then, it sorts the characters in the `s` string based on their custom order, treating characters not in the `order` string as having a high priority (i.e., 26).

**Approach**
1. Create a hash table `h1` to store the custom order of characters in the `order` string.
2. Iterate over the `order` string and store each character as a key in the hash table `h1`, with its value being its index in the `order` string.
3. Sort the characters in the `s` string using the `sorted` function, with a custom key function that looks up each character in the hash table `h1`. If a character is not found in the hash table, it is treated as having a high priority (i.e., 26).
4. Join the sorted characters into a single string using the `"".join()` method.

**Time Complexity**
O(n log n), where n is the length of the `s` string. This is because the `sorted` function has a time complexity of O(n log n) in Python.

**Space Complexity**
O(n), where n is the length of the `order` string. This is because we need to store the custom order of characters in the hash table `h1`.

**Key Insight**
The key insight is to treat characters not in the `order` string as having a high priority, allowing us to sort the characters in the `s` string based on their custom order. This is achieved by using a custom key function that looks up each character in the hash table `h1`, returning its index if found, or 26 if not found.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-02-15 |
| 💻 Language | Python |