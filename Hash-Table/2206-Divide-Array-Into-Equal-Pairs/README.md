> 📌 **Cross-listed:** Primary location is [Array/2206-Divide-Array-Into-Equal-Pairs](../../Array/2206-Divide-Array-Into-Equal-Pairs). This problem also appears under: **Array**, **Hash Table**, **Bit Manipulation**, **Counting**

# 2206. Divide Array Into Equal Pairs


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/divide-array-into-equal-pairs/)


## 📝 Problem Description

You are given an integer array `nums` consisting of `2 * n` integers.

You need to divide `nums` into `n` pairs such that:

	- Each element belongs to **exactly one** pair.

	- The elements present in a pair are **equal**.

Return `true` *if nums can be divided into* `n` *pairs, otherwise return* `false`.

 

Example 1:**

```

**Input:** nums = [3,2,3,2,2,2]
**Output:** true
**Explanation:** 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

```

Example 2:**

```

**Input:** nums = [1,2,3,4]
**Output:** false
**Explanation:** 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.

```

 

**Constraints:**

	- `nums.length == 2 * n`

	- `1 <= n <= 500`

	- `1 <= nums[i] <= 500`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2 ms (Beats 79.57%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-03-17 |
| 💻 Language | Python |