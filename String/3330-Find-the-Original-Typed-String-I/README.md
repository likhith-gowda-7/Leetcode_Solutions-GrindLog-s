# 3330. Find the Original Typed String I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-original-typed-string-i/)


## 📝 Problem Description

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and **may** press a key for too long, resulting in a character being typed **multiple** times.

Although Alice tried to focus on her typing, she is aware that she may still have done this **at most** *once*.

You are given a string `word`, which represents the **final** output displayed on Alice's screen.

Return the total number of *possible* original strings that Alice *might* have intended to type.

 

Example 1:**

**Input:** word = "abbcccc"

**Output:** 5

**Explanation:**

The possible strings are: `"abbcccc"`, `"abbccc"`, `"abbcc"`, `"abbc"`, and `"abcccc"`.

Example 2:**

**Input:** word = "abcd"

**Output:** 1

**Explanation:**

The only possible string is `"abcd"`.

Example 3:**

**Input:** word = "aaaa"

**Output:** 4

 

**Constraints:**

	- `1 <= word.length <= 100`

	- `word` consists only of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution works by treating the entire string as a single typed character and then incrementing the count for each consecutive repeated character. This approach is based on the fact that Alice can press a key at most once, so each repeated character can be considered as a separate typed character.

**Approach**
1. Initialize a counter `res` to 1, representing the case where the entire string is typed intentionally.
2. Iterate through the string from the second character to the end (index 1 to `len(word)`).
3. For each character, check if it is the same as the previous character.
4. If it is the same, increment the counter `res` by 1.
5. Return the final count `res`.

**Time Complexity**
O(n), where n is the length of the string. This is because we are iterating through the string once.

**Space Complexity**
O(1), because we are using a constant amount of space to store the counter `res`.

**Key Insight**
The key insight is that each repeated character can be considered as a separate typed character, allowing us to increment the count for each consecutive repeated character. This approach takes advantage of the fact that Alice can press a key at most once, making it efficient and easy to implement.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 33 ms (Beats 99.3%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-07-01 |
| 💻 Language | Python |