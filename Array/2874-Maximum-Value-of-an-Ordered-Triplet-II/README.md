# 2874. Maximum Value of an Ordered Triplet II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums`.

Return ***the maximum value over all triplets of indices*** `(i, j, k)` *such that* `i < j < k`*. *If all such triplets have a negative value, return `0`.

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

	- `3 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The solution iterates through the array to find the maximum value of all triplets of indices `(i, j, k)` such that `i < j < k`. The key insight is that the maximum value of a triplet is determined by the maximum difference between the smallest and largest elements in the triplet, multiplied by the largest element.

**Approach**
1. Initialize variables `max_val`, `max_diff`, and `max_trip` to keep track of the maximum value, maximum difference, and maximum triplet value respectively.
2. Iterate through the array `nums` and for each element `i`:
   1. Update `max_trip` to be the maximum of its current value and `max_diff * i`.
   2. Update `max_val` to be the maximum of its current value and `i`.
   3. Update `max_diff` to be the maximum of its current value and `max_val - i`.
3. Return `max_trip` as the maximum value of all triplets.

**Time Complexity**
O(n), where n is the length of the array `nums`. This is because we are iterating through the array once.

**Space Complexity**
O(1), as we are using a constant amount of space to store the variables `max_val`, `max_diff`, and `max_trip`.

**Key Insight**
The solution works by maintaining the maximum difference between the smallest and largest elements in the triplet, and multiplying it by the largest element to get the maximum value of the triplet. This approach ensures that we consider all possible triplets and find the maximum value.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 164 ms (Beats 24.87%) |
| 💾 Memory | 29.3 MB (Beats 100%) |
| 📅 Solved | 2025-04-03 |
| 💻 Language | Python |