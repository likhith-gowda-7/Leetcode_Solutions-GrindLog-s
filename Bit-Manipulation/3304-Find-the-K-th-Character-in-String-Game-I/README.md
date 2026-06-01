> 📌 **Cross-listed:** Primary location is [Math/3304-Find-the-K-th-Character-in-String-Game-I](../../Math/3304-Find-the-K-th-Character-in-String-Game-I). This problem also appears under: **Math**, **Bit Manipulation**, **Recursion**, **Simulation**

# 3304. Find the K-th Character in String Game I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/)


## 📝 Problem Description

Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

You are given a **positive** integer `k`.

Now Bob will ask Alice to perform the following operation **forever**:

	- Generate a new string by **changing** each character in `word` to its **next** character in the English alphabet, and **append** it to the *original* `word`.

For example, performing the operation on `"c"` generates `"cd"` and performing the operation on `"zb"` generates `"zbac"`.

Return the value of the `k^th` character in `word`, after enough operations have been done for `word` to have **at least** `k` characters.

 

Example 1:**

**Input:** k = 5

**Output:** "b"

**Explanation:**

Initially, `word = "a"`. We need to do the operation three times:

	- Generated string is `"b"`, `word` becomes `"ab"`.

	- Generated string is `"bc"`, `word` becomes `"abbc"`.

	- Generated string is `"bccd"`, `word` becomes `"abbcbccd"`.

Example 2:**

**Input:** k = 10

**Output:** "c"

 

**Constraints:**

	- `1 <= k <= 500`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-07-03 |
| 💻 Language | Python |