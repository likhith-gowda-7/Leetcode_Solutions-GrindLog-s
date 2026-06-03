# 2444. Count Subarrays With Fixed Bounds


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Monotonic Queue](https://img.shields.io/badge/Monotonic%20Queue-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/)


## 📝 Problem Description

You are given an integer array `nums` and two integers `minK` and `maxK`.

A **fixed-bound subarray** of `nums` is a subarray that satisfies the following conditions:

	- The **minimum** value in the subarray is equal to `minK`.

	- The **maximum** value in the subarray is equal to `maxK`.

Return *the **number** of fixed-bound subarrays*.

A **subarray** is a **contiguous** part of an array.

 

Example 1:**

```

**Input:** nums = [1,3,5,2,7,5], minK = 1, maxK = 5
**Output:** 2
**Explanation:** The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

```

Example 2:**

```

**Input:** nums = [1,1,1,1], minK = 1, maxK = 1
**Output:** 10
**Explanation:** Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

```

 

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `1 <= nums[i], minK, maxK <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The problem asks us to count the number of subarrays in the given array `nums` where the minimum and maximum values are equal to `minK` and `maxK` respectively. We can use a sliding window approach with the help of a monotonic queue to efficiently count these subarrays.

**Approach**
1. Initialize variables to store the result, the index of the last bad element, and the indices of the last maximum and minimum elements.
2. Iterate over the array `nums` using a right pointer `r`.
3. If the current element is outside the range `[minK, maxK]`, update the index of the last bad element.
4. If the current element is equal to `maxK` or `minK`, update the indices of the last maximum and minimum elements respectively.
5. For each valid maximum and minimum element, calculate the number of subarrays ending at the current position and add it to the result.
6. Return the total count of fixed-bound subarrays.

**Time Complexity**
O(n), where n is the length of the array `nums`. We only iterate over the array once, and the operations within the loop take constant time.

**Space Complexity**
O(1), as we only use a constant amount of space to store the indices and the result.

**Key Insight**
The key insight is to use a monotonic queue to efficiently count the number of subarrays ending at each position. By maintaining the indices of the last maximum and minimum elements, we can calculate the number of subarrays ending at each position in O(1) time. This approach allows us to solve the problem in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 167 ms (Beats 10.6%) |
| 💾 Memory | 28.9 MB (Beats 100%) |
| 📅 Solved | 2025-04-01 |
| 💻 Language | Python |