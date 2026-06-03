> 📌 **Cross-listed:** Primary location is [Hash Table/0387-First-Unique-Character-in-a-String](../../Hash-Table/0387-First-Unique-Character-in-a-String). This problem also appears under: **Hash Table**, **String**, **Queue**, **Counting**

# 387. First Unique Character in a String


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)


## 📝 Problem Description

Given a string `s`, find the **first** non-repeating character in it and return its index. If it **does not** exist, return `-1`.

 

Example 1:**

**Input:** s = "leetcode"

**Output:** 0

**Explanation:**

The character `'l'` at index 0 is the first character that does not occur at any other index.

Example 2:**

**Input:** s = "loveleetcode"

**Output:** 2

Example 3:**

**Input:** s = "aabb"

**Output:** -1

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of only lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table (implemented as a Counter object) to count the frequency of each character in the string. It then iterates through the hash table to find the first character that appears only once. This approach works because it takes advantage of the fact that the string is relatively small and can be processed in a single pass.

**Approach**
1. Create a hash table (Counter object) to count the frequency of each character in the string.
2. Iterate through the hash table to find the first character that has a count of 1.
3. If such a character is found, return its index in the string using the `find()` method.
4. If no such character is found, return -1.

**Time Complexity**
O(n), where n is the length of the string. This is because we are iterating through the string twice: once to count the frequency of each character, and once to find the first unique character.

**Space Complexity**
O(n), where n is the length of the string. This is because we are storing the frequency of each character in the hash table, which requires O(n) space.

**Key Insight**
The key insight here is that we can use a single pass through the string to count the frequency of each character, and then use another pass to find the first unique character. This approach avoids the need for multiple passes through the string, making it efficient for large inputs.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 27 ms (Beats 98.73%) |
| 💾 Memory | 18.1 MB (Beats 100%) |
| 📅 Solved | 2025-02-06 |
| 💻 Language | Python |