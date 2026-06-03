# 278. First Bad Version


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Interactive](https://img.shields.io/badge/Interactive-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/first-bad-version/)


## 📝 Problem Description

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:**

```

**Input:** n = 5, bad = 4
**Output:** 4
**Explanation:**
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

```

Example 2:**

```

**Input:** n = 1, bad = 1
**Output:** 1

```

 

**Constraints:**

	- `1 <= bad <= n <= 2^31 - 1`

## 🧠 Solution Explanation

**Intuition**
This solution uses a binary search approach to find the first bad version. The idea is to repeatedly divide the search space in half until we find the first bad version. This approach works because the versions are ordered, and each bad version causes all subsequent versions to be bad.

**Approach**
1. Initialize two pointers, `l` and `r`, to the start and end of the version range, respectively.
2. While `l` is less than or equal to `r`, calculate the midpoint `mid` of the current search range.
3. Call the `isBadVersion` API to check if the version at `mid` is bad. If it is, update `r` to `mid - 1` to search in the left half of the range. If it's not, update `l` to `mid + 1` to search in the right half of the range.
4. Repeat steps 2-3 until `l` is greater than `r`.
5. The first bad version is the one at index `l`.

**Time Complexity**
O(log n), where n is the number of versions. This is because we divide the search space in half at each step, resulting in a logarithmic number of iterations.

**Space Complexity**
O(1), as we only use a constant amount of space to store the pointers `l` and `r`.

**Key Insight**
The key insight here is that we can use binary search to find the first bad version in logarithmic time, even though we don't have direct access to the version numbers. This is possible because we can use the `isBadVersion` API to determine whether a version is bad or not, and then adjust our search range accordingly.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 28 ms (Beats 99.57%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-21 |
| 💻 Language | Python |