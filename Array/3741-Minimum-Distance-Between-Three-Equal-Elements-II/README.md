# 3741. Minimum Distance Between Three Equal Elements II


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/)


## 📝 Problem Description

You are given an integer array `nums`.

A tuple `(i, j, k)` of 3 **distinct** indices is **good** if `nums[i] == nums[j] == nums[k]`.

The **distance** of a **good** tuple is `abs(i - j) + abs(j - k) + abs(k - i)`, where `abs(x)` denotes the **absolute value** of `x`.

Return an integer denoting the **minimum** possible **distance** of a **good** tuple. If no **good** tuples exist, return `-1`.

 

Example 1:**

**Input:** nums = [1,2,1,1,3]

**Output:** 6

**Explanation:**

The minimum distance is achieved by the good tuple `(0, 2, 3)`.

`(0, 2, 3)` is a good tuple because `nums[0] == nums[2] == nums[3] == 1`. Its distance is `abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6`.

Example 2:**

**Input:** nums = [1,1,2,3,2,1,2]

**Output:** 8

**Explanation:**

The minimum distance is achieved by the good tuple `(2, 4, 6)`.

`(2, 4, 6)` is a good tuple because `nums[2] == nums[4] == nums[6] == 2`. Its distance is `abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8`.

Example 3:**

**Input:** nums = [1]

**Output:** -1

**Explanation:**

There are no good tuples. Therefore, the answer is -1.

 

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= n`

## 🧠 Solution Explanation

**Intuition**
The solution works by first grouping the elements of the input array by their values. Then, for each group with at least three elements, it calculates the minimum distance between all possible triplets of indices. The minimum distance is updated accordingly.

**Approach**
1. Create a hash table `h1` to store the indices of elements with the same value.
2. Iterate over the input array and populate the hash table `h1`.
3. Iterate over the hash table `h1`. For each group with at least three elements, calculate the minimum distance between all possible triplets of indices.
4. Update the minimum distance `res` accordingly.
5. Return the minimum distance `res` if it is not infinity, otherwise return -1.

**Time Complexity**
O(n + m), where n is the length of the input array and m is the number of unique elements in the array. This is because we iterate over the array once to populate the hash table, and then iterate over the hash table once to calculate the minimum distance.

**Space Complexity**
O(m), where m is the number of unique elements in the array. This is because we store the indices of elements with the same value in the hash table.

**Key Insight**
The key insight is that we only need to consider groups with at least three elements, because for groups with two elements, there is no possible triplet of indices that can form a good tuple. This significantly reduces the number of possible triplets to consider, making the solution more efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 371 ms (Beats 34.92%) |
| 💾 Memory | 50.7 MB (Beats 34.38%) |
| 📅 Solved | 2026-04-11 |
| 💻 Language | Python |