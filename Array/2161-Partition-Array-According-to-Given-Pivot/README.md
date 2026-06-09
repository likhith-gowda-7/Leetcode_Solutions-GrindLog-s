# 2161. Partition Array According to Given Pivot


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/partition-array-according-to-given-pivot/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums` and an integer `pivot`. Rearrange `nums` such that the following conditions are satisfied:

	- Every element less than `pivot` appears **before** every element greater than `pivot`.

	- Every element equal to `pivot` appears **in between** the elements less than and greater than `pivot`.

	- The **relative order** of the elements less than `pivot` and the elements greater than `pivot` is maintained.
	
		- More formally, consider every `p_i`, `p_j` where `p_i` is the new position of the `i^th` element and `p_j` is the new position of the `j^th` element. If `i < j` and **both** elements are smaller (*or larger*) than `pivot`, then `p_i < p_j`.

	
	

Return `nums`* after the rearrangement.*

 

Example 1:**

```

**Input:** nums = [9,12,5,10,14,3,10], pivot = 10
**Output:** [9,5,3,10,10,12,14]
**Explanation:** 
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.

```

Example 2:**

```

**Input:** nums = [-3,4,3,2], pivot = 2
**Output:** [-3,2,4,3]
**Explanation:** 
The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^6 <= nums[i] <= 10^6`

	- `pivot` equals to an element of `nums`.

## 🧠 Solution Explanation

**Intuition**
The solution works by first partitioning the input array `nums` into three lists: `less`, `great`, and a counter `c` for the number of elements equal to the `pivot`. Then, it reconstructs the array by concatenating `less`, the `pivot` elements, and `great` in that order.

**Approach**
1. Initialize three variables: `less` to store elements less than the `pivot`, `great` to store elements greater than the `pivot`, and `c` to count the number of elements equal to the `pivot`.
2. Iterate through the input array `nums`. For each element:
   - If the element is less than the `pivot`, append it to `less`.
   - If the element is greater than the `pivot`, append it to `great`.
   - If the element is equal to the `pivot`, increment the counter `c`.
3. Create a new array `res` and concatenate `less`, `c` occurrences of the `pivot`, and `great` in that order.

**Time Complexity**
O(n), where n is the length of the input array `nums`. This is because we make a single pass through the array to partition it and then another pass to reconstruct the array.

**Space Complexity**
O(n), where n is the length of the input array `nums`. This is because in the worst case, we need to store all elements in the `less` and `great` lists.

**Key Insight**
The key insight is to recognize that the problem requires a two-stage approach: first, partitioning the array into three lists, and then reconstructing the array in the desired order. By doing so, we can maintain the relative order of elements less than and greater than the `pivot` while satisfying the given conditions.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 30 ms (Beats 60.88%) |
| 💾 Memory | 34.2 MB (Beats 6.97%) |
| 📅 Solved | 2026-06-08 |
| 💻 Language | Python |