# 3660. Jump Game IX


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/jump-game-ix/)


## 📝 Problem Description

You are given an integer array `nums`.

From any index `i`, you can jump to another index `j` under the following rules:

	- Jump to index `j` where `j > i` is allowed only if `nums[j] < nums[i]`.

	- Jump to index `j` where `j < i` is allowed only if `nums[j] > nums[i]`.

For each index `i`, find the **maximum** **value** in `nums` that can be reached by following **any** sequence of valid jumps starting at `i`.

Return an array `ans` where `ans[i]` is the **maximum** **value** reachable starting from index `i`.

 

Example 1:**

**Input:** nums = [2,1,3]

**Output:** [2,2,3]

**Explanation:**

	- For `i = 0`: No jump increases the value.

	- For `i = 1`: Jump to `j = 0` as `nums[j] = 2` is greater than `nums[i]`.

	- For `i = 2`: Since `nums[2] = 3` is the maximum value in `nums`, no jump increases the value.

Thus, `ans = [2, 2, 3]`.

Example 2:**

**Input:** nums = [2,3,1]

**Output:** [3,3,3]

**Explanation:**

	- For `i = 0`: Jump forward to `j = 2` as `nums[j] = 1` is less than `nums[i] = 2`, then from `i = 2` jump to `j = 1` as `nums[j] = 3` is greater than `nums[2]`.

	- For `i = 1`: Since `nums[1] = 3` is the maximum value in `nums`, no jump increases the value.

	- For `i = 2`: Jump to `j = 1` as `nums[j] = 3` is greater than `nums[2] = 1`.

Thus, `ans = [3, 3, 3]`.

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9​​​​​​​`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 223 ms (Beats 51.6%) |
| 💾 Memory | 39.6 MB (Beats 55.76%) |
| 📅 Solved | 2026-05-07 |
| 💻 Language | Python |