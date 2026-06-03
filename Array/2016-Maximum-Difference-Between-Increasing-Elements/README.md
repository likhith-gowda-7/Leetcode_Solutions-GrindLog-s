# 2016. Maximum Difference Between Increasing Elements


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)


## 📝 Problem Description

Given a **0-indexed** integer array `nums` of size `n`, find the **maximum difference** between `nums[i]` and `nums[j]` (i.e., `nums[j] - nums[i]`), such that `0 <= i < j < n` and `nums[i] < nums[j]`.

Return *the **maximum difference**. *If no such `i` and `j` exists, return `-1`.

 

Example 1:**

```

**Input:** nums = [7,**1**,**5**,4]
**Output:** 4
**Explanation:**
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

```

Example 2:**

```

**Input:** nums = [9,4,3,2]
**Output:** -1
**Explanation:**
There is no i and j such that i < j and nums[i] < nums[j].

```

Example 3:**

```

**Input:** nums = [**1**,5,2,**10**]
**Output:** 9
**Explanation:**
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.

```

 

**Constraints:**

	- `n == nums.length`

	- `2 <= n <= 1000`

	- `1 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by maintaining a running minimum value (`take`) and a maximum difference (`maxi`). As we iterate through the array, we update `take` to be the minimum of its current value and the current element, and we update `maxi` to be the maximum of its current value and the difference between the current element and `take`. This way, we ensure that `take` is always less than or equal to the current element, and `maxi` is the maximum difference between the current element and any previous element that was smaller.

**Approach**
1. Initialize `take` to the first element of the array and `maxi` to -1.
2. Iterate through the array from the second element to the end.
3. For each element, calculate the difference between the current element and `take`.
4. Update `take` to be the minimum of its current value and the current element.
5. Update `maxi` to be the maximum of its current value and the difference calculated in step 3.
6. After iterating through the entire array, return `maxi` if it is not -1, otherwise return -1.

**Time Complexity**
O(n), where n is the length of the array. This is because we are iterating through the array once.

**Space Complexity**
O(1), because we are using a constant amount of space to store `take` and `maxi`.

**Key Insight**
The key insight is that by maintaining a running minimum value (`take`), we can ensure that we are always considering the maximum difference between the current element and any previous element that was smaller. This allows us to efficiently find the maximum difference in a single pass through the array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-06-16 |
| 💻 Language | Python |