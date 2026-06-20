# 1840. Maximum Building Height


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/maximum-building-height/)


## 📝 Problem Description

You want to build `n` new buildings in a city. The new buildings will be built in a line and are labeled from `1` to `n`.

However, there are city restrictions on the heights of the new buildings:

	- The height of each building must be a non-negative integer.

	- The height of the first building **must** be `0`.

	- The height difference between any two adjacent buildings **cannot exceed** `1`.

Additionally, there are city restrictions on the maximum height of specific buildings. These restrictions are given as a 2D integer array `restrictions` where `restrictions[i] = [id_i, maxHeight_i]` indicates that building `id_i` must have a height **less than or equal to** `maxHeight_i`.

It is guaranteed that each building will appear **at most once** in `restrictions`, and building `1` will **not** be in `restrictions`.

Return *the **maximum possible height** of the **tallest** building*.

 

Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/08/ic236-q4-ex1-1.png)
```

**Input:** n = 5, restrictions = [[2,1],[4,1]]
**Output:** 2
**Explanation:** The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.
```

Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/08/ic236-q4-ex2.png)
```

**Input:** n = 6, restrictions = []
**Output:** 5
**Explanation:** The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,4,5], and the tallest building has a height of 5.

```

Example 3:**

![](https://assets.leetcode.com/uploads/2021/04/08/ic236-q4-ex3.png)
```

**Input:** n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
**Output:** 5
**Explanation:** The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,3,4,4,5,4,3], and the tallest building has a height of 5.

```

 

**Constraints:**

	- `2 <= n <= 10^9`

	- `0 <= restrictions.length <= min(n - 1, 10^5)`

	- `2 <= id_i <= n`

	- `id_i` is **unique**.

	- `0 <= maxHeight_i <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a two-pass approach to find the maximum building height. The first pass calculates the maximum height for each building based on the restrictions from the left, and the second pass calculates the maximum height for each building based on the restrictions from the right. The maximum height is then calculated by considering the maximum height of each building and the distance between them.

**Approach**
1. Initialize an array `arr` with the first building at position 1 with height 0.
2. Add the restrictions to the array `arr`.
3. Sort the array `arr` based on the building positions.
4. Perform a left-to-right pass through the array `arr` to calculate the maximum height for each building based on the restrictions from the left.
5. Perform a right-to-left pass through the array `arr` to calculate the maximum height for each building based on the restrictions from the right.
6. Iterate through the array `arr` to calculate the maximum height by considering the maximum height of each building and the distance between them.
7. Update the maximum height by considering the last building and the remaining distance to the end of the city.

**Time Complexity**
O(n log n) due to the sorting of the array `arr` and the two passes through the array.

**Space Complexity**
O(n) for storing the array `arr` and the restrictions.

**Key Insight**
The key insight is to use a two-pass approach to calculate the maximum height for each building based on the restrictions from both the left and right. This allows us to consider the maximum height of each building and the distance between them to calculate the maximum building height.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 250 ms (Beats 56.82%) |
| 💾 Memory | 45.4 MB (Beats 95.45%) |
| 📅 Solved | 2026-06-20 |
| 💻 Language | Python |