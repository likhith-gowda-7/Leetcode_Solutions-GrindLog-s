> 📌 **Cross-listed:** Primary location is [Array/0162-Find-Peak-Element](../../Array/0162-Find-Peak-Element). This problem also appears under: **Array**, **Binary Search**

# 162. Find Peak Element


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-peak-element/)


## 📝 Problem Description

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -&infin;`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

 

Example 1:**

```

**Input:** nums = [1,2,3,1]
**Output:** 2
**Explanation:** 3 is a peak element and your function should return the index number 2.
```

Example 2:**

```

**Input:** nums = [1,2,1,3,5,6,4]
**Output:** 5
**Explanation:** Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `-2^31 <= nums[i] <= 2^31 - 1`

	- `nums[i] != nums[i + 1]` for all valid `i`.

## 🧠 Solution Explanation

## Intuition
The solution works by utilizing a modified binary search algorithm to find a peak element in the given array. This approach takes advantage of the fact that a peak element must exist in the array, given the constraints that `nums[-1] = nums[n] = -∞`. By repeatedly dividing the search space in half, we can efficiently locate a peak element.

## Approach
1. Initialize two pointers, `l` and `r`, to the start and end of the array, respectively.
2. Loop until `l` and `r` converge.
3. Calculate the midpoint `mid` of the current search space.
4. Compare the value of `nums[mid]` with `nums[mid+1]`.
5. If `nums[mid]` is greater than `nums[mid+1]`, update `r` to `mid`, as the peak element must be in the left half.
6. Otherwise, update `l` to `mid+1`, as the peak element must be in the right half.
7. Once `l` and `r` converge, return `l` as the index of a peak element.

## Time Complexity
The time complexity is O(log n), where n is the number of elements in the array. This is because the algorithm divides the search space in half at each iteration, resulting in a logarithmic number of steps.

## Space Complexity
The space complexity is O(1), as the algorithm only uses a constant amount of space to store the pointers and midpoint.

## Key Insight
The key insight behind this solution is the realization that a peak element must exist in the array, and that by comparing adjacent elements, we can determine which half of the search space to focus on. This allows us to efficiently locate a peak element using a modified binary search algorithm.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-02-24 |
| 💻 Language | Python |