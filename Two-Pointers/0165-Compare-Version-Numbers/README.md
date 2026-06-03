# 165. Compare Version Numbers


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![String](https://img.shields.io/badge/String-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/compare-version-numbers/)


## 📝 Problem Description

Given two **version strings**, `version1` and `version2`, compare them. A version string consists of **revisions** separated by dots `'.'`. The **value of the revision** is its **integer conversion** ignoring leading zeros.

To compare version strings, compare their revision values in **left-to-right order**. If one of the version strings has fewer revisions, treat the missing revision values as `0`.

Return the following:

	- If `version1 < version2`, return -1.

	- If `version1 > version2`, return 1.

	- Otherwise, return 0.

 

Example 1:**

**Input:** version1 = "1.2", version2 = "1.10"

**Output:** -1

**Explanation:**

version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:**

**Input:** version1 = "1.01", version2 = "1.001"

**Output:** 0

**Explanation:**

Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:**

**Input:** version1 = "1.0", version2 = "1.0.0.0"

**Output:** 0

**Explanation:**

version1 has less revisions, which means every missing revision are treated as "0".

 

**Constraints:**

	- `1 <= version1.length, version2.length <= 500`

	- `version1` and `version2` only contain digits and `'.'`.

	- `version1` and `version2` **are valid version numbers**.

	- All the given revisions in `version1` and `version2` can be stored in a **32-bit integer**.

## 🧠 Solution Explanation

**Intuition**
The solution works by splitting the version strings into their constituent revisions, comparing them as integers, and returning the result based on the comparison. This approach leverages the fact that integers can be directly compared, making it efficient for version comparison.

**Approach**
1. Split the input version strings into revisions using the dot (`.`) as a delimiter.
2. Determine the maximum length between the two version strings.
3. Iterate through the revisions, comparing the integer values of each revision.
4. If a revision is missing from one of the version strings, treat its value as 0.
5. Return -1 if the current revision of `version1` is less than the current revision of `version2`.
6. Return 1 if the current revision of `version2` is less than the current revision of `version1`.
7. If all revisions are equal, return 0.

**Time Complexity**
O(max(m, n)), where m and n are the lengths of the input version strings. This is because we iterate through the maximum number of revisions between the two strings.

**Space Complexity**
O(m + n), where m and n are the lengths of the input version strings. This is because we store the split revisions in two separate lists.

**Key Insight**
The key insight is to treat missing revisions as 0, allowing us to directly compare the integer values of each revision. This simplifies the comparison logic and makes the solution efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 28.47%) |
| 📅 Solved | 2026-01-28 |
| 💻 Language | Python |