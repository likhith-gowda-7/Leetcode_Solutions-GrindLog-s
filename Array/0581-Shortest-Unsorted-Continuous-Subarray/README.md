# 581. Shortest Unsorted Continuous Subarray


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)


## 📝 Problem Description

Given an integer array `nums`, you need to find one **continuous subarray** such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return *the shortest such subarray and output its length*.

 

Example 1:**

```

**Input:** nums = [2,6,4,8,10,9,15]
**Output:** 5
**Explanation:** You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

```

Example 2:**

```

**Input:** nums = [1,2,3,4]
**Output:** 0

```

Example 3:**

```

**Input:** nums = [1]
**Output:** 0

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-10^5 <= nums[i] <= 10^5`

 

**Follow up:** Can you solve it in `O(n)` time complexity?

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 16 ms (Beats 35.76%) |
| 💾 Memory | 18.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-16 |
| 💻 Language | Python |