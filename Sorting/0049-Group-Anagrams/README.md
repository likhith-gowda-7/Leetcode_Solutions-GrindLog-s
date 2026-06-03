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

## 🧠 Solution Explanation

## Intuition
The approach works by using a hash table to group anagrams together, where the key is the sorted version of each string. This is because anagrams are strings that contain the same characters, just in a different order, and sorting them will result in the same string. By using the sorted string as the key, we can efficiently group all anagrams together.

## Approach
1. Initialize a hash table (`res`) to store the anagrams, where each key is a sorted string and the value is a list of anagrams.
2. Iterate over each string (`i`) in the input array (`strs`).
3. For each string, sort its characters and join them into a new string (`curr`).
4. Use the sorted string (`curr`) as the key to append the original string (`i`) to the corresponding list in the hash table (`res`).
5. Finally, return the values of the hash table as a list of lists, where each inner list contains the anagrams.

## Time Complexity
The time complexity is O(NMlogM), where N is the number of strings and M is the maximum length of a string. This is because we are sorting each string, which takes O(MlogM) time, and we are doing this for N strings.

## Space Complexity
The space complexity is O(NM), where N is the number of strings and M is the maximum length of a string. This is because we are storing all the characters of the input strings in the hash table.

## Key Insight
The key insight is to use the sorted version of each string as the key in the hash table, which allows us to efficiently group all anagrams together. This is because sorting the characters of a string provides a unique identifier for all anagrams of that string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 10 ms (Beats 87.72%) |
| 💾 Memory | 20.6 MB (Beats 99.99%) |
| 📅 Solved | 2025-02-02 |
| 💻 Language | Python |