# 643. Maximum Average Subarray I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/)


## 📝 Problem Description

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose **length is equal to** `k` that has the maximum average value and return *this value*. Any answer with a calculation error less than `10^-5` will be accepted.

 

Example 1:**

```

**Input:** nums = [1,12,-5,-6,50,3], k = 4
**Output:** 12.75000
**Explanation:** Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

```

Example 2:**

```

**Input:** nums = [5], k = 1
**Output:** 5.00000

```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= k <= n <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 80 ms (Beats 28.27%) |
| 💾 Memory | 27.4 MB (Beats 100%) |
| 📅 Solved | 2025-03-04 |
| 💻 Language | Python |