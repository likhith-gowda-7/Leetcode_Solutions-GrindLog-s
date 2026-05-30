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

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 19 ms (Beats 61.66%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-01-17 |
| 💻 Language | Python |