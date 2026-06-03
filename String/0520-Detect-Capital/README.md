# 520. Detect Capital


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/detect-capital/)


## 📝 Problem Description

We define the usage of capitals in a word to be right when one of the following cases holds:

	- All letters in this word are capitals, like `"USA"`.

	- All letters in this word are not capitals, like `"leetcode"`.

	- Only the first letter in this word is capital, like `"Google"`.

Given a string `word`, return `true` if the usage of capitals in it is right.

 

Example 1:**

```
**Input:** word = "USA"
**Output:** true

```
Example 2:**

```
**Input:** word = "FlaG"
**Output:** false

```

 

**Constraints:**

	- `1 <= word.length <= 100`

	- `word` consists of lowercase and uppercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution works by counting the number of uppercase and lowercase letters in the input string. It then checks if the usage of capitals is right based on the counts and the first letter of the string.

**Approach**
1. Initialize two counters, `upper_count` and `lower_count`, to keep track of the number of uppercase and lowercase letters in the string.
2. Iterate through each character `w` in the string.
3. Check if the character is lowercase (ASCII value greater than 96) and increment `lower_count` accordingly.
4. Otherwise, increment `upper_count`.
5. After iterating through the entire string, check the conditions:
   - If all characters are uppercase (`upper_count == n`), return `True`.
   - If all characters are lowercase (`lower_count == n`), return `True`.
   - If the first character is uppercase and the rest are lowercase (`word[0] == word[0].upper() and lower_count == n - 1`), return `True`.

**Time Complexity**
O(n), where n is the length of the input string, because we iterate through each character once.

**Space Complexity**
O(1), because we only use a constant amount of space to store the counters and do not use any data structures that scale with the input size.

**Key Insight**
The key insight is that we can determine the usage of capitals in the string by simply counting the number of uppercase and lowercase letters. This approach is efficient because it avoids the need to iterate through the string multiple times or use complex string manipulation.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 23.19%) |
| 📅 Solved | 2026-05-26 |
| 💻 Language | Python |