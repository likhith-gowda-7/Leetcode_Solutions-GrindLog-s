> 📌 **Cross-listed:** Primary location is [Hash Table/3121-Count-the-Number-of-Special-Characters-II](../../Hash-Table/3121-Count-the-Number-of-Special-Characters-II). This problem also appears under: **Hash Table**, **String**

# 3121. Count the Number of Special Characters II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-the-number-of-special-characters-ii/)


## 📝 Problem Description

You are given a string `word`. A letter `c` is called **special** if it appears **both** in lowercase and uppercase in `word`, and **every** lowercase occurrence of `c` appears before the **first** uppercase occurrence of `c`.

Return the number of* ***special** letters* *in* *`word`.

 

Example 1:**

**Input:** word = "aaAbcBC"

**Output:** 3

**Explanation:**

The special characters are `'a'`, `'b'`, and `'c'`.

Example 2:**

**Input:** word = "abc"

**Output:** 0

**Explanation:**

There are no special characters in `word`.

Example 3:**

**Input:** word = "AbBCab"

**Output:** 0

**Explanation:**

There are no special characters in `word`.

 

**Constraints:**

	- `1 <= word.length <= 2 * 10^5`

	- `word` consists of only lowercase and uppercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining a hash table of characters and their first occurrence indices. It then iterates through the hash table to count the number of special characters, which are uppercase letters that appear after all their lowercase occurrences.

**Approach**
1. Initialize an empty hash table `char_count` to store characters and their first occurrence indices.
2. Iterate through the input string `word`. For each character:
   - If the character is lowercase or not in the hash table, add it to the hash table with its index.
3. Iterate through the hash table. For each key (character):
   - If the key is uppercase and its lowercase version is in the hash table:
     - Get the last occurrence index of the lowercase version and the first occurrence index of the uppercase version.
     - If the first occurrence index is greater than the last occurrence index, increment the special character count.

**Time Complexity**
O(n), where n is the length of the input string. This is because we make two passes through the string: one to populate the hash table and another to count special characters.

**Space Complexity**
O(n), where n is the length of the input string. This is because in the worst case, we need to store all characters in the hash table.

**Key Insight**
The key insight is to recognize that a character is special if its uppercase version appears after all its lowercase occurrences. By maintaining a hash table of characters and their first occurrence indices, we can efficiently identify and count special characters.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 201 ms (Beats 82.23%) |
| 💾 Memory | 21.7 MB (Beats 22.55%) |
| 📅 Solved | 2026-05-27 |
| 💻 Language | Python |