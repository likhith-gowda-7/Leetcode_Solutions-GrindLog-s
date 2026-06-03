# 581. Shortest Unsorted Continuous Subarray


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Stack](https://img.shields.io/badge/Stack-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)


## 📝 Problem Description

Given an integer array `nums`, you need to find one **continuous subarray** such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return *the shortest such subarray and output its length*.

 

Example 1:**

```

**Input:** nums = [2,6,4,8,10,9,15]
**Output:** 5
**Explanation:** You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

```

Example 2:**

```

**Input:** nums = [1,2,3,4]
**Output:** 0

```

Example 3:**

```

**Input:** nums = [1]
**Output:** 0

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-10^5 <= nums[i] <= 10^5`

 

**Follow up:** Can you solve it in `O(n)` time complexity?

## 🧠 Solution Explanation

**Intuition**
The solution works by first sorting the input array and then comparing it with the original array. The goal is to find the shortest subarray that needs to be sorted to make the entire array sorted. This can be achieved by finding the first and last indices where the original array differs from the sorted array.

**Approach**
1. Sort the input array `nums` to get `n1`.
2. Check if the original array is already sorted or has only one element. If so, return 0 as there's no unsorted subarray.
3. Initialize two pointers, `l` and `r`, to the start and end of the array, respectively.
4. Move the pointers towards each other. If the elements at the current positions of the pointers match the corresponding elements in the sorted array, move the pointer towards the center.
5. If the elements at the current positions of the pointers do not match the corresponding elements in the sorted array, it means we've found the first and last indices of the unsorted subarray. Break the loop.
6. Return the length of the unsorted subarray, which is `r - l + 1`.

**Time Complexity**
O(n log n) due to the sorting operation, where n is the length of the input array.

**Space Complexity**
O(n) for the sorting operation, where n is the length of the input array.

**Key Insight**
The key insight is that we can find the shortest unsorted subarray by comparing the original array with its sorted version. By using two pointers to traverse the array, we can efficiently find the first and last indices of the unsorted subarray, which allows us to calculate its length.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 16 ms (Beats 35.76%) |
| 💾 Memory | 18.9 MB (Beats 100%) |
| 📅 Solved | 2025-02-16 |
| 💻 Language | Python |