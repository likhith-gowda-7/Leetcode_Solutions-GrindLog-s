# 3302. Find the Lexicographically Smallest Valid Sequence


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/)


## 📝 Problem Description

You are given two strings `word1` and `word2`.

A string `x` is called **almost equal** to `y` if you can change **at most** one character in `x` to make it *identical* to `y`.

A sequence of indices `seq` is called **valid** if:

	- The indices are sorted in **ascending** order.

	- *Concatenating* the characters at these indices in `word1` in **the same** order results in a string that is **almost equal** to `word2`.

Return an array of size `word2.length` representing the lexicographically smallest **valid** sequence of indices. If no such sequence of indices exists, return an **empty** array.

**Note** that the answer must represent the *lexicographically smallest array*, **not** the corresponding string formed by those indices.

 

Example 1:**

**Input:** word1 = "vbcca", word2 = "abc"

**Output:** [0,1,2]

**Explanation:**

The lexicographically smallest valid sequence of indices is `[0, 1, 2]`:

	- Change `word1[0]` to `'a'`.

	- `word1[1]` is already `'b'`.

	- `word1[2]` is already `'c'`.

Example 2:**

**Input:** word1 = "bacdc", word2 = "abc"

**Output:** [1,2,4]

**Explanation:**

The lexicographically smallest valid sequence of indices is `[1, 2, 4]`:

	- `word1[1]` is already `'a'`.

	- Change `word1[2]` to `'b'`.

	- `word1[4]` is already `'c'`.

Example 3:**

**Input:** word1 = "aaaaaa", word2 = "aaabc"

**Output:** []

**Explanation:**

There is no valid sequence of indices.

Example 4:**

**Input:** word1 = "abc", word2 = "ab"

**Output:** [0,1]

 

**Constraints:**

	- `1 <= word2.length < word1.length <= 3 * 10^5`

	- `word1` and `word2` consist only of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pointer approach to find the lexicographically smallest valid sequence of indices. It first constructs a suffix array `last` to store the last occurrence of each character in `word2`. Then, it iterates through `word1` and `word2` to find the valid sequence of indices.

**Approach**
1. Initialize a suffix array `last` of size `m` to store the last occurrence of each character in `word2`.
2. Use two pointers `i` and `j` to iterate through `word1` and `word2` in reverse order. If `word1[i]` matches `word2[j]`, update `last[j]` and decrement `j`.
3. Initialize an empty list `ans` to store the valid sequence of indices.
4. Iterate through `word1` again, and for each character, check if it matches `word2[j]`. If it does, append the index to `ans` and increment `j`.
5. If the current character in `word1` does not match `word2[j]`, check if it can be skipped by checking if `j` is not at the end of `word2` or if the current index is less than the last occurrence of the next character in `word2`. If it can be skipped, append the index to `ans`, set `can_skip` to `False`, and increment `j`.
6. If the end of `word2` is reached, return `ans`. Otherwise, return an empty list.

**Time Complexity**
O(n + m), where n and m are the lengths of `word1` and `word2`, respectively. This is because we iterate through `word1` and `word2` twice, and the suffix array construction takes O(m) time.

**Space Complexity**
O(m), where m is the length of `word2`. This is because we need to store the suffix array `last` of size `m`.

**Key Insight**
The key insight is to use a suffix array to store the last occurrence of each character in `word2`, which allows us to efficiently find the valid sequence of indices by iterating through `word1` and `word2` in reverse order.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 403 ms (Beats 87.23%) |
| 💾 Memory | 47.4 MB (Beats 63.83%) |
| 📅 Solved | 2026-08-08 |
| 💻 Language | Python |