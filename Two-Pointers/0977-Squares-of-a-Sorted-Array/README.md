> 📌 **Cross-listed:** Primary location is [Array/0977-Squares-of-a-Sorted-Array](../../Array/0977-Squares-of-a-Sorted-Array). This problem also appears under: **Array**, **Two Pointers**, **Sorting**

# 977. Squares of a Sorted Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/)


## 📝 Problem Description

Given an integer array `nums` sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

 

Example 1:**

```

**Input:** nums = [-4,-1,0,3,10]
**Output:** [0,1,9,16,100]
**Explanation:** After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

```

Example 2:**

```

**Input:** nums = [-7,-3,2,3,11]
**Output:** [4,9,9,49,121]

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-10^4 <= nums[i] <= 10^4`

	- `nums` is sorted in **non-decreasing** order.

 

**Follow up:** Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 9 ms (Beats 65.6%) |
| 💾 Memory | 19.5 MB (Beats 100%) |
| 📅 Solved | 2025-01-23 |
| 💻 Language | Python |