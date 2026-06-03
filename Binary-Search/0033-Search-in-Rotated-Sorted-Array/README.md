> 📌 **Cross-listed:** Primary location is [Array/0033-Search-in-Rotated-Sorted-Array](../../Array/0033-Search-in-Rotated-Sorted-Array). This problem also appears under: **Array**, **Binary Search**

# 33. Search in Rotated Sorted Array


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)


## 📝 Problem Description

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly left rotated** at an unknown index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of *`target`* if it is in *`nums`*, or *`-1`* if it is not in *`nums`.

You must write an algorithm with `O(log n)` runtime complexity.

 

Example 1:**

```
**Input:** nums = [4,5,6,7,0,1,2], target = 0
**Output:** 4

```
Example 2:**

```
**Input:** nums = [4,5,6,7,0,1,2], target = 3
**Output:** -1

```
Example 3:**

```
**Input:** nums = [1], target = 0
**Output:** -1

```

 

**Constraints:**

	- `1 <= nums.length <= 5000`

	- `-10^4 <= nums[i] <= 10^4`

	- All values of `nums` are **unique**.

	- `nums` is an ascending array that is possibly rotated.

	- `-10^4 <= target <= 10^4`

## 🧠 Solution Explanation

## Intuition
This solution works by utilizing a modified binary search algorithm to find the target element in the rotated sorted array. The key idea is to determine which half of the array is sorted and then decide which half to continue searching in. This approach takes advantage of the fact that the array was initially sorted in ascending order.

## Approach
1. Initialize two pointers, `left` and `right`, to the start and end of the array, respectively.
2. Calculate the middle index `mid` and compare the middle element to the target.
3. If the left half is sorted, check if the target is within the range of the left half. If it is, update `right` to `mid - 1`. Otherwise, update `left` to `mid + 1`.
4. If the left half is not sorted, the right half must be sorted. Check if the target is within the range of the right half. If it is, update `left` to `mid + 1`. Otherwise, update `right` to `mid - 1`.
5. Repeat steps 2-4 until `left` is greater than `right`.

## Time Complexity
The time complexity is O(log n), where n is the number of elements in the array. This is because the algorithm divides the search space in half at each step, similar to a standard binary search.

## Space Complexity
The space complexity is O(1), as the algorithm only uses a constant amount of space to store the pointers and the middle index.

## Key Insight
The key insight that makes this solution work is the ability to determine which half of the array is sorted at each step, allowing the algorithm to efficiently narrow down the search space. This is achieved by comparing the middle element to the left and right elements, and using the fact that the array was initially sorted in ascending order.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 95.99%) |
| 📅 Solved | 2026-05-22 |
| 💻 Language | Python |