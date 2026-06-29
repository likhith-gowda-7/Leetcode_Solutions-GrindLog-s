# 1048. Longest String Chain


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-string-chain/)


## 📝 Problem Description

You are given an array of `words` where each word consists of lowercase English letters.

`word_A` is a **predecessor** of `word_B` if and only if we can insert **exactly one** letter anywhere in `word_A` **without changing the order of the other characters** to make it equal to `word_B`.

	- For example, `"abc"` is a **predecessor** of `"abac"`, while `"cba"` is not a **predecessor** of `"bcad"`.

A **word chain*** *is a sequence of words `[word_1, word_2, ..., word_k]` with `k >= 1`, where `word_1` is a **predecessor** of `word_2`, `word_2` is a **predecessor** of `word_3`, and so on. A single word is trivially a **word chain** with `k == 1`.

Return *the **length** of the **longest possible word chain** with words chosen from the given list of *`words`.

 

Example 1:**

```

**Input:** words = ["a","b","ba","bca","bda","bdca"]
**Output:** 4
**Explanation**: One of the longest word chains is ["a","ba","bda","bdca"].

```

Example 2:**

```

**Input:** words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
**Output:** 5
**Explanation:** All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

```

Example 3:**

```

**Input:** words = ["abcd","dbqca"]
**Output:** 1
**Explanation:** The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

```

 

**Constraints:**

	- `1 <= words.length <= 1000`

	- `1 <= words[i].length <= 16`

	- `words[i]` only consists of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
This solution uses dynamic programming to find the longest possible word chain. The key insight is that we can extend a word chain by finding a predecessor of the current word. We sort the words by their lengths and use a dynamic programming table to keep track of the maximum length of the word chain ending at each word.

**Approach**
1. Define a helper function `check(s1, s2)` to check if `s1` is a predecessor of `s2`. This function returns `True` if `s1` can be extended to `s2` by inserting exactly one character.
2. Sort the input words by their lengths in ascending order.
3. Initialize a dynamic programming table `dp` of size `n`, where `n` is the number of words. Set all elements of `dp` to 1, since a single word is a trivial word chain of length 1.
4. Iterate over the sorted words. For each word `words[i]`, iterate over its predecessors `words[prev]`. If `words[i]` is a predecessor of `words[prev]` and the length of the word chain ending at `words[prev]` plus 1 is greater than the current length of the word chain ending at `words[i]`, update `dp[i]` to the maximum of its current value and the length of the word chain ending at `words[prev]` plus 1.
5. Keep track of the maximum length of the word chain seen so far and return it at the end.

**Time Complexity**
O(n^2 * m), where n is the number of words and m is the maximum length of a word. The `check` function has a time complexity of O(m), and we call it for each pair of words, resulting in a total time complexity of O(n^2 * m).

**Space Complexity**
O(n), where n is the number of words. We use a dynamic programming table of size n to keep track of the maximum length of the word chain ending at each word.

**Key Insight**
The key insight is that we can extend a word chain by finding a predecessor of the current word. By sorting the words by their lengths and using a dynamic programming table, we can efficiently find the longest possible word chain.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 757 ms (Beats 25.17%) |
| 💾 Memory | 19.4 MB (Beats 70.2%) |
| 📅 Solved | 2026-06-28 |
| 💻 Language | Python |