> 📌 **Cross-listed:** Primary location is [Array/0287-Find-the-Duplicate-Number](../../Array/0287-Find-the-Duplicate-Number). This problem also appears under: **Array**, **Two Pointers**, **Binary Search**, **Bit Manipulation**

# 287. Find the Duplicate Number


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-duplicate-number/)


## 📝 Problem Description

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return *this repeated number*.

You must solve the problem **without** modifying the array `nums` and using only constant extra space.

 

Example 1:**

```

**Input:** nums = [1,3,4,2,2]
**Output:** 2

```

Example 2:**

```

**Input:** nums = [3,1,3,4,2]
**Output:** 3

```

Example 3:**

```

**Input:** nums = [3,3,3,3,3]
**Output:** 3
```

 

**Constraints:**

	- `1 <= n <= 10^5`

	- `nums.length == n + 1`

	- `1 <= nums[i] <= n`

	- All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

 

**Follow up:**

	- How can we prove that at least one duplicate number must exist in `nums`?

	- Can you solve the problem in linear runtime complexity?

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 24 ms (Beats 67.55%) |
| 💾 Memory | 29.9 MB (Beats 99.98%) |
| 📅 Solved | 2025-04-23 |
| 💻 Language | Python |