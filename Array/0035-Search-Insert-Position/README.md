# 35. Search Insert Position


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/search-insert-position/)


## 📝 Problem Description

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

 

Example 1:**

```

**Input:** nums = [1,3,5,6], target = 5
**Output:** 2

```

Example 2:**

```

**Input:** nums = [1,3,5,6], target = 2
**Output:** 1

```

Example 3:**

```

**Input:** nums = [1,3,5,6], target = 7
**Output:** 4

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-10^4 <= nums[i] <= 10^4`

	- `nums` contains **distinct** values sorted in **ascending** order.

	- `-10^4 <= target <= 10^4`

## 🧠 Solution Explanation

## Intuition
The solution works by utilizing a binary search approach to find the target value in the sorted array. If the target is found, the index is returned; otherwise, the algorithm determines the correct insertion point to maintain the sorted order. This approach takes advantage of the fact that the input array is already sorted, allowing for an efficient search.

## Approach
1. Initialize two pointers, `l` and `r`, to the start and end of the array, respectively.
2. Loop until `l` is greater than `r`.
3. Calculate the midpoint `mid` of the current range `[l, r]`.
4. Compare the value at the midpoint `nums[mid]` with the target value.
5. If `nums[mid]` is less than the target, move the left pointer `l` to `mid + 1`.
6. Otherwise, move the right pointer `r` to `mid - 1`.
7. Once the loop ends, return the left pointer `l`, which represents the index where the target should be inserted to maintain the sorted order.

## Time Complexity
The time complexity is O(log n), where n is the length of the input array. This is because the algorithm divides the search space in half at each step, resulting in a logarithmic number of iterations.

## Space Complexity
The space complexity is O(1), as the algorithm only uses a constant amount of space to store the pointers and the midpoint, regardless of the input size.

## Key Insight
The key insight is that the binary search approach can be modified to find the insertion point of a target value in a sorted array, even if the target is not present. By returning the left pointer `l` after the loop ends, the algorithm effectively determines the correct index where the target should be inserted to maintain the sorted order.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.3 MB (Beats 100%) |
| 📅 Solved | 2025-12-10 |
| 💻 Language | Python |