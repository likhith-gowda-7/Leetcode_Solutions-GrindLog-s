> 📌 **Cross-listed:** Primary location is [Array/0704-Binary-Search](../../Array/0704-Binary-Search). This problem also appears under: **Array**, **Binary Search**

# 704. Binary Search


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/binary-search/)


## 📝 Problem Description

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

 

Example 1:**

```

**Input:** nums = [-1,0,3,5,9,12], target = 9
**Output:** 4
**Explanation:** 9 exists in nums and its index is 4

```

Example 2:**

```

**Input:** nums = [-1,0,3,5,9,12], target = 2
**Output:** -1
**Explanation:** 2 does not exist in nums so return -1

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-10^4 < nums[i], target < 10^4`

	- All the integers in `nums` are **unique**.

	- `nums` is sorted in ascending order.

## 🧠 Solution Explanation

**Intuition**
The solution uses a binary search approach, which is a divide-and-conquer strategy that takes advantage of the sorted array to find the target element in logarithmic time. By repeatedly dividing the search space in half, we can find the target element efficiently.

**Approach**
1. Initialize two pointers, `l` and `r`, to the start and end of the array, respectively.
2. Calculate the middle index `mid` using the formula `(r + l) // 2`.
3. Compare the middle element `n` with the target `target`.
   - If `target` is greater than `n`, move the left pointer `l` to `mid + 1` to search in the right half.
   - If `target` is less than `n`, move the right pointer `r` to `mid - 1` to search in the left half.
   - If `target` is equal to `n`, return the middle index `mid`.
4. Repeat steps 2-3 until `l` is greater than `r`.
5. If the target is not found, return -1.

**Time Complexity**
O(log n), where n is the length of the array. This is because we divide the search space in half at each step, resulting in a logarithmic number of iterations.

**Space Complexity**
O(1), as we only use a constant amount of space to store the pointers and the middle index.

**Key Insight**
The key insight is that by repeatedly dividing the search space in half, we can find the target element in logarithmic time. This is because each iteration reduces the search space by half, resulting in a binary search tree-like structure where each node represents a possible location of the target element.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 18.7 MB (Beats 100%) |
| 📅 Solved | 2025-02-20 |
| 💻 Language | Python |