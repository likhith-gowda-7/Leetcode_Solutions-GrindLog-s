> 📌 **Cross-listed:** Primary location is [Array/0503-Next-Greater-Element-II](../../Array/0503-Next-Greater-Element-II). This problem also appears under: **Array**, **Stack**, **Monotonic Stack**

# 503. Next Greater Element II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Monotonic Stack](https://img.shields.io/badge/Monotonic%20Stack-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/next-greater-element-ii/)


## 📝 Problem Description

Given a circular integer array `nums` (i.e., the next element of `nums[nums.length - 1]` is `nums[0]`), return *the **next greater number** for every element in* `nums`.

The **next greater number** of a number `x` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return `-1` for this number.

 

Example 1:**

```

**Input:** nums = [1,2,1]
**Output:** [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

```

Example 2:**

```

**Input:** nums = [1,2,3,4,3]
**Output:** [2,3,4,-1,4]

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-10^9 <= nums[i] <= 10^9`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 16 ms (Beats 89.86%) |
| 💾 Memory | 19.6 MB (Beats 100%) |
| 📅 Solved | 2025-02-16 |
| 💻 Language | Python |