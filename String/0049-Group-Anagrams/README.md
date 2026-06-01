> 📌 **Cross-listed:** Primary location is [Array/0049-Group-Anagrams](../../Array/0049-Group-Anagrams). This problem also appears under: **Array**, **Hash Table**, **String**, **Sorting**

# 49. Group Anagrams


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/group-anagrams/)


## 📝 Problem Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

 

Example 1:**

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Explanation:**

	- There is no string in strs that can be rearranged to form `"bat"`.

	- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.

	- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

Example 2:**

**Input:** strs = [""]

**Output:** [[""]]

Example 3:**

**Input:** strs = ["a"]

**Output:** [["a"]]

 

**Constraints:**

	- `1 <= strs.length <= 10^4`

	- `0 <= strs[i].length <= 100`

	- `strs[i]` consists of lowercase English letters.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 10 ms (Beats 87.72%) |
| 💾 Memory | 20.6 MB (Beats 99.99%) |
| 📅 Solved | 2025-02-02 |
| 💻 Language | Python |