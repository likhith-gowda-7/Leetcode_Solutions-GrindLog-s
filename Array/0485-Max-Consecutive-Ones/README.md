# 485. Max Consecutive Ones


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/max-consecutive-ones/)


## 📝 Problem Description

Given a binary array `nums`, return *the maximum number of consecutive *`1`*'s in the array*.

 

Example 1:**

```

**Input:** nums = [1,1,0,1,1,1]
**Output:** 3
**Explanation:** The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

```

Example 2:**

```

**Input:** nums = [1,0,1,1,0,1]
**Output:** 2

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `nums[i]` is either `0` or `1`.

## 🧠 Solution Explanation

**Intuition**
The key insight here is that we can keep track of the maximum number of consecutive ones seen so far and the current number of consecutive ones. When we encounter a zero, we update the maximum and reset the current count. This way, we can efficiently find the maximum number of consecutive ones in the array.

**Approach**
1. Initialize two variables: `maxi` to store the maximum number of consecutive ones seen so far, and `curr` to store the current number of consecutive ones.
2. Iterate through the input array `nums`.
3. If the current element `n` is 1, increment `curr`.
4. If the current element `n` is 0, update `maxi` with the maximum of its current value and `curr`, then reset `curr` to 0.
5. After iterating through the entire array, update `maxi` with the maximum of its current value and `curr` (in case the last element is 1).
6. Return `maxi` as the maximum number of consecutive ones.

**Time Complexity**
O(n), where n is the length of the input array `nums`. This is because we only iterate through the array once.

**Space Complexity**
O(1), since we only use a constant amount of space to store the `maxi` and `curr` variables.

**Key Insight**
The key to this solution is to keep track of the current number of consecutive ones (`curr`) and the maximum number of consecutive ones seen so far (`maxi`). By resetting `curr` whenever we encounter a zero, we can efficiently find the maximum number of consecutive ones in the array.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 10 ms (Beats 87.58%) |
| 💾 Memory | 20.3 MB (Beats 100%) |
| 📅 Solved | 2025-11-14 |
| 💻 Language | Python |