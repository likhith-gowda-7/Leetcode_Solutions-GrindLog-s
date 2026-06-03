# 1790. Check if One String Swap Can Make Strings Equal


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/)


## 📝 Problem Description

You are given two strings `s1` and `s2` of equal length. A **string swap** is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return `true` *if it is possible to make both strings equal by performing **at most one string swap **on **exactly one** of the strings. *Otherwise, return `false`.

 

Example 1:**

```

**Input:** s1 = "bank", s2 = "kanb"
**Output:** true
**Explanation:** For example, swap the first character with the last character of s2 to make "bank".

```

Example 2:**

```

**Input:** s1 = "attack", s2 = "defend"
**Output:** false
**Explanation:** It is impossible to make them equal with one string swap.

```

Example 3:**

```

**Input:** s1 = "kelb", s2 = "kelb"
**Output:** true
**Explanation:** The two strings are already equal, so no string swap operation is required.

```

 

**Constraints:**

	- `1 <= s1.length, s2.length <= 100`

	- `s1.length == s2.length`

	- `s1` and `s2` consist of only lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The problem asks us to determine if we can make two strings equal by performing at most one string swap on exactly one of the strings. We can approach this by counting the frequency of each character in both strings and then checking if there's a mismatch that can be resolved with a single swap.

**Approach**
1. Count the frequency of each character in the first string using a hash table (in this case, `Counter` from the `collections` module).
2. If the two strings are already equal, return `True`.
3. Iterate through the second string. For each character:
   1. Check if it's present in the hash table and if its count is greater than 0.
   2. If the characters at the current position in both strings are different, increment a counter.
   3. Decrement the count of the character in the hash table.
   4. If the character is not present in the hash table or its count is 0, return `False`.
4. After iterating through the second string, check if the counter is equal to 2. If it's not, return `False`.
5. If all checks pass, return `True`.

**Time Complexity**
O(n), where n is the length of the strings. We iterate through each character in the strings once.

**Space Complexity**
O(1), excluding the space needed for the input strings. We use a hash table to store the frequency of each character, which has a constant maximum size.

**Key Insight**
The key insight is that we only need to count the frequency of each character once and then check if there's a mismatch that can be resolved with a single swap. This approach allows us to solve the problem in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-02-05 |
| 💻 Language | Python |