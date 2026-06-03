> 📌 **Cross-listed:** Primary location is [Array/0014-Longest-Common-Prefix](../../Array/0014-Longest-Common-Prefix). This problem also appears under: **Array**, **String**, **Trie**

# 14. Longest Common Prefix


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![String](https://img.shields.io/badge/String-purple) ![Trie](https://img.shields.io/badge/Trie-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-common-prefix/)


## 📝 Problem Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

 

Example 1:**

```

**Input:** strs = ["flower","flow","flight"]
**Output:** "fl"

```

Example 2:**

```

**Input:** strs = ["dog","racecar","car"]
**Output:** ""
**Explanation:** There is no common prefix among the input strings.

```

 

**Constraints:**

	- `1 <= strs.length <= 200`

	- `0 <= strs[i].length <= 200`

	- `strs[i]` consists of only lowercase English letters if it is non-empty.

## 🧠 Solution Explanation

## Intuition
The approach works by initializing the prefix as the first string in the array and then iteratively comparing it with the remaining strings. By gradually reducing the prefix length, we can find the common prefix among all strings. This method takes advantage of the fact that the common prefix must be a prefix of the first string.

## Approach
1. Initialize the prefix as the first string in the array.
2. Iterate over the remaining strings in the array.
3. For each string, compare the prefix with the corresponding substring of the string.
4. If the prefix does not match the substring, reduce the prefix length by one character and repeat the comparison.
5. If the prefix length becomes zero, return an empty string as there is no common prefix.
6. After iterating over all strings, return the prefix as the longest common prefix.

## Time Complexity
The time complexity is O(n * m), where n is the number of strings and m is the maximum length of a string. This is because in the worst case, we need to compare each character of each string with the prefix.

## Space Complexity
The space complexity is O(1), as we only use a constant amount of space to store the prefix and its length, regardless of the input size.

## Key Insight
The key insight is to start with the first string as the prefix and iteratively refine it by comparing with the remaining strings, rather than trying to find the common prefix from scratch. This approach allows us to efficiently find the longest common prefix by leveraging the fact that the common prefix must be a prefix of the first string.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-06-18 |
| 💻 Language | Python |