> 📌 **Cross-listed:** Primary location is [Hash Table/3120-Count-the-Number-of-Special-Characters-I](../../Hash-Table/3120-Count-the-Number-of-Special-Characters-I). This problem also appears under: **Hash Table**, **String**

# 3120. Count the Number of Special Characters I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-the-number-of-special-characters-i/)


## 📝 Problem Description

You are given a string `word`. A letter is called **special** if it appears **both** in lowercase and uppercase in `word`.

Return the number of* ***special** letters in* *`word`.

 

Example 1:**

**Input:** word = "aaAbcBC"

**Output:** 3

**Explanation:**

The special characters in `word` are `'a'`, `'b'`, and `'c'`.

Example 2:**

**Input:** word = "abc"

**Output:** 0

**Explanation:**

No character in `word` appears in uppercase.

Example 3:**

**Input:** word = "abBCab"

**Output:** 1

**Explanation:**

The only special character in `word` is `'b'`.

 

**Constraints:**

	- `1 <= word.length <= 50`

	- `word` consists of only lowercase and uppercase English letters.

## 🧠 Solution Explanation

**Intuition**
The problem requires counting the number of special characters in a given string, where a special character appears both in lowercase and uppercase. This can be achieved by creating a hash table to store the frequency of each character and then iterating through the hash table to count the special characters.

**Approach**
1. Create a hash table `h1` to store the frequency of each character in the string `word` using the `Counter` class from the `collections` module.
2. Initialize a variable `count` to store the number of special characters.
3. Iterate through the keys of the hash table `h1`.
4. For each key, check if the character is uppercase and its lowercase version is also present in the hash table, or if the character is lowercase and its uppercase version is present in the hash table. If either condition is true, increment the `count` variable.
5. Return the `count` variable divided by 2, as each special character is counted twice.

**Time Complexity**
O(n), where n is the length of the string `word`. This is because we are iterating through the string once to create the hash table and then iterating through the hash table once to count the special characters.

**Space Complexity**
O(n), where n is the length of the string `word`. This is because we are storing the frequency of each character in the hash table, which requires O(n) space.

**Key Insight**
The key insight is to use a hash table to efficiently store and count the frequency of each character, and then iterate through the hash table to count the special characters. This approach allows us to solve the problem in linear time and space complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 57.52%) |
| 📅 Solved | 2026-05-26 |
| 💻 Language | Python |