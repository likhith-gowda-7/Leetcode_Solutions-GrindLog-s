> 📌 **Cross-listed:** Primary location is [Math/3307-Find-the-K-th-Character-in-String-Game-II](../../Math/3307-Find-the-K-th-Character-in-String-Game-II). This problem also appears under: **Math**, **Bit Manipulation**, **Recursion**

# 3307. Find the K-th Character in String Game II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Recursion](https://img.shields.io/badge/Recursion-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/)


## 📝 Problem Description

Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

You are given a **positive** integer `k`. You are also given an integer array `operations`, where `operations[i]` represents the **type** of the `i^th` operation.

Now Bob will ask Alice to perform **all** operations in sequence:

	- If `operations[i] == 0`, **append** a copy of `word` to itself.

	- If `operations[i] == 1`, generate a new string by **changing** each character in `word` to its **next** character in the English alphabet, and **append** it to the *original* `word`. For example, performing the operation on `"c"` generates `"cd"` and performing the operation on `"zb"` generates `"zbac"`.

Return the value of the `k^th` character in `word` after performing all the operations.

**Note** that the character `'z'` can be changed to `'a'` in the second type of operation.

 

Example 1:**

**Input:** k = 5, operations = [0,0,0]

**Output:** "a"

**Explanation:**

Initially, `word == "a"`. Alice performs the three operations as follows:

	- Appends `"a"` to `"a"`, `word` becomes `"aa"`.

	- Appends `"aa"` to `"aa"`, `word` becomes `"aaaa"`.

	- Appends `"aaaa"` to `"aaaa"`, `word` becomes `"aaaaaaaa"`.

Example 2:**

**Input:** k = 10, operations = [0,1,0,1]

**Output:** "b"

**Explanation:**

Initially, `word == "a"`. Alice performs the four operations as follows:

	- Appends `"a"` to `"a"`, `word` becomes `"aa"`.

	- Appends `"bb"` to `"aa"`, `word` becomes `"aabb"`.

	- Appends `"aabb"` to `"aabb"`, `word` becomes `"aabbaabb"`.

	- Appends `"bbccbbcc"` to `"aabbaabb"`, `word` becomes `"aabbaabbbbccbbcc"`.

 

**Constraints:**

	- `1 <= k <= 10^14`

	- `1 <= operations.length <= 100`

	- `operations[i]` is either 0 or 1.

	- The input is generated such that `word` has **at least** `k` characters after all operations.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-07-04 |
| 💻 Language | Python |