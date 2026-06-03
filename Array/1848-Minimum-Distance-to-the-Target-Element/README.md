# 1848. Minimum Distance to the Target Element


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-distance-to-the-target-element/)


## 📝 Problem Description

Given an integer array `nums` **(0-indexed)** and two integers `target` and `start`, find an index `i` such that `nums[i] == target` and `abs(i - start)` is **minimized**. Note that `abs(x)` is the absolute value of `x`.

Return `abs(i - start)`.

It is **guaranteed** that `target` exists in `nums`.

 

Example 1:**

```

**Input:** nums = [1,2,3,4,5], target = 5, start = 3
**Output:** 1
**Explanation:** nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.

```

Example 2:**

```

**Input:** nums = [1], target = 1, start = 0
**Output:** 0
**Explanation:** nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.

```

Example 3:**

```

**Input:** nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
**Output:** 0
**Explanation:** Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.

```

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 10^4`

	- `0 <= start < nums.length`

	- `target` is in `nums`.

## 🧠 Solution Explanation

**Intuition**
This solution works by iterating through the array and keeping track of the minimum distance found so far between the target element and the start index. The key insight is that we only need to find the first occurrence of the target element, as it is guaranteed to exist in the array.

**Approach**
1. Initialize `mini` to the length of the array, which will store the minimum distance found so far.
2. Iterate through the array using `enumerate`, which provides both the index `i` and the value `val` at each position.
3. Check if the current value `val` is equal to the target element. If it is, update `mini` to be the minimum of its current value and the absolute difference between the current index `i` and the start index.
4. After iterating through the entire array, return the value of `mini`, which represents the minimum distance found.

**Time Complexity**
O(n), where n is the length of the array. This is because we are iterating through the array once.

**Space Complexity**
O(1), as we are only using a constant amount of space to store the minimum distance `mini` and the start index.

**Key Insight**
The key insight is that we only need to find the first occurrence of the target element, as it is guaranteed to exist in the array. This allows us to stop iterating as soon as we find the target element, making the solution efficient even for large arrays.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.4 MB (Beats 14.29%) |
| 📅 Solved | 2026-04-13 |
| 💻 Language | Python |