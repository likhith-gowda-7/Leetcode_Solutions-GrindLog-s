# 500. Keyboard Row


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/keyboard-row/)


## 📝 Problem Description

Given an array of strings `words`, return *the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below*.

**Note** that the strings are **case-insensitive**, both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the **American keyboard**:

	- the first row consists of the characters `"qwertyuiop"`,

	- the second row consists of the characters `"asdfghjkl"`, and

	- the third row consists of the characters `"zxcvbnm"`.

![](https://assets.leetcode.com/uploads/2018/10/12/keyboard.png)
 

Example 1:**

**Input:** words = ["Hello","Alaska","Dad","Peace"]

**Output:** ["Alaska","Dad"]

**Explanation:**

Both `"a"` and `"A"` are in the 2nd row of the American keyboard due to case insensitivity.

Example 2:**

**Input:** words = ["omk"]

**Output:** []

Example 3:**

**Input:** words = ["adsdf","sfd"]

**Output:** ["adsdf","sfd"]

 

**Constraints:**

	- `1 <= words.length <= 20`

	- `1 <= words[i].length <= 100`

	- `words[i]` consists of English letters (both lowercase and uppercase).

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating over each word in the input list and checking if it can be typed on a single row of the American keyboard. We achieve this by converting each word to lowercase and checking if all its characters are present in one of the keyboard rows.

**Approach**
1. Create a set of keyboard rows for easy lookup.
2. Initialize an empty list to store the result.
3. Iterate over each word in the input list.
4. Convert the word to lowercase for case-insensitive comparison.
5. Iterate over each keyboard row.
6. Check if all characters in the word are present in the current keyboard row.
7. If a match is found, add the original word to the result list and break the loop.
8. Return the result list.

**Time Complexity**
O(n * m * k), where n is the number of words, m is the maximum length of a word, and k is the number of keyboard rows. This is because we iterate over each word, then over each character in the word, and finally over each keyboard row.

**Space Complexity**
O(n + k), where n is the number of words and k is the number of keyboard rows. This is because we store the result list and the set of keyboard rows.

**Key Insight**
The key insight is to use a set of keyboard rows for efficient lookup, allowing us to check if a word can be typed on a single row in O(k) time, where k is the number of rows. This optimization is crucial for achieving a reasonable time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-04-09 |
| 💻 Language | Python |