> 📌 **Cross-listed:** Primary location is [Array/3206-Alternating-Groups-I](../../Array/3206-Alternating-Groups-I). This problem also appears under: **Array**, **Sliding Window**

# 3206. Alternating Groups I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/alternating-groups-i/)


## 📝 Problem Description

There is a circle of red and blue tiles. You are given an array of integers `colors`. The color of tile `i` is represented by `colors[i]`:

	- `colors[i] == 0` means that tile `i` is **red**.

	- `colors[i] == 1` means that tile `i` is **blue**.

Every 3 contiguous tiles in the circle with **alternating** colors (the middle tile has a different color from its **left** and **right** tiles) is called an **alternating** group.

Return the number of **alternating** groups.

**Note** that since `colors` represents a **circle**, the **first** and the **last** tiles are considered to be next to each other.

 

Example 1:**

**Input:** colors = [1,1,1]

**Output:** 0

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-53-171.png)

Example 2:**

**Input:** colors = [0,1,0,0,1]

**Output:** 3

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-47-491.png)

Alternating groups:

![](https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-50-441.png)**![](https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-48-211.png)![](https://assets.leetcode.com/uploads/2024/05/16/image_2024-05-16_23-49-351.png)**

 

**Constraints:**

	- `3 <= colors.length <= 100`

	- `0 <= colors[i] <= 1`

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 50 ms (Beats 95.89%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-03-09 |
| 💻 Language | Python |