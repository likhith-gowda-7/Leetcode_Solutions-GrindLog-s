> 📌 **Cross-listed:** Primary location is [Array/3740-Minimum-Distance-Between-Three-Equal-Elements-I](../../Array/3740-Minimum-Distance-Between-Three-Equal-Elements-I). This problem also appears under: **Array**, **Hash Table**

# 3740. Minimum Distance Between Three Equal Elements I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/)


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

	- `1 <= n == nums.length <= 100`

	- `1 <= nums[i] <= n`

## 🧠 Solution Explanation

**Intuition**
The solution works by first grouping the array elements by their values using a hash table. Then, for each group with at least three elements, it calculates the minimum distance between three distinct indices within the group. The minimum distance is updated if a smaller distance is found.

**Approach**
1. Create a hash table `h1` to store the indices of elements with the same value.
2. Iterate through the input array `nums` and populate the hash table `h1` with the indices of elements with the same value.
3. Iterate through the hash table `h1` and for each group with at least three elements, calculate the minimum distance between three distinct indices within the group.
4. Update the minimum distance `res` if a smaller distance is found.
5. Return the minimum distance `res` if it's not infinity, otherwise return -1.

**Time Complexity**
The time complexity is O(n), where n is the length of the input array `nums`. This is because we iterate through the array once to populate the hash table and then iterate through the hash table once to calculate the minimum distance.

**Space Complexity**
The space complexity is O(n), where n is the length of the input array `nums`. This is because in the worst case, we store all elements in the hash table.

**Key Insight**
The key insight is that we can find the minimum distance between three distinct indices within a group by iterating through the group and calculating the distance for each possible triple of indices. This is because the distance is symmetric, meaning that the order of the indices does not matter.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 66.83%) |
| 💾 Memory | 19.2 MB (Beats 66.75%) |
| 📅 Solved | 2026-04-11 |
| 💻 Language | Python |