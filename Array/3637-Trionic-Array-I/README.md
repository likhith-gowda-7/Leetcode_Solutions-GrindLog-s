# 3637. Trionic Array I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/trionic-array-i/)


## 📝 Problem Description

You are given an integer array nums` of length n`.

An array is trionic** if there exist indices 0 < p < q < n &minus; 1` such that:

	nums[0...p]` is **strictly** increasing,

	nums[p...q]` is **strictly** decreasing,

	nums[q...n &minus; 1]` is **strictly** increasing.

Return true` if nums` is trionic, otherwise return false`.

 

Example 1:**

**Input:** nums = [1,3,5,4,2,6]

**Output:** true

**Explanation:**

Pick p = 2`, q = 4`:

	- nums[0...2] = [1, 3, 5]` is strictly increasing (1 < 3 < 5`).

	- nums[2...4] = [5, 4, 2]` is strictly decreasing (5 > 4 > 2`).

	- nums[4...5] = [2, 6]` is strictly increasing (2 < 6`).

Example 2:**

**Input:** nums = [2,1,3]

**Output:** false

**Explanation:**

There is no way to pick `p` and `q` to form the required three segments.

 

**Constraints:**

	3 <= n <= 100`

	-1000 <= nums[i] <= 1000`

## 🧠 Solution Explanation

**Intuition**
This solution works by iterating through the array and checking for the conditions of a trionic array. It first finds the index `p` where the array starts to decrease, then finds the index `q` where the array starts to increase again. If both `p` and `q` are found within the array, the array is trionic.

**Approach**
1. Initialize `found` to 0 and `i` to 0.
2. Iterate through the array from left to right, incrementing `i` as long as the current element is less than the next element.
3. If `i` reaches the end of the array or the beginning of the array, return False, as a trionic array must have at least two elements.
4. If `i` is at the end of the array, return False, as there is no decreasing segment.
5. Iterate through the array from `i` to the end, incrementing `i` as long as the current element is greater than the next element.
6. If `i` reaches the end of the array, return False, as there is no increasing segment after the decreasing segment.
7. Iterate through the array from `i` to the end, incrementing `i` as long as the current element is less than the next element.
8. If `i` reaches the end of the array, return True, as the array is trionic.
9. Otherwise, return False.

**Time Complexity**
O(n), where n is the length of the array. This is because the solution iterates through the array at most three times.

**Space Complexity**
O(1), as the solution uses a constant amount of space to store the indices `i` and `found`.

**Key Insight**
The key insight is that a trionic array must have at least two elements, and the decreasing segment must be followed by an increasing segment. The solution iterates through the array to find these two segments, and checks if they exist within the array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 70.89%) |
| 📅 Solved | 2026-02-03 |
| 💻 Language | Python |