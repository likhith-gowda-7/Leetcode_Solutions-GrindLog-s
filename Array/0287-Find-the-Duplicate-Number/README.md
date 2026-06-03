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

## 🧠 Solution Explanation

## Intuition
This solution works by utilizing Floyd's Tortoise and Hare algorithm, also known as the "cycle detection" algorithm. The idea is to treat the given array as a linked list where each value is a node that points to the index of its value. Since there is a duplicate in the array, this linked list must have a cycle. The algorithm detects this cycle and then finds the starting point of the cycle, which corresponds to the duplicate number.

## Approach
1. Initialize two pointers, `slow` and `fast`, to the start of the array.
2. Move `slow` one step at a time and `fast` two steps at a time until they meet, indicating the presence of a cycle.
3. Reset `slow` to the start and move both `slow` and `fast` one step at a time until they meet again, which will be at the start of the cycle, i.e., the duplicate number.

## Time Complexity
The time complexity is O(n), where n is the number of elements in the array. This is because in the worst-case scenario, the algorithm needs to traverse the entire array to detect the cycle and then find the duplicate number.

## Space Complexity
The space complexity is O(1), which means the space required does not change with the size of the input array, making it constant extra space. This is because the algorithm only uses a fixed amount of space to store the pointers and does not modify the input array.

## Key Insight
The key insight here is recognizing that the given array can be treated as a linked list with a cycle due to the presence of a duplicate number, and applying Floyd's Tortoise and Hare algorithm to detect and find the start of this cycle, which corresponds to the duplicate number.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 24 ms (Beats 67.55%) |
| 💾 Memory | 29.9 MB (Beats 99.98%) |
| 📅 Solved | 2025-04-23 |
| 💻 Language | Python |