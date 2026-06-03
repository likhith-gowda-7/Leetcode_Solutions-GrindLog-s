# 977. Squares of a Sorted Array


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/)


## 📝 Problem Description

Given an integer array `nums` sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

 

Example 1:**

```

**Input:** nums = [-4,-1,0,3,10]
**Output:** [0,1,9,16,100]
**Explanation:** After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

```

Example 2:**

```

**Input:** nums = [-7,-3,2,3,11]
**Output:** [4,9,9,49,121]

```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-10^4 <= nums[i] <= 10^4`

	- `nums` is sorted in **non-decreasing** order.

 

**Follow up:** Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

## 🧠 Solution Explanation

**Intuition**
The key insight here is to take advantage of the fact that the input array is sorted in non-decreasing order. We can use two pointers, one at the start and one at the end of the array, to efficiently find the largest absolute value and square it, then move the corresponding pointer towards the center.

**Approach**
1. Initialize an empty result array `res` of the same length as the input array `nums`.
2. Initialize two pointers, `l` at the start and `r` at the end of `nums`.
3. Iterate from the end of `nums` to the start, keeping track of the current index `i`.
4. At each iteration, compare the absolute values of `nums[l]` and `nums[r]`.
5. If `abs(nums[l])` is larger, square `nums[l]` and move `l` one step forward.
6. Otherwise, square `nums[r]` and move `r` one step backward.
7. Store the squared value at the current index `i` in `res`.
8. Repeat steps 4-7 until the entire `res` array is filled.

**Time Complexity**
O(n), where n is the length of the input array `nums`. This is because we only need to iterate through the array once, and each operation (comparing, squaring, and storing) takes constant time.

**Space Complexity**
O(n), where n is the length of the input array `nums`. This is because we need to create a new array `res` of the same length as `nums` to store the squared values.

**Key Insight**
The key to this solution is to use two pointers, one at the start and one at the end of the array, to efficiently find the largest absolute value and square it. This approach takes advantage of the fact that the input array is sorted in non-decreasing order, allowing us to find the largest absolute value in O(1) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 9 ms (Beats 65.6%) |
| 💾 Memory | 19.5 MB (Beats 100%) |
| 📅 Solved | 2025-01-23 |
| 💻 Language | Python |