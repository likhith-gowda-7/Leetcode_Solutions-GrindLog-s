> 📌 **Cross-listed:** Primary location is [Array/0209-Minimum-Size-Subarray-Sum](../../Array/0209-Minimum-Size-Subarray-Sum). This problem also appears under: **Array**, **Binary Search**, **Sliding Window**, **Prefix Sum**

# 209. Minimum Size Subarray Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)


## 📝 Problem Description

Given an array of positive integers `nums` and a positive integer `target`, return *the **minimal length** of a **subarray** whose sum is greater than or equal to* `target`. If there is no such subarray, return `0` instead.

 

Example 1:**

```

**Input:** target = 7, nums = [2,3,1,2,4,3]
**Output:** 2
**Explanation:** The subarray [4,3] has the minimal length under the problem constraint.

```

Example 2:**

```

**Input:** target = 4, nums = [1,4,4]
**Output:** 1

```

Example 3:**

```

**Input:** target = 11, nums = [1,1,1,1,1,1,1,1]
**Output:** 0

```

 

**Constraints:**

	- `1 <= target <= 10^9`

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^4`

 

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 10 ms (Beats 97.94%) |
| 💾 Memory | 20.3 MB (Beats 14.08%) |
| 📅 Solved | 2025-03-14 |
| 💻 Language | Python |