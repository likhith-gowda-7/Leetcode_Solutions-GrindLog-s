> 📌 **Cross-listed:** Primary location is [Array/3356-Zero-Array-Transformation-II](../../Array/3356-Zero-Array-Transformation-II). This problem also appears under: **Array**, **Two Pointers**, **Binary Search**, **Prefix Sum**

# 3356. Zero Array Transformation II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/zero-array-transformation-ii/)


## 📝 Problem Description

You are given an integer array `nums` of length `n` and a 2D array `queries` where `queries[i] = [l_i, r_i, val_i]`.

Each `queries[i]` represents the following action on `nums`:

	- Decrement the value at each index in the range `[l_i, r_i]` in `nums` by **at most** `val_i`.

	- The amount by which each value is decremented can be chosen **independently** for each index.

A **Zero Array** is an array with all its elements equal to 0.

Return the **minimum** possible **non-negative** value of `k`, such that after processing the first `k` queries in **sequence**, `nums` becomes a **Zero Array**. If no such `k` exists, return -1.

 

Example 1:**

**Input:** nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

**Output:** 2

**Explanation:**

	- **For i = 0 (l = 0, r = 2, val = 1):**

	
		- Decrement values at indices `[0, 1, 2]` by `[1, 0, 1]` respectively.

		- The array will become `[1, 0, 1]`.

	
	

	- **For i = 1 (l = 0, r = 2, val = 1):**
	
		- Decrement values at indices `[0, 1, 2]` by `[1, 0, 1]` respectively.

		- The array will become `[0, 0, 0]`, which is a Zero Array. Therefore, the minimum value of `k` is 2.

	
	

Example 2:**

**Input:** nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

**Output:** -1

**Explanation:**

	- **For i = 0 (l = 1, r = 3, val = 2):**

	
		- Decrement values at indices `[1, 2, 3]` by `[2, 2, 1]` respectively.

		- The array will become `[4, 1, 0, 0]`.

	
	

	- **For i = 1 (l = 0, r = 2, val = 1):**
	
		- Decrement values at indices `[0, 1, 2]` by `[1, 1, 0]` respectively.

		- The array will become `[3, 0, 0, 0]`, which is not a Zero Array.

	
	

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 5 * 10^5`

	- `1 <= queries.length <= 10^5`

	- `queries[i].length == 3`

	- `0 <= l_i <= r_i < nums.length`

	- `1 <= val_i <= 5`

## 🧠 Solution Explanation

**Intuition**
The solution uses a prefix sum array to efficiently calculate the total decrement value for each index in the array. It iterates through the array and queries, adjusting the prefix sum array to reflect the minimum decrement value required to make the array a Zero Array.

**Approach**
1. Initialize a prefix sum array `diff` of size `n+1` to store the total decrement value for each index.
2. Initialize `sum_val` to 0, which stores the cumulative sum of the prefix sum array.
3. Iterate through the array `nums` and queries `queries` simultaneously.
4. For each index `i` in the array, calculate the minimum decrement value required to make the array a Zero Array by checking if `sum_val + diff[i] < nums[i]`.
5. If the minimum decrement value is not sufficient, increment `pos` to move to the next query.
6. If `pos` reaches the end of the queries, return -1 as no such `k` exists.
7. Otherwise, update the prefix sum array `diff` based on the current query and increment `pos`.
8. Update `sum_val` by adding the current prefix sum value.
9. Return `pos` as the minimum possible non-negative value of `k`.

**Time Complexity**
O(n + m), where n is the length of the array and m is the number of queries. The solution iterates through the array and queries once, resulting in a linear time complexity.

**Space Complexity**
O(n), where n is the length of the array. The solution uses a prefix sum array of size n+1 to store the total decrement value for each index.

**Key Insight**
The key insight is to use a prefix sum array to efficiently calculate the total decrement value for each index in the array. By adjusting the prefix sum array based on the current query, the solution can determine the minimum possible non-negative value of k required to make the array a Zero Array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 163 ms (Beats 68.22%) |
| 💾 Memory | 63.1 MB (Beats 100%) |
| 📅 Solved | 2025-03-14 |
| 💻 Language | Python |