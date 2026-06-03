# 918. Maximum Sum Circular Subarray


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Queue](https://img.shields.io/badge/Queue-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-sum-circular-subarray/)


## 📝 Problem Description

Given a **circular integer array** `nums` of length `n`, return *the maximum possible sum of a non-empty **subarray** of *`nums`.

A **circular array** means the end of the array connects to the beginning of the array. Formally, the next element of `nums[i]` is `nums[(i + 1) % n]` and the previous element of `nums[i]` is `nums[(i - 1 + n) % n]`.

A **subarray** may only include each element of the fixed buffer `nums` at most once. Formally, for a subarray `nums[i], nums[i + 1], ..., nums[j]`, there does not exist `i <= k1`, `k2 <= j` with `k1 % n == k2 % n`.

 

Example 1:**

```

**Input:** nums = [1,-2,3,-2]
**Output:** 3
**Explanation:** Subarray [3] has maximum sum 3.

```

Example 2:**

```

**Input:** nums = [5,-3,5]
**Output:** 10
**Explanation:** Subarray [5,5] has maximum sum 5 + 5 = 10.

```

Example 3:**

```

**Input:** nums = [-3,-2,-3]
**Output:** -2
**Explanation:** Subarray [-2] has maximum sum -2.

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 3 * 10^4`

	- `-3 * 10^4 <= nums[i] <= 3 * 10^4`

## 🧠 Solution Explanation

**Intuition**
The solution uses Kadane's algorithm to find the maximum and minimum sum of subarrays in the given circular array. It keeps track of the maximum and minimum sum of subarrays ending at the current position and updates the overall maximum and minimum sum. The key insight is that the maximum sum of a subarray in a circular array is either the maximum sum of a subarray in the linear array or the total sum minus the minimum sum of a subarray in the linear array.

**Approach**
1. Initialize `maxi` and `mini` to the first element of the array, and `curr_max` and `curr_min` to 0.
2. Iterate through the array, updating `curr_max` and `curr_min` as follows:
   - `curr_max` is the maximum of the current element and the sum of the current element and `curr_max`.
   - `curr_min` is the minimum of the current element and the sum of the current element and `curr_min`.
3. Update `maxi` and `mini` to be the maximum of the current `maxi` and `curr_max`, and the minimum of the current `mini` and `curr_min`, respectively.
4. Keep a running total of the sum of all elements in the array.
5. If `maxi` is negative, return `maxi` as the maximum sum of a subarray.
6. Otherwise, return the maximum of `maxi` and the total sum minus `mini`.

**Time Complexity**
O(n), where n is the length of the array, because we make a single pass through the array.

**Space Complexity**
O(1), because we use a constant amount of space to store the variables `maxi`, `mini`, `curr_max`, `curr_min`, and `total`.

**Key Insight**
The key insight is that the maximum sum of a subarray in a circular array is either the maximum sum of a subarray in the linear array or the total sum minus the minimum sum of a subarray in the linear array. This allows us to solve the problem in a single pass through the array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 98 ms (Beats 5.1%) |
| 💾 Memory | 21.3 MB (Beats 100%) |
| 📅 Solved | 2025-04-05 |
| 💻 Language | Python |