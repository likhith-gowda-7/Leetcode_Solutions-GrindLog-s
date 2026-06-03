# 2840. Check if Strings Can be Made Equal With Operations II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![String](https://img.shields.io/badge/String-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/)


## 📝 Problem Description

You are given two strings `s1` and `s2`, both of length `n`, consisting of **lowercase** English letters.

You can apply the following operation on **any** of the two strings **any** number of times:

	- Choose any two indices `i` and `j` such that `i < j` and the difference `j - i` is **even**, then **swap** the two characters at those indices in the string.

Return `true`* if you can make the strings *`s1`* and *`s2`* equal, and *`false`* otherwise*.

 

Example 1:**

```

**Input:** s1 = "abcdba", s2 = "cabdab"
**Output:** true
**Explanation:** We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.

```

Example 2:**

```

**Input:** s1 = "abe", s2 = "bea"
**Output:** false
**Explanation:** It is not possible to make the two strings equal.

```

 

**Constraints:**

	- `n == s1.length == s2.length`

	- `1 <= n <= 10^5`

	- `s1` and `s2` consist only of lowercase English letters.

## 🧠 Solution Explanation

**Intuition**
The solution works by observing that the given operation can only swap characters at even or odd indices, effectively "grouping" characters into two sets: one for even indices and one for odd indices. If the two strings can be made equal, the counts of characters at even and odd indices must be equal in both strings.

**Approach**
1. Create two counters, `even` and `odd`, to store the counts of characters at even and odd indices in the first string `s1`.
2. Create two counters, `even` and `odd`, to store the counts of characters at even and odd indices in the second string `s2`.
3. Compare the counts of characters at even indices in `s1` and `s2` using the `==` operator.
4. Compare the counts of characters at odd indices in `s1` and `s2` using the `==` operator.
5. Return `True` if both comparisons are `True`, and `False` otherwise.

**Time Complexity**
O(n) - The solution iterates over the strings `s1` and `s2` once to count the characters at even and odd indices.

**Space Complexity**
O(n) - The solution uses two counters to store the counts of characters at even and odd indices, which requires O(n) space in the worst case.

**Key Insight**
The key insight is that the given operation can only swap characters at even or odd indices, effectively "grouping" characters into two sets. By comparing the counts of characters at even and odd indices in both strings, we can determine if the strings can be made equal. This insight allows us to simplify the problem and solve it efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 51 ms (Beats 85.37%) |
| 💾 Memory | 20.1 MB (Beats 72.78%) |
| 📅 Solved | 2026-03-31 |
| 💻 Language | Python |