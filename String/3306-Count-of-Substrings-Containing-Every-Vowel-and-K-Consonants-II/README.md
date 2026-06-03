> 📌 **Cross-listed:** Primary location is [Hash Table/3306-Count-of-Substrings-Containing-Every-Vowel-and-K-Consonants-II](../../Hash-Table/3306-Count-of-Substrings-Containing-Every-Vowel-and-K-Consonants-II). This problem also appears under: **Hash Table**, **String**, **Sliding Window**

# 3306. Count of Substrings Containing Every Vowel and K Consonants II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/)


## 📝 Problem Description

You are given a string `word` and a **non-negative** integer `k`.

Return the total number of substrings of `word` that contain every vowel (`'a'`, `'e'`, `'i'`, `'o'`, and `'u'`) **at least** once and **exactly** `k` consonants.

 

Example 1:**

**Input:** word = "aeioqq", k = 1

**Output:** 0

**Explanation:**

There is no substring with every vowel.

Example 2:**

**Input:** word = "aeiou", k = 0

**Output:** 1

**Explanation:**

The only substring with every vowel and zero consonants is `word[0..4]`, which is `"aeiou"`.

Example 3:**

**Input:** word = "ieaouqqieaouqq", k = 1

**Output:** 3

**Explanation:**

The substrings with every vowel and one consonant are:

	- `word[0..5]`, which is `"ieaouq"`.

	- `word[6..11]`, which is `"qieaou"`.

	- `word[7..12]`, which is `"ieaouq"`.

 

**Constraints:**

	- `5 <= word.length <= 2 * 10^5`

	- `word` consists only of lowercase English letters.

	- `0 <= k <= word.length - 5`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach to count the number of substrings that contain every vowel at least once and exactly k consonants. It maintains a count of vowels and consonants within the current window and expands the window to the right until it contains all vowels and at least k consonants. The solution then subtracts the count of substrings with k+1 consonants to exclude those that contain all vowels and more than k consonants.

**Approach**
1. Define a helper function `atleastk(k)` that takes an integer `k` as input and returns the count of substrings with at least k consonants.
2. Initialize a dictionary `count` to store the count of vowels, a variable `non_vowels` to store the count of consonants, and a variable `res` to store the count of substrings.
3. Iterate over the string `word` from left to right using a sliding window approach. For each character:
   - If the character is a vowel, increment its count in the `count` dictionary.
   - If the character is a consonant, increment `non_vowels`.
4. When the window contains all vowels and at least k consonants, increment `res` by the length of the remaining string.
5. Shrink the window from the left by removing the leftmost character:
   - If the removed character is a vowel, decrement its count in the `count` dictionary.
   - If the removed character is a consonant, decrement `non_vowels`.
   - If the count of the removed vowel becomes zero, remove it from the `count` dictionary.
6. Return the count of substrings with at least k consonants.
7. Call the `atleastk(k)` function and subtract the result of `atleastk(k+1)` to exclude substrings with k+1 consonants.

**Time Complexity**
O(n * m), where n is the length of the string and m is the maximum number of vowels in the string. The reason is that in the worst case, we need to iterate over the string n times and maintain a dictionary of size m.

**Space Complexity**
O(m), where m is the maximum number of vowels in the string. The reason is that we need to store the count of vowels in a dictionary.

**Key Insight**
The key insight is to use a sliding window approach to efficiently count the number of substrings that contain every vowel at least once and exactly k consonants. By maintaining a count of vowels and consonants within the current window, we can quickly expand and shrink the window to find all possible substrings.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3030 ms (Beats 42.86%) |
| 💾 Memory | 20.3 MB (Beats 21.43%) |
| 📅 Solved | 2025-03-10 |
| 💻 Language | Python |