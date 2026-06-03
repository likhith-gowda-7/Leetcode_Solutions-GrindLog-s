# 3355. Zero Array Transformation I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/zero-array-transformation-i/)


## 📝 Problem Description

You are given an integer array `nums` of length `n` and a 2D array `queries`, where `queries[i] = [l_i, r_i]`.

For each `queries[i]`:

	- Select a subset of indices within the range `[l_i, r_i]` in `nums`.

	- Decrement the values at the selected indices by 1.

A **Zero Array** is an array where all elements are equal to 0.

Return `true` if it is *possible* to transform `nums` into a **Zero Array **after processing all the queries sequentially, otherwise return `false`.

 

Example 1:**

**Input:** nums = [1,0,1], queries = [[0,2]]

**Output:** true

**Explanation:**

	- **For i = 0:**

	
		- Select the subset of indices as `[0, 2]` and decrement the values at these indices by 1.

		- The array will become `[0, 0, 0]`, which is a Zero Array.

	
	

Example 2:**

**Input:** nums = [4,3,2,1], queries = [[1,3],[0,2]]

**Output:** false

**Explanation:**

	- **For i = 0:**

	
		- Select the subset of indices as `[1, 2, 3]` and decrement the values at these indices by 1.

		- The array will become `[4, 2, 1, 0]`.

	
	

	- **For i = 1:**
	
		- Select the subset of indices as `[0, 1, 2]` and decrement the values at these indices by 1.

		- The array will become `[3, 1, 0, 0]`, which is not a Zero Array.

	
	

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^5`

	- `1 <= queries.length <= 10^5`

	- `queries[i].length == 2`

	- `0 <= l_i <= r_i < nums.length`

## 🧠 Solution Explanation

**Intuition**
The solution uses a technique called "line sweep" or "difference array" to efficiently process the queries and determine if it's possible to transform the array into a Zero Array. The key insight is to maintain a running sum of the decrements and increments caused by the queries, allowing us to check if the array can be made zero in a single pass.

**Approach**
1. Initialize a difference array `diff_arr` of size `n+1` with all elements set to 0, where `n` is the length of the input array `nums`.
2. Iterate through the queries and update the difference array accordingly:
   - For each query `[left, right]`, increment the value at index `left` by 1 and decrement the value at index `right+1` by 1.
3. Iterate through the difference array and calculate the running sum for each element:
   - For each element `i` (except the first one), add the value at `i-1` to `diff_arr[i]`.
4. Check if the array can be made zero by iterating through `nums` and `diff_arr` simultaneously:
   - For each element `i` in `nums`, check if `nums[i]` is greater than `diff_arr[i]`. If true, return False.

**Time Complexity**
O(n + q), where n is the length of the input array `nums` and q is the number of queries. This is because we perform a single pass through the queries and the difference array.

**Space Complexity**
O(n), as we need to store the difference array of size `n+1`.

**Key Insight**
The key insight is to maintain a running sum of the decrements and increments caused by the queries, allowing us to check if the array can be made zero in a single pass. This is achieved by using a difference array, which simplifies the problem and enables an efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 70 ms (Beats 76.1%) |
| 💾 Memory | 54.9 MB (Beats 86.83%) |
| 📅 Solved | 2025-05-20 |
| 💻 Language | Python |