# 3136. Valid Word


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/valid-word/)


## 📝 Problem Description

A word is considered **valid** if:

	- It contains a **minimum** of 3 characters.

	- It contains only digits (0-9), and English letters (uppercase and lowercase).

	- It includes **at least** one **vowel**.

	- It includes **at least** one **consonant**.

You are given a string `word`.

Return `true` if `word` is valid, otherwise, return `false`.

**Notes:**

	- `'a'`, `'e'`, `'i'`, `'o'`, `'u'`, and their uppercases are **vowels**.

	- A **consonant** is an English letter that is not a vowel.

 

Example 1:**

**Input:** word = "234Adas"

**Output:** true

**Explanation:**

This word satisfies the conditions.

Example 2:**

**Input:** word = "b3"

**Output:** false

**Explanation:**

The length of this word is fewer than 3, and does not have a vowel.

Example 3:**

**Input:** word = "a3$e"

**Output:** false

**Explanation:**

This word contains a `'$'` character and does not have a consonant.

 

**Constraints:**

	- `1 <= word.length <= 20`

	- `word` consists of English uppercase and lowercase letters, digits, `'@'`, `'#'`, and `'$'`.

## 🧠 Solution Explanation

**Intuition**
The solution checks if a given word is valid by verifying its length, character set, and presence of vowels and consonants. It iterates through each character in the word, tracking the count of vowels, consonants, and digits. The solution returns `True` if the word meets all conditions and `False` otherwise.

**Approach**
1. Check if the word's length is less than 3 or if it contains non-alphanumeric characters. If either condition is true, return `False`.
2. Initialize sets for vowels and consonants.
3. Initialize counters for vowels (`v`), consonants (`conso`), and digits (`d`).
4. Iterate through each character in the word:
   1. If the character is a letter, check if it's a vowel. If it is, increment the vowel counter (`v`).
   2. If the character is not a vowel, increment the consonant counter (`conso`).
   3. If the character is a digit, increment the digit counter (`d`).
5. Return `True` if the word has at least one consonant and one vowel, and `False` otherwise.

**Time Complexity**
O(n), where n is the length of the word. This is because the solution iterates through each character in the word once.

**Space Complexity**
O(1), as the solution uses a constant amount of space to store the counters and sets, regardless of the input size.

**Key Insight**
The key insight is that the solution can be optimized by tracking the presence of vowels and consonants separately, rather than checking for each condition individually. This allows for a more efficient solution with a time complexity of O(n).

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-07-15 |
| 💻 Language | Python |