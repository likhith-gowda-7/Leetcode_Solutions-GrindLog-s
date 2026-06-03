> 📌 **Cross-listed:** Primary location is [Array/0862-Shortest-Subarray-with-Sum-at-Least-K](../../Array/0862-Shortest-Subarray-with-Sum-at-Least-K). This problem also appears under: **Array**, **Binary Search**, **Queue**, **Sliding Window**, **Heap (Priority Queue)**, **Prefix Sum**, **Monotonic Queue**

# 862. Shortest Subarray with Sum at Least K


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Queue](https://img.shields.io/badge/Queue-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)


## 📝 Problem Description

Given an integer array `nums` and an integer `k`, return *the length of the shortest non-empty **subarray** of *`nums`* with a sum of at least *`k`. If there is no such **subarray**, return `-1`.

A **subarray** is a **contiguous** part of an array.

 

Example 1:**

```
**Input:** nums = [1], k = 1
**Output:** 1

```
Example 2:**

```
**Input:** nums = [1,2], k = 4
**Output:** -1

```
Example 3:**

```
**Input:** nums = [2,-1,2], k = 3
**Output:** 3

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^5 <= nums[i] <= 10^5`

	- `1 <= k <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a deque (double-ended queue) to efficiently track the subarray with the smallest sum that meets the condition. The deque stores the indices and corresponding cumulative sums of subarrays. By maintaining a sliding window and using binary search-like logic, we can efficiently find the shortest subarray with a sum of at least k.

**Approach**
1. Initialize variables to keep track of the current cumulative sum (`curr`), the result (`res`), and a deque (`dq`) to store subarray indices and cumulative sums.
2. Iterate through the array, updating the cumulative sum and deque as follows:
   - If the current cumulative sum is greater than or equal to k, update the result with the minimum length of the current subarray.
   - Remove elements from the front of the deque if the difference between the current cumulative sum and the cumulative sum of the subarray at the front of the deque is greater than or equal to k.
   - Remove elements from the back of the deque if the current cumulative sum is less than the cumulative sum of the subarray at the back of the deque.
   - Add the current index and cumulative sum to the back of the deque.
3. If the result is still infinity after iterating through the entire array, return -1; otherwise, return the result.

**Time Complexity**
O(n), where n is the length of the input array. This is because we are iterating through the array once and performing constant-time operations on the deque.

**Space Complexity**
O(n), where n is the length of the input array. This is because in the worst case, we may need to store all elements of the array in the deque.

**Key Insight**
The key insight is to use a deque to efficiently track the subarray with the smallest sum that meets the condition. By maintaining a sliding window and using binary search-like logic, we can efficiently find the shortest subarray with a sum of at least k.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 231 ms (Beats 23.38%) |
| 💾 Memory | 32.8 MB (Beats 100%) |
| 📅 Solved | 2025-04-06 |
| 💻 Language | Python |