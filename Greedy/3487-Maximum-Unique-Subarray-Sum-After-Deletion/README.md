> 📌 **Cross-listed:** Primary location is [Array/3487-Maximum-Unique-Subarray-Sum-After-Deletion](../../Array/3487-Maximum-Unique-Subarray-Sum-After-Deletion). This problem also appears under: **Array**, **Hash Table**, **Greedy**

# 3487. Maximum Unique Subarray Sum After Deletion


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/)


## 📝 Problem Description

You are given an integer array `nums`.

You are allowed to delete any number of elements from `nums` without making it **empty**. After performing the deletions, select a subarray of `nums` such that:

	- All elements in the subarray are **unique**.

	- The sum of the elements in the subarray is **maximized**.

Return the **maximum sum** of such a subarray.

 

Example 1:**

**Input:** nums = [1,2,3,4,5]

**Output:** 15

**Explanation:**

Select the entire array without deleting any element to obtain the maximum sum.

Example 2:**

**Input:** nums = [1,1,0,1,1]

**Output:** 1

**Explanation:**

Delete the element `nums[0] == 1`, `nums[1] == 1`, `nums[2] == 0`, and `nums[3] == 1`. Select the entire array `[1]` to obtain the maximum sum.

Example 3:**

**Input:** nums = [1,2,-1,-2,1,0,-1]

**Output:** 3

**Explanation:**

Delete the elements `nums[2] == -1` and `nums[3] == -2`, and select the subarray `[2, 1]` from `[1, 2, 1, 0, -1]` to obtain the maximum sum.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `-100 <= nums[i] <= 100`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-07-25 |
| 💻 Language | Python |