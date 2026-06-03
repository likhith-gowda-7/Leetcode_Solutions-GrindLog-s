> 📌 **Cross-listed:** Primary location is [Array/0812-Largest-Triangle-Area](../../Array/0812-Largest-Triangle-Area). This problem also appears under: **Array**, **Math**, **Geometry**

# 812. Largest Triangle Area


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Geometry](https://img.shields.io/badge/Geometry-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/largest-triangle-area/)


## 📝 Problem Description

Given an array of points on the **X-Y** plane `points` where `points[i] = [x_i, y_i]`, return *the area of the largest triangle that can be formed by any three different points*. Answers within `10^-5` of the actual answer will be accepted.

 

Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png)
```

**Input:** points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
**Output:** 2.00000
**Explanation:** The five points are shown in the above figure. The red triangle is the largest.

```

Example 2:**

```

**Input:** points = [[1,0],[0,0],[0,1]]
**Output:** 0.50000

```

 

**Constraints:**

	- `3 <= points.length <= 50`

	- `-50 <= x_i, y_i <= 50`

	- All the given points are **unique**.

## 🧠 Solution Explanation

**Intuition**
The solution uses the shoelace formula to calculate the area of each triangle formed by three points and keeps track of the maximum area found. This approach works because the shoelace formula can be used to calculate the area of a simple polygon, and a triangle is a special case of a simple polygon.

**Approach**
1. Initialize the maximum area to 0.
2. Iterate over all possible combinations of three points from the input array.
3. For each combination of three points, calculate the area of the triangle formed by these points using the shoelace formula.
4. Update the maximum area if the calculated area is greater than the current maximum area.
5. After iterating over all combinations, return the maximum area found.

**Time Complexity**
O(n^3), where n is the number of points. This is because we have three nested loops, each iterating over the points array.

**Space Complexity**
O(1), as we only use a constant amount of space to store the maximum area and the temporary variables used in the shoelace formula.

**Key Insight**
The key insight here is that the shoelace formula can be used to calculate the area of a triangle formed by three points, and by iterating over all possible combinations of three points, we can find the maximum area of the triangle that can be formed. This approach is efficient because it only requires a constant amount of space and has a time complexity that is cubic in the number of points.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 49 ms (Beats 28.84%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-09-27 |
| 💻 Language | Python |