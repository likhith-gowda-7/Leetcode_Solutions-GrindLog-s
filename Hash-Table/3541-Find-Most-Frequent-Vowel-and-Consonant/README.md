# 3541. Find Most Frequent Vowel and Consonant


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/)


## 📝 Problem Description

You are given a string `s` consisting of lowercase English letters (`'a'` to `'z'`). 

Your task is to:

	- Find the vowel (one of `'a'`, `'e'`, `'i'`, `'o'`, or `'u'`) with the **maximum** frequency.

	- Find the consonant (all other letters excluding vowels) with the **maximum** frequency.

Return the sum of the two frequencies.

**Note**: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

The **frequency** of a letter `x` is the number of times it occurs in the string.
 

Example 1:**

**Input:** s = "successes"

**Output:** 6

**Explanation:**

	- The vowels are: `'u'` (frequency 1), `'e'` (frequency 2). The maximum frequency is 2.

	- The consonants are: `'s'` (frequency 4), `'c'` (frequency 2). The maximum frequency is 4.

	- The output is `2 + 4 = 6`.

Example 2:**

**Input:** s = "aeiaeia"

**Output:** 3

**Explanation:**

	- The vowels are: `'a'` (frequency 3), `'e'` ( frequency 2), `'i'` (frequency 2). The maximum frequency is 3.

	- There are no consonants in `s`. Hence, maximum consonant frequency = 0.

	- The output is `3 + 0 = 3`.

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists of lowercase English letters only.

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating over the input string and maintaining a count of the maximum frequency of vowels and consonants separately. It uses a dictionary to store the frequency of each letter and updates the maximum frequency of vowels and consonants accordingly.

**Approach**
1. Initialize a set of vowels and a dictionary to store the frequency of each letter.
2. Initialize variables to store the maximum frequency of vowels and consonants.
3. Iterate over each character in the input string.
4. For each character, increment its frequency in the dictionary and update the maximum frequency of vowels and consonants if necessary.
5. Return the sum of the maximum frequency of vowels and consonants.

**Time Complexity**
O(n), where n is the length of the input string. This is because we are iterating over the string once.

**Space Complexity**
O(n), where n is the length of the input string. This is because in the worst case, we are storing the frequency of each character in the dictionary.

**Key Insight**
The key insight is to use a dictionary to store the frequency of each letter, which allows us to update the maximum frequency of vowels and consonants efficiently. This approach avoids the need to sort the letters or use a separate data structure to store the maximum frequency, making it more efficient and scalable.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 5 ms (Beats 14.85%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-09-13 |
| 💻 Language | Python |