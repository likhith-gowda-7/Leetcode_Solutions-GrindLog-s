# 3170. Lexicographically Minimum String After Removing Stars


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/)


## 📝 Problem Description

You are given a string `s`. It may contain any number of `'*'` characters. Your task is to remove all `'*'` characters.

While there is a `'*'`, do the following operation:

	- Delete the leftmost `'*'` and the **smallest** non-`'*'` character to its *left*. If there are several smallest characters, you can delete any of them.

Return the lexicographically smallest resulting string after removing all `'*'` characters.

 

Example 1:**

**Input:** s = "aaba*"

**Output:** "aab"

**Explanation:**

We should delete one of the `'a'` characters with `'*'`. If we choose `s[3]`, `s` becomes the lexicographically smallest.

Example 2:**

**Input:** s = "abc"

**Output:** "abc"

**Explanation:**

There is no `'*'` in the string.

 

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists only of lowercase English letters and `'*'`.

	- The input is generated such that it is possible to delete all `'*'` characters.

## 🧠 Solution Explanation

**Intuition**
This solution works by maintaining a hash table (dictionary in Python) to track the positions of each character in the string. When a '*' is encountered, it finds the smallest character in the hash table, removes it from the hash table and the string, and continues. This approach ensures that the resulting string is lexicographically smallest.

**Approach**
1. Initialize an empty hash table `h1` to store the positions of each character in the string.
2. Iterate through the string `s` from left to right.
3. If the current character is not '*', add it to the hash table with its position.
4. If the current character is '*', find the smallest character in the hash table (i.e., the key with the smallest ASCII value).
5. Remove the smallest character from the hash table and the string.
6. Repeat steps 3-5 until the end of the string is reached.
7. Iterate through the hash table and add the characters with their positions to the result string `res`, in lexicographically smallest order.

**Time Complexity**
O(n), where n is the length of the string `s`. This is because we iterate through the string once to populate the hash table, and then iterate through the hash table once to construct the result string.

**Space Complexity**
O(n), where n is the length of the string `s`. This is because in the worst case, we need to store all characters in the hash table.

**Key Insight**
The key insight is to use a hash table to efficiently track the positions of each character in the string, and to remove the smallest character when a '*' is encountered. This approach ensures that the resulting string is lexicographically smallest.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 562 ms (Beats 40.37%) |
| 💾 Memory | 21.7 MB (Beats 99.38%) |
| 📅 Solved | 2025-06-07 |
| 💻 Language | Python |