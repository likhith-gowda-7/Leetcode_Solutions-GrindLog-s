# 884. Uncommon Words from Two Sentences


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/uncommon-words-from-two-sentences/)


## 📝 Problem Description

A **sentence** is a string of single-space separated words where each word consists only of lowercase letters.

A word is **uncommon** if it appears exactly once in one of the sentences, and **does not appear** in the other sentence.

Given two **sentences** `s1` and `s2`, return *a list of all the **uncommon words***. You may return the answer in **any order**.

 

Example 1:**

**Input:** s1 = "this apple is sweet", s2 = "this apple is sour"

**Output:** ["sweet","sour"]

**Explanation:**

The word `"sweet"` appears only in `s1`, while the word `"sour"` appears only in `s2`.

Example 2:**

**Input:** s1 = "apple apple", s2 = "banana"

**Output:** ["banana"]

 

**Constraints:**

	- `1 <= s1.length, s2.length <= 200`

	- `s1` and `s2` consist of lowercase English letters and spaces.

	- `s1` and `s2` do not have leading or trailing spaces.

	- All the words in `s1` and `s2` are separated by a single space.

## 🧠 Solution Explanation

**Intuition**
The solution works by first splitting each sentence into individual words, then counting the occurrences of each word in both sentences using a hash table. Finally, it iterates through the hash table to find words that appear only once in one of the sentences.

**Approach**
1. Initialize an empty hash table `h1` to store word counts.
2. Iterate through the first sentence `s1`:
   - If the current character is not a space, add it to the current word `curr`.
   - If the current character is a space, increment the count of `curr` in `h1` and reset `curr`.
3. After iterating through `s1`, increment the count of the last word `curr` in `h1`.
4. Repeat steps 2-3 for the second sentence `s2`.
5. Iterate through `h1` and append words with a count of 1 to the result list `res`.

**Time Complexity**
O(n + m), where n and m are the lengths of `s1` and `s2`, respectively. This is because we iterate through each character in both sentences once.

**Space Complexity**
O(n + m), where n and m are the lengths of `s1` and `s2`, respectively. This is because we store each word in the hash table, and in the worst case, we store all words from both sentences.

**Key Insight**
The key insight is to use a hash table to efficiently count word occurrences in both sentences. This allows us to find uncommon words in O(n + m) time, making the solution efficient for large input sentences.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-02-06 |
| 💻 Language | Python |