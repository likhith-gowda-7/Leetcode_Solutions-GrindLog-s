# 3691. Maximum Total Subarray Value II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-total-subarray-value-ii/)


## 📝 Problem Description

You are given an integer array `nums` of length `n` and an integer `k`.

You must select **exactly** `k` **distinct** subarrays `nums[l..r]` of `nums`. Subarrays may overlap, but the exact same subarray (same `l` and `r`) **cannot** be chosen more than once.

The **value** of a subarray `nums[l..r]` is defined as: `max(nums[l..r]) - min(nums[l..r])`.

The **total value** is the sum of the **values** of all chosen subarrays.

Return the **maximum** possible total value you can achieve.

 

Example 1:**

**Input:** nums = [1,3,2], k = 2

**Output:** 4

**Explanation:**

One optimal approach is:

	- Choose `nums[0..1] = [1, 3]`. The maximum is 3 and the minimum is 1, giving a value of `3 - 1 = 2`.

	- Choose `nums[0..2] = [1, 3, 2]`. The maximum is still 3 and the minimum is still 1, so the value is also `3 - 1 = 2`.

Adding these gives `2 + 2 = 4`.

Example 2:**

**Input:** nums = [4,2,5,1], k = 3

**Output:** 12

**Explanation:**

One optimal approach is:

	- Choose `nums[0..3] = [4, 2, 5, 1]`. The maximum is 5 and the minimum is 1, giving a value of `5 - 1 = 4`.

	- Choose `nums[1..3] = [2, 5, 1]`. The maximum is 5 and the minimum is 1, so the value is also `4`.

	- Choose `nums[2..3] = [5, 1]`. The maximum is 5 and the minimum is 1, so the value is again `4`.

Adding these gives `4 + 4 + 4 = 12`.

 

**Constraints:**

	- `1 <= n == nums.length <= 5 * 10^​​​​​​​4`

	- `0 <= nums[i] <= 10^9`

	- `1 <= k <= min(10^5, n * (n + 1) / 2)`

## 🧠 Solution Explanation

**Intuition**
The solution uses a combination of a sparse table and a priority queue to efficiently find the maximum possible total value. The sparse table allows for fast querying of the maximum and minimum values in a subarray, while the priority queue helps to select the most valuable subarrays.

**Approach**
1. Create a sparse table to store the maximum and minimum values in subarrays of the input array `nums`.
2. Initialize a priority queue `pq` with the values of all subarrays in `nums`, along with their start and end indices.
3. Iterate `k` times, popping the subarray with the maximum value from the priority queue and updating the total value.
4. For each iteration, remove the popped subarray from the priority queue and add the subarray with the next maximum value to the priority queue.
5. After `k` iterations, return the total value.

**Time Complexity**
The time complexity of the solution is O(n log n + k log n), where n is the length of the input array `nums`. This is because creating the sparse table takes O(n log n) time, and each iteration of the priority queue takes O(log n) time.

**Space Complexity**
The space complexity of the solution is O(n log n), which is used to store the sparse table.

**Key Insight**
The key insight behind this solution is the use of a sparse table to efficiently query the maximum and minimum values in subarrays. This allows for fast updates to the priority queue, enabling the solution to find the maximum possible total value in O(n log n + k log n) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3106 ms (Beats 73.17%) |
| 💾 Memory | 41.6 MB (Beats 63.41%) |
| 📅 Solved | 2026-06-10 |
| 💻 Language | Python |