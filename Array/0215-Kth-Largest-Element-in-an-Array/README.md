# 215. Kth Largest Element in an Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)


## 📝 Problem Description

Given an integer array `nums` and an integer `k`, return *the* `k^th` *largest element in the array*.

Note that it is the `k^th` largest element in the sorted order, not the `k^th` distinct element.

Can you solve it without sorting?

 

Example 1:**

```
**Input:** nums = [3,2,1,5,6,4], k = 2
**Output:** 5

```
Example 2:**

```
**Input:** nums = [3,2,3,1,2,4,5,5,6], k = 4
**Output:** 4

```

 

**Constraints:**

	- `1 <= k <= nums.length <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

## 🧠 Solution Explanation

## Intuition
The solution works by utilizing a max heap data structure to efficiently find the kth largest element in the array. By maintaining a max heap, we can easily remove the largest element and repeat this process until we find the kth largest element. This approach takes advantage of the heap property, where the parent node is always greater than its child nodes.

## Approach
1. First, we convert the input array into a max heap using the `heapq._heapify_max` function.
2. Then, we remove the largest element from the max heap `k-1` times using the `heapq._heappop_max` function.
3. After removing the largest elements, the root of the max heap will be the kth largest element, which we return as the result.

## Time Complexity
The time complexity is O(n + k log n), where n is the number of elements in the array. The `heapq._heapify_max` function takes O(n) time, and the `heapq._heappop_max` function takes O(log n) time. Since we call `heapq._heappop_max` k-1 times, the total time complexity is O(n + k log n).

## Space Complexity
The space complexity is O(n), as we need to store all elements in the max heap.

## Key Insight
The key insight here is that using a max heap allows us to efficiently find the kth largest element without sorting the entire array, reducing the time complexity from O(n log n) to O(n + k log n). This approach is particularly useful when k is much smaller than n, making it a efficient solution for large arrays.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 81 ms (Beats 60.88%) |
| 💾 Memory | 26.7 MB (Beats 100%) |
| 📅 Solved | 2025-07-04 |
| 💻 Language | Python |