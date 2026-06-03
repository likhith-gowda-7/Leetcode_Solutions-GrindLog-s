# 1413. Minimum Value to Get Positive Step by Step Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/)


## 📝 Problem Description

Given an array of integers `nums`, you start with an initial **positive** value *startValue**.*

In each iteration, you calculate the step by step sum of *startValue* plus elements in `nums` (from left to right).

Return the minimum **positive** value of *startValue* such that the step by step sum is never less than 1.

 

Example 1:**

```

**Input:** nums = [-3,2,-3,4,2]
**Output:** 5
**Explanation: **If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
**step by step sum**
**startValue = 4 | startValue = 5 | nums**
  (4 **-3** ) = 1  | (5 **-3** ) = 2    |  -3
  (1 **+2** ) = 3  | (2 **+2** ) = 4    |   2
  (3 **-3** ) = 0  | (4 **-3** ) = 1    |  -3
  (0 **+4** ) = 4  | (1 **+4** ) = 5    |   4
  (4 **+2** ) = 6  | (5 **+2** ) = 7    |   2

```

Example 2:**

```

**Input:** nums = [1,2]
**Output:** 1
**Explanation:** Minimum start value should be positive. 

```

Example 3:**

```

**Input:** nums = [1,-2,-3]
**Output:** 5

```

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `-100 <= nums[i] <= 100`

## 🧠 Solution Explanation

**Intuition**
The key insight here is that we need to find the minimum positive value of `startValue` such that the step-by-step sum is never less than 1. This can be achieved by finding the minimum sum of the array and then subtracting it from 1, since we want the sum to be at least 1.

**Approach**
1. Initialize `min_sum` to 0, which will store the minimum sum of the array.
2. Initialize `curr` to 0, which will store the current sum of the array.
3. Iterate over the array `nums` from left to right.
4. In each iteration, add the current number to `curr`.
5. Update `min_sum` to be the minimum of its current value and `curr`.
6. After iterating over the entire array, return `1 - min_sum`.

**Time Complexity**
The time complexity of this solution is O(n), where n is the length of the array `nums`. This is because we are iterating over the array once.

**Space Complexity**
The space complexity of this solution is O(1), since we are using a constant amount of space to store `min_sum` and `curr`.

**Key Insight**
The key insight here is that we can find the minimum positive value of `startValue` by finding the minimum sum of the array and then subtracting it from 1. This is because the step-by-step sum is the sum of `startValue` and the array elements, and we want this sum to be at least 1. Therefore, we can find the minimum positive value of `startValue` by finding the minimum sum of the array and then subtracting it from 1.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17 MB (Beats 100%) |
| 📅 Solved | 2024-12-13 |
| 💻 Language | Python |