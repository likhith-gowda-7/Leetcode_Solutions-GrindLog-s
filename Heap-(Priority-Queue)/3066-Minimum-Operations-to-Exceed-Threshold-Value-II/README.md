> 📌 **Cross-listed:** Primary location is [Array/3066-Minimum-Operations-to-Exceed-Threshold-Value-II](../../Array/3066-Minimum-Operations-to-Exceed-Threshold-Value-II). This problem also appears under: **Array**, **Heap (Priority Queue)**, **Simulation**

# 3066. Minimum Operations to Exceed Threshold Value II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums`, and an integer `k`.

You are allowed to perform some operations on `nums`, where in a single operation, you can:

	- Select the two **smallest** integers `x` and `y` from `nums`.

	- Remove `x` and `y` from `nums`.

	- Insert `(min(x, y) * 2 + max(x, y))` at any position in the array.

**Note** that you can only apply the described operation if `nums` contains **at least** two elements.

Return the **minimum** number of operations needed so that all elements of the array are **greater than or equal to** `k`.

 

Example 1:**

**Input:** nums = [2,11,10,1,3], k = 10

**Output:** 2

**Explanation:**

	- In the first operation, we remove elements 1 and 2, then add `1 * 2 + 2` to `nums`. `nums` becomes equal to `[4, 11, 10, 3]`.

	- In the second operation, we remove elements 3 and 4, then add `3 * 2 + 4` to `nums`. `nums` becomes equal to `[10, 11, 10]`.

At this stage, all the elements of nums are greater than or equal to 10 so we can stop. 

It can be shown that 2 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.

Example 2:**

**Input:** nums = [1,1,2,4,9], k = 20

**Output:** 4

**Explanation:**

	- After one operation, `nums` becomes equal to `[2, 4, 9, 3]`. 

	- After two operations, `nums` becomes equal to `[7, 4, 9]`. 

	- After three operations, `nums` becomes equal to `[15, 9]`. 

	- After four operations, `nums` becomes equal to `[33]`.

At this stage, all the elements of `nums` are greater than 20 so we can stop. 

It can be shown that 4 is the minimum number of operations needed so that all elements of the array are greater than or equal to 20.

 

**Constraints:**

	- `2 <= nums.length <= 2 * 10^5`

	- `1 <= nums[i] <= 10^9`

	- `1 <= k <= 10^9`

	- The input is generated such that an answer always exists. That is, after performing some number of operations, all elements of the array are greater than or equal to `k`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a priority queue (min-heap) to efficiently manage the smallest elements in the array. By repeatedly removing the two smallest elements, combining them, and inserting the result back into the heap, we can simulate the described operations and find the minimum number of operations needed to exceed the threshold value.

**Approach**
1. Initialize a min-heap to store the smallest elements from the input array `nums`.
2. Iterate through `nums` and push each element into the min-heap.
3. Initialize a counter `op` to keep track of the number of operations performed.
4. While the min-heap is not empty:
   1. Pop the two smallest elements `min1` and `min2` from the heap.
   2. If `min1` is greater than or equal to the threshold value `k`, break the loop.
   3. Calculate the new element `curr` by combining `min1` and `min2`.
   4. Push `curr` back into the heap and increment the operation counter `op`.

**Time Complexity**
O(n log n), where n is the length of the input array `nums`. The reason is that we perform a heap operation (push or pop) for each element in `nums`, and each heap operation takes O(log n) time.

**Space Complexity**
O(n), as we need to store all elements from `nums` in the min-heap.

**Key Insight**
The key insight is that by repeatedly combining the two smallest elements, we can effectively "grow" the smallest elements in the array while minimizing the number of operations. This approach takes advantage of the heap data structure to efficiently manage the smallest elements and find the minimum number of operations needed to exceed the threshold value.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 210 ms (Beats 83.74%) |
| 💾 Memory | 35.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-13 |
| 💻 Language | Python |