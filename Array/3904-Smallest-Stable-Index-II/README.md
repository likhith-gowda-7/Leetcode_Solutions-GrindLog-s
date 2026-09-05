# 3904. Smallest Stable Index II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/smallest-stable-index-ii/)


## 📝 Problem Description

You are given an integer array `nums` of length `n` and an integer `k`.

For each index `i`, define its **instability score** as `max(nums[0..i]) - min(nums[i..n - 1])`.

In other words:

	- `max(nums[0..i])` is the **largest** value among the elements from index 0 to index `i`.

	- `min(nums[i..n - 1])` is the **smallest** value among the elements from index `i` to index `n - 1`.

An index `i` is called **stable** if its instability score is **less than or equal to** `k`.

Return the **smallest** stable index. If no such index exists, return -1.

 

Example 1:**

**Input:** nums = [5,0,1,4], k = 3

**Output:** 3

**Explanation:**

	- At index 0: The maximum in `[5]` is 5, and the minimum in `[5, 0, 1, 4]` is 0, so the instability score is `5 - 0 = 5`.

	- At index 1: The maximum in `[5, 0]` is 5, and the minimum in `[0, 1, 4]` is 0, so the instability score is `5 - 0 = 5`.

	- At index 2: The maximum in `[5, 0, 1]` is 5, and the minimum in `[1, 4]` is 1, so the instability score is `5 - 1 = 4`.

	- At index 3: The maximum in `[5, 0, 1, 4]` is 5, and the minimum in `[4]` is 4, so the instability score is `5 - 4 = 1`.

	- This is the first index with an instability score less than or equal to `k = 3`. Thus, the answer is 3.

Example 2:**

**Input:** nums = [3,2,1], k = 1

**Output:** -1

**Explanation:**

	- At index 0, the instability score is `3 - 1 = 2`.

	- At index 1, the instability score is `3 - 1 = 2`.

	- At index 2, the instability score is `3 - 1 = 2`.

	- None of these values is less than or equal to `k = 1`, so the answer is -1.

Example 3:**

**Input:** nums = [0], k = 0

**Output:** 0

**Explanation:**

At index 0, the instability score is `0 - 0 = 0`, which is less than or equal to `k = 0`. Therefore, the answer is 0.

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^9`

	- `0 <= k <= 10^9`

## 🧠 Solution Explanation

**Intuition**  
The instability at index *i* depends only on the largest value to its left (including itself) and the smallest value to its right (including itself). If we know the suffix minimum for every position, we can evaluate each index in a single forward scan.

**Approach**  
1. Build an array `mini` where `mini[i]` is the minimum of `nums[i…n‑1]`.  
   *Traverse from right to left, keeping the running minimum.*  
2. Scan `nums` from left to right, maintaining `maxi`, the maximum seen so far.  
   For each index `i`:  
   - Update `maxi = max(maxi, nums[i])`.  
   - Compute `curr = maxi - mini[i]`.  
   - If `curr ≤ k`, return `i` immediately (the first such index).  
3. If the loop finishes without a hit, return `-1`.

**Time Complexity**  
Two linear passes over the array → **O(n)** time. Each operation inside the loops is O(1).

**Space Complexity**  
The `mini` array of length `n` plus a few variables → **O(n)** auxiliary space.

**Key Insight**  
Precomputing suffix minima lets us evaluate the instability of every index in a single forward pass, turning a naïve O(n²) check into an efficient O(n) solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 138 ms (Beats 86.82%) |
| 💾 Memory | 33 MB (Beats 49.55%) |
| 📅 Solved | 2026-09-05 |
| 💻 Language | Python |