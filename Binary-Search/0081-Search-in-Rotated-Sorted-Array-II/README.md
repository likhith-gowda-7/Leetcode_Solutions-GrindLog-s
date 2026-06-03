> 📌 **Cross-listed:** Primary location is [Array/0081-Search-in-Rotated-Sorted-Array-II](../../Array/0081-Search-in-Rotated-Sorted-Array-II). This problem also appears under: **Array**, **Binary Search**

# 81. Search in Rotated Sorted Array II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)


## 📝 Problem Description

There is an integer array `nums` sorted in non-decreasing order (not necessarily with **distinct** values).

Before being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` **after** the rotation and an integer `target`, return `true`* if *`target`* is in *`nums`*, or *`false`* if it is not in *`nums`*.*

You must decrease the overall operation steps as much as possible.

 

Example 1:**

```
**Input:** nums = [2,5,6,0,0,1,2], target = 0
**Output:** true

```
Example 2:**

```
**Input:** nums = [2,5,6,0,0,1,2], target = 3
**Output:** false

```

 

**Constraints:**

	- `1 <= nums.length <= 5000`

	- `-10^4 <= nums[i] <= 10^4`

	- `nums` is guaranteed to be rotated at some pivot.

	- `-10^4 <= target <= 10^4`

 

**Follow up:** This problem is similar to [Search in Rotated Sorted Array](/problems/search-in-rotated-sorted-array/description/), but `nums` may contain **duplicates**. Would this affect the runtime complexity? How and why?

## 🧠 Solution Explanation

## Intuition
This approach works by utilizing a modified binary search algorithm that accounts for the rotation and potential duplicates in the array. The key idea is to determine which half of the array is sorted and then decide which half to continue searching in. The presence of duplicates requires special handling to avoid getting stuck in an infinite loop.

## Approach
1. Initialize two pointers, `left` and `right`, to the start and end of the array, respectively.
2. Loop until `left` is greater than `right`.
3. Calculate the `mid` index and check if the target is found at this index. If so, return `True`.
4. If the values at `left`, `mid`, and `right` are the same, increment `left` and decrement `right` to handle duplicates.
5. Determine which half of the array is sorted and decide which half to continue searching in based on the target value.
6. Repeat steps 3-5 until the target is found or the search space is exhausted.

## Time Complexity
The time complexity is O(n) in the worst case, where n is the number of elements in the array. This occurs when the array is filled with duplicates, and the algorithm has to iterate through the entire array to find the target or determine that it's not present.

## Space Complexity
The space complexity is O(1), as the algorithm only uses a constant amount of space to store the pointers and variables, regardless of the input size.

## Key Insight
The key insight is to handle duplicates by incrementing `left` and decrementing `right` when the values at these indices are the same, ensuring that the search space is reduced and the algorithm doesn't get stuck in an infinite loop. This allows the algorithm to efficiently search for the target in the rotated and potentially duplicate-filled array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.5 MB (Beats 67.88%) |
| 📅 Solved | 2026-05-22 |
| 💻 Language | Python |