# 2540. Minimum Common Value


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-common-value/)


## 📝 Problem Description

Given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, return *the **minimum integer common** to both arrays*. If there is no common integer amongst `nums1` and `nums2`, return `-1`.

Note that an integer is said to be **common** to `nums1` and `nums2` if both arrays have **at least one** occurrence of that integer.

 

Example 1:**

```

**Input:** nums1 = [1,2,3], nums2 = [2,4]
**Output:** 2
**Explanation:** The smallest element common to both arrays is 2, so we return 2.

```

Example 2:**

```

**Input:** nums1 = [1,2,3,6], nums2 = [2,3,4,5]
**Output:** 2
**Explanation:** There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

```

 

**Constraints:**

	- `1 <= nums1.length, nums2.length <= 10^5`

	- `1 <= nums1[i], nums2[j] <= 10^9`

	- Both `nums1` and `nums2` are sorted in **non-decreasing** order.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 7 ms (Beats 79.87%) |
| 💾 Memory | 37.7 MB (Beats 75.6%) |
| 📅 Solved | 2026-05-19 |
| 💻 Language | Python |