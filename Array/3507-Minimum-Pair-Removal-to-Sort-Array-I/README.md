# 3507. Minimum Pair Removal to Sort Array I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Linked List](https://img.shields.io/badge/Linked%20List-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/)


## 📝 Problem Description

Given an array `nums`, you can perform the following operation any number of times:

	- Select the **adjacent** pair with the **minimum** sum in `nums`. If multiple such pairs exist, choose the leftmost one.

	- Replace the pair with their sum.

Return the **minimum number of operations** needed to make the array **non-decreasing**.

An array is said to be **non-decreasing** if each element is greater than or equal to its previous element (if it exists).

 

Example 1:**

**Input:** nums = [5,2,3,1]

**Output:** 2

**Explanation:**

	- The pair `(3,1)` has the minimum sum of 4. After replacement, `nums = [5,2,4]`.

	- The pair `(2,4)` has the minimum sum of 6. After replacement, `nums = [5,6]`.

The array `nums` became non-decreasing in two operations.

Example 2:**

**Input:** nums = [1,2,2]

**Output:** 0

**Explanation:**

The array `nums` is already sorted.

 

**Constraints:**

	- `1 <= nums.length <= 50`

	- `-1000 <= nums[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
The solution works by iteratively removing the minimum pair in the array and replacing it with their sum, until the array becomes non-decreasing. This approach is based on the observation that removing the minimum pair will always result in a non-decreasing array if the remaining elements are already non-decreasing.

**Approach**
1. Define a helper function `check(arr)` to verify if the array is non-decreasing.
2. Initialize variables to keep track of the minimum sum, index, and count of operations.
3. Enter a loop that continues until the array is non-decreasing.
4. Inside the loop, find the minimum sum of adjacent pairs and update the minimum sum, index, and count of operations.
5. Replace the minimum pair with their sum and remove the right element from the array.
6. Repeat steps 4-5 until the array is non-decreasing.
7. Return the count of operations.

**Time Complexity**
O(n^2) because in the worst case, we need to iterate over the array to find the minimum sum of adjacent pairs in each iteration, and there are n iterations in total.

**Space Complexity**
O(1) because we only use a constant amount of space to store the variables, regardless of the size of the input array.

**Key Insight**
The key insight is that removing the minimum pair will always result in a non-decreasing array if the remaining elements are already non-decreasing. This allows us to use a simple iterative approach to solve the problem, without the need for more complex data structures or algorithms.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 11 ms (Beats 73.64%) |
| 💾 Memory | 19.4 MB (Beats 25.58%) |
| 📅 Solved | 2026-01-22 |
| 💻 Language | Python |