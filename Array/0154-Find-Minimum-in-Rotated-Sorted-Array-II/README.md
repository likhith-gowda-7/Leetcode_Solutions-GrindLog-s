# 154. Find Minimum in Rotated Sorted Array II


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)


## 📝 Problem Description

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,4,4,5,6,7]` might become:

	- `[4,5,6,7,0,1,4]` if it was rotated `4` times.

	- `[0,1,4,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` that may contain **duplicates**, return *the minimum element of this array*.

You must decrease the overall operation steps as much as possible.

 

Example 1:**

```
**Input:** nums = [1,3,5]
**Output:** 1

```
Example 2:**

```
**Input:** nums = [2,2,2,0,1]
**Output:** 0

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 5000`

	- `-5000 <= nums[i] <= 5000`

	- `nums` is sorted and rotated between `1` and `n` times.

 

**Follow up:** This problem is similar to [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/), but `nums` may contain **duplicates**. Would this affect the runtime complexity? How and why?

## 🧠 Solution Explanation

## Intuition
This approach works by utilizing a modified binary search algorithm to find the minimum element in a rotated sorted array that may contain duplicates. The key idea is to handle duplicates by skipping over them and then applying the standard binary search logic. The algorithm iteratively narrows down the search space until it finds the minimum element.

## Approach
1. Initialize two pointers, `l` and `r`, to the start and end of the array, respectively, and a variable `mini` to store the minimum element found so far.
2. Skip over any duplicate elements at the start and end of the current search space.
3. Calculate the midpoint `mid` of the current search space.
4. Compare the elements at `l` and `mid` to determine which half of the search space the minimum element is likely to be in.
5. Update the `mini` variable and adjust the search space accordingly.

## Time Complexity
The time complexity is O(n) in the worst case, where n is the number of elements in the array. This occurs when the array is filled with duplicates, and the algorithm has to iterate over the entire array to find the minimum element.

## Space Complexity
The space complexity is O(1), as the algorithm only uses a constant amount of space to store the pointers and the minimum element.

## Key Insight
The key insight behind this solution is the way it handles duplicates by skipping over them before applying the standard binary search logic. This allows the algorithm to efficiently find the minimum element in a rotated sorted array with duplicates, even in the worst-case scenario where the array is filled with duplicates.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.6 MB (Beats 58.74%) |
| 📅 Solved | 2026-05-16 |
| 💻 Language | Python |