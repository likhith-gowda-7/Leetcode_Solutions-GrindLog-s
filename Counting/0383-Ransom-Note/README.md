> 📌 **Cross-listed:** Primary location is [Hash Table/0383-Ransom-Note](../../Hash-Table/0383-Ransom-Note). This problem also appears under: **Hash Table**, **String**, **Counting**

# 383. Ransom Note


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/ransom-note/)


## 📝 Problem Description

Given two strings `ransomNote` and `magazine`, return `true`* if *`ransomNote`* can be constructed by using the letters from *`magazine`* and *`false`* otherwise*.

Each letter in `magazine` can only be used once in `ransomNote`.

 

Example 1:**

```
**Input:** ransomNote = "a", magazine = "b"
**Output:** false

```
Example 2:**

```
**Input:** ransomNote = "aa", magazine = "ab"
**Output:** false

```
Example 3:**

```
**Input:** ransomNote = "aa", magazine = "aab"
**Output:** true

```

 

**Constraints:**

	- `1 <= ransomNote.length, magazine.length <= 10^5`

	- `ransomNote` and `magazine` consist of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to count the frequency of each character in the `magazine` string. Then, it iterates through the `ransomNote` string, decrementing the count of each character in the hash table if it exists. If the count of a character becomes zero, it means the character has been used up and cannot be used again. The function returns `True` if all characters in `ransomNote` can be constructed from `magazine` and `False` otherwise.

**Approach**
1. Create a hash table `h` to store the frequency of each character in the `magazine` string.
2. Iterate through the `magazine` string, incrementing the count of each character in the hash table.
3. Initialize a counter `j` to keep track of the number of characters in `ransomNote` that have been constructed.
4. Iterate through the `ransomNote` string. For each character:
   - Check if the character exists in the hash table.
   - If it exists, decrement its count in the hash table.
   - If the count becomes zero, return `False` because the character cannot be used again.
   - Increment the counter `j` to indicate that the character has been constructed.
5. After iterating through all characters in `ransomNote`, return `True` if the counter `j` is equal to the length of `ransomNote`, indicating that all characters can be constructed.

**Time Complexity**
O(n + m), where n is the length of `ransomNote` and m is the length of `magazine`. This is because we iterate through both strings once.

**Space Complexity**
O(m), where m is the length of `magazine`. This is because we use a hash table to store the frequency of each character in `magazine`.

**Key Insight**
The key insight is to use a hash table to count the frequency of each character in `magazine`, allowing us to efficiently check if a character can be used to construct a character in `ransomNote`. This approach ensures that we can handle large inputs efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 19 ms (Beats 61.77%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-01-17 |
| 💻 Language | Python |