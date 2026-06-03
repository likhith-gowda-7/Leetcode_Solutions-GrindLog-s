# 3719. Longest Balanced Subarray I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Divide and Conquer](https://img.shields.io/badge/Divide%20and%20Conquer-purple) ![Segment Tree](https://img.shields.io/badge/Segment%20Tree-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-balanced-subarray-i/)


## 📝 Problem Description

You are given an integer array `nums`.

A **subarray** is called **balanced** if the number of **distinct even** numbers in the subarray is equal to the number of **distinct odd** numbers.

Return the length of the **longest** balanced subarray.

 

Example 1:**

**Input:** nums = [2,5,4,3]

**Output:** 4

**Explanation:**

	- The longest balanced subarray is `[2, 5, 4, 3]`.

	- It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[5, 3]`. Thus, the answer is 4.

Example 2:**

**Input:** nums = [3,2,2,5,4]

**Output:** 5

**Explanation:**

	- The longest balanced subarray is `[3, 2, 2, 5, 4]`.

	- It has 2 distinct even numbers `[2, 4]` and 2 distinct odd numbers `[3, 5]`. Thus, the answer is 5.

Example 3:**

**Input:** nums = [1,2,3,2]

**Output:** 3

**Explanation:**

	- The longest balanced subarray is `[2, 3, 2]`.

	- It has 1 distinct even number `[2]` and 1 distinct odd number `[3]`. Thus, the answer is 3.

 

**Constraints:**

	- `1 <= nums.length <= 1500`

	- `1 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach to find the longest balanced subarray. It iterates over the array, maintaining two sets to track the distinct even and odd numbers within the current window. When the number of distinct even and odd numbers are equal, it updates the maximum length of the balanced subarray.

**Approach**
1. Initialize variables to store the maximum length of the balanced subarray (`maxi`) and the length of the input array (`n`).
2. Iterate over the array using a sliding window, starting from the first element (`i`).
3. For each window, initialize two sets to store the distinct even (`even`) and odd (`odd`) numbers.
4. Iterate over the elements within the current window (`j` ranges from `i` to `n-1`).
5. For each element, add it to the corresponding set based on its parity (even or odd).
6. Check if the number of distinct even and odd numbers are equal. If they are, update the maximum length of the balanced subarray (`maxi`) with the current window size (`j-i+1`).
7. Repeat steps 4-6 for each window until the end of the array.

**Time Complexity**
O(n^2), where n is the length of the input array. This is because for each window, we are iterating over the remaining elements in the array.

**Space Complexity**
O(n), where n is the length of the input array. This is because in the worst case, we are storing all elements in the `even` and `odd` sets.

**Key Insight**
The key insight is to use a sliding window approach to efficiently find the longest balanced subarray. By maintaining two sets to track the distinct even and odd numbers, we can quickly determine when the number of distinct even and odd numbers are equal, allowing us to update the maximum length of the balanced subarray.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 1269 ms (Beats 58.75%) |
| 💾 Memory | 19.6 MB (Beats 18.51%) |
| 📅 Solved | 2026-02-10 |
| 💻 Language | Python |