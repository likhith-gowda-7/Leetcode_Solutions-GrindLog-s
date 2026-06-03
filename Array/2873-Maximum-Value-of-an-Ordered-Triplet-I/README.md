# 2873. Maximum Value of an Ordered Triplet I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums`.

Return ***the maximum value over all triplets of indices*** `(i, j, k)` *such that* `i < j < k`. If all such triplets have a negative value, return `0`.

The **value of a triplet of indices** `(i, j, k)` is equal to `(nums[i] - nums[j]) * nums[k]`.

 

Example 1:**

```

**Input:** nums = [12,6,1,2,7]
**Output:** 77
**Explanation:** The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
It can be shown that there are no ordered triplets of indices with a value greater than 77. 

```

Example 2:**

```

**Input:** nums = [1,10,3,4,19]
**Output:** 133
**Explanation:** The value of the triplet (1, 2, 4) is (nums[1] - nums[2]) * nums[4] = 133.
It can be shown that there are no ordered triplets of indices with a value greater than 133.

```

Example 3:**

```

**Input:** nums = [1,2,3]
**Output:** 0
**Explanation:** The only ordered triplet of indices (0, 1, 2) has a negative value of (nums[0] - nums[1]) * nums[2] = -3. Hence, the answer would be 0.

```

 

**Constraints:**

	- `3 <= nums.length <= 100`

	- `1 <= nums[i] <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining three variables: `max_val`, `max_diff`, and `max_trip`. `max_val` stores the maximum value in the array so far, `max_diff` stores the maximum difference between `max_val` and any other value in the array, and `max_trip` stores the maximum value of a triplet. The solution iterates through the array, updating these variables at each step to ensure that `max_trip` is always the maximum value of a triplet.

**Approach**
1. Initialize `max_val`, `max_diff`, and `max_trip` to 0.
2. Iterate through the array `nums`.
3. For each element `i` in `nums`:
   - Update `max_trip` to be the maximum of its current value and `max_diff * i`.
   - Update `max_val` to be the maximum of its current value and `i`.
   - Update `max_diff` to be the maximum of its current value and `max_val - i`.
4. Return `max_trip`.

**Time Complexity**
The time complexity of this solution is O(n), where n is the number of elements in the array. This is because we are iterating through the array once.

**Space Complexity**
The space complexity of this solution is O(1), which means it uses constant space. This is because we are only using a few variables to store the maximum values and differences.

**Key Insight**
The key insight here is that we can calculate the maximum value of a triplet by maintaining the maximum difference between the maximum value and any other value in the array. This allows us to update the maximum value of a triplet in constant time, resulting in a efficient solution.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-04-03 |
| 💻 Language | Python |