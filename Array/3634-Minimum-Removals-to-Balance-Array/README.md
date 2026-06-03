# 3634. Minimum Removals to Balance Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-removals-to-balance-array/)


## 📝 Problem Description

You are given an integer array `nums` and an integer `k`.

An array is considered **balanced** if the value of its **maximum** element is **at most** `k` times the **minimum** element.

You may remove **any** number of elements from `nums`​​​​​​​ without making it **empty**.

Return the **minimum** number of elements to remove so that the remaining array is balanced.

**Note:** An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.

 

Example 1:**

**Input:** nums = [2,1,5], k = 2

**Output:** 1

**Explanation:**

	- Remove `nums[2] = 5` to get `nums = [2, 1]`.

	- Now `max = 2`, `min = 1` and `max <= min * k` as `2 <= 1 * 2`. Thus, the answer is 1.

Example 2:**

**Input:** nums = [1,6,2,9], k = 3

**Output:** 2

**Explanation:**

	- Remove `nums[0] = 1` and `nums[3] = 9` to get `nums = [6, 2]`.

	- Now `max = 6`, `min = 2` and `max <= min * k` as `6 <= 2 * 3`. Thus, the answer is 2.

Example 3:**

**Input:** nums = [4,6], k = 2

**Output:** 0

**Explanation:**

	- Since `nums` is already balanced as `6 <= 4 * 2`, no elements need to be removed.

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `1 <= k <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining a sliding window of elements in the sorted array, where the minimum element is at the left boundary (`l`) and the maximum element is at the right boundary (`r`). The goal is to find the minimum number of elements to remove such that the remaining array is balanced.

**Approach**
1. Sort the input array `nums` in ascending order.
2. Initialize two pointers, `l` and `r`, to the start of the array.
3. Iterate through the array using the `r` pointer.
4. At each step, check if the current element (`nums[r]`) is greater than `k` times the minimum element (`nums[l]`).
5. If the condition is true, increment the `l` pointer to move the minimum element to the right.
6. The number of elements removed is the difference between the initial length of the array and the final position of the `l` pointer.

**Time Complexity**
O(n log n) due to the sorting step, where n is the length of the input array. The subsequent iteration through the array takes O(n) time, but it's dominated by the sorting step.

**Space Complexity**
O(1) (excluding the input array), as we only use a constant amount of space to store the pointers and variables.

**Key Insight**
The key insight is that by maintaining a sliding window of elements, we can efficiently find the minimum number of elements to remove to balance the array. The sorting step allows us to easily identify the minimum and maximum elements within the window, making it possible to check the balance condition in O(1) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 78 ms (Beats 98.55%) |
| 💾 Memory | 34.6 MB (Beats 70.71%) |
| 📅 Solved | 2026-02-06 |
| 💻 Language | Python |