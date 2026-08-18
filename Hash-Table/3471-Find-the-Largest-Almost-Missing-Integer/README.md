> 📌 **Cross-listed:** Primary location is [Array/3471-Find-the-Largest-Almost-Missing-Integer](../../Array/3471-Find-the-Largest-Almost-Missing-Integer). This problem also appears under: **Array**, **Hash Table**

# 3471. Find the Largest Almost Missing Integer


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-largest-almost-missing-integer/)


## 📝 Problem Description

You are given an integer array `nums` and an integer `k`.

An integer `x` is **almost missing** from `nums` if `x` appears in *exactly* one subarray of size `k` within `nums`.

Return the **largest** **almost missing** integer from `nums`. If no such integer exists, return `-1`.

A **subarray** is a contiguous sequence of elements within an array.
 

Example 1:**

**Input:** nums = [3,9,2,1,7], k = 3

**Output:** 7

**Explanation:**

	- 1 appears in 2 subarrays of size 3: `[9, 2, 1]` and `[2, 1, 7]`.

	- 2 appears in 3 subarrays of size 3: `[3, 9, 2]`, `[9, 2, 1]`, `[2, 1, 7]`.

	3 appears in 1 subarray of size 3: `[3, 9, 2]`.

	7 appears in 1 subarray of size 3: `[2, 1, 7]`.

	9 appears in 2 subarrays of size 3: `[3, 9, 2]`, and `[9, 2, 1]`.

We return 7 since it is the largest integer that appears in exactly one subarray of size `k`.

Example 2:**

**Input:** nums = [3,9,7,2,1,7], k = 4

**Output:** 3

**Explanation:**

	- 1 appears in 2 subarrays of size 4: `[9, 7, 2, 1]`, `[7, 2, 1, 7]`.

	- 2 appears in 3 subarrays of size 4: `[3, 9, 7, 2]`, `[9, 7, 2, 1]`, `[7, 2, 1, 7]`.

	- 3 appears in 1 subarray of size 4: `[3, 9, 7, 2]`.

	- 7 appears in 3 subarrays of size 4: `[3, 9, 7, 2]`, `[9, 7, 2, 1]`, `[7, 2, 1, 7]`.

	- 9 appears in 2 subarrays of size 4: `[3, 9, 7, 2]`, `[9, 7, 2, 1]`.

We return 3 since it is the largest and only integer that appears in exactly one subarray of size `k`.

Example 3:**

**Input:** nums = [0,0], k = 1

**Output:** -1

**Explanation:**

There is no integer that appears in only one subarray of size 1.

 

**Constraints:**

	- `1 <= nums.length <= 50`

	- `0 <= nums[i] <= 50`

	- `1 <= k <= nums.length`

## 🧠 Solution Explanation

**Intuition**  
The number of subarrays of length k that contain a particular element depends only on how many times that element appears and where those appearances lie.  
If an element occurs more than once, it will inevitably appear in at least two different k‑length windows.  
Thus, only elements that appear exactly once can be “almost missing.”  
Among those, the largest candidate must be one of the array’s endpoints, because a single occurrence can only be captured by a window that starts or ends at that position.

**Approach**  
1. Count frequencies of all numbers with a `Counter`.  
2. Handle trivial cases:  
   * If `k == n`, every element appears in the single window → return the maximum.  
   * If `k == 1`, each element forms its own window → return the largest element whose frequency is 1.  
3. If both the first and last elements appear more than once, no element can be almost missing → return -1.  
4. Initialize `res` to the first element if it is unique; otherwise `0`.  
5. If the last element is larger than `res` and unique, update `res` to it.  
6. Return `res` (or `-1` if no unique endpoint exists).

**Time Complexity**  
`O(n)` – one pass to build the counter and a few constant‑time checks.  
**Space Complexity**  
`O(n)` – the counter stores up to `n` distinct values.

**Key Insight**  
A number that appears only once can be almost missing only if its single occurrence lies at an array boundary; otherwise it would be included in at least two k‑length windows. This reduces the search to the two endpoints.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 75.41%) |
| 📅 Solved | 2026-08-18 |
| 💻 Language | Python |