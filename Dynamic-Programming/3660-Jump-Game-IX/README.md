> 📌 **Cross-listed:** Primary location is [Array/3660-Jump-Game-IX](../../Array/3660-Jump-Game-IX). This problem also appears under: **Array**, **Dynamic Programming**

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

## 🧠 Solution Explanation

**Intuition**
The problem requires finding the maximum value that can be reached by following valid jumps from each index in the array. The key insight is to use dynamic programming to build two arrays, prefix max and suffix min, which represent the maximum value that can be reached by jumping to the left and right of each index, respectively. By merging these two arrays, we can find the maximum value that can be reached from each index.

**Approach**
1. Initialize three arrays: `pre`, `suf`, and `res`, where `pre` and `suf` store the prefix max and suffix min values, respectively, and `res` stores the maximum value that can be reached from each index.
2. Build the `pre` array by iterating from left to right and updating each element with the maximum of the previous element and the current element.
3. Build the `suf` array by iterating from right to left and updating each element with the minimum of the next element and the current element.
4. Initialize the last element of `res` with the last element of `pre`.
5. Iterate from right to left and update each element of `res` by merging the corresponding elements of `pre` and `suf`. If the prefix max value is greater than the suffix min value, use the prefix max value; otherwise, use the suffix min value.

**Time Complexity**
O(n), where n is the length of the input array, since we iterate through the array twice to build the `pre` and `suf` arrays and once to build the `res` array.

**Space Complexity**
O(n), where n is the length of the input array, since we need to store the `pre`, `suf`, and `res` arrays, each of length n.

**Key Insight**
The key insight is to use dynamic programming to build the `pre` and `suf` arrays, which represent the maximum value that can be reached by jumping to the left and right of each index, respectively. By merging these two arrays, we can find the maximum value that can be reached from each index.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 223 ms (Beats 51.6%) |
| 💾 Memory | 39.6 MB (Beats 55.76%) |
| 📅 Solved | 2026-05-07 |
| 💻 Language | Python |