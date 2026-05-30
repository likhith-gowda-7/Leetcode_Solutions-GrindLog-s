# 1394. Find Lucky Integer in an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-lucky-integer-in-an-array/)


## 📝 Problem Description

Given an array of integers `arr`, a **lucky integer** is an integer that has a frequency in the array equal to its value.

Return *the largest **lucky integer** in the array*. If there is no **lucky integer** return `-1`.

 

Example 1:**

```

**Input:** arr = [2,2,3,4]
**Output:** 2
**Explanation:** The only lucky number in the array is 2 because frequency[2] == 2.

```

Example 2:**

```

**Input:** arr = [1,2,2,3,3,3]
**Output:** 3
**Explanation:** 1, 2 and 3 are all lucky numbers, return the largest of them.

```

Example 3:**

```

**Input:** arr = [2,2,2,3,3]
**Output:** -1
**Explanation:** There are no lucky numbers in the array.

```

 

**Constraints:**

	- `1 <= arr.length <= 500`

	- `1 <= arr[i] <= 500`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-07-05 |
| 💻 Language | Python |