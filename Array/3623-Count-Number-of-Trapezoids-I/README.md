# 3623. Count Number of Trapezoids I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Geometry](https://img.shields.io/badge/Geometry-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-number-of-trapezoids-i/)


## 📝 Problem Description

You are given a 2D integer array `points`, where `points[i] = [x_i, y_i]` represents the coordinates of the `i^th` point on the Cartesian plane.

A **horizontal** **trapezoid** is a convex quadrilateral with at least one pair** of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the  number of unique ****horizontal* *trapezoids*** that can be formed by choosing any four distinct points from `points`.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

 

Example 1:**

**Input:** points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

**Output:** 3

**Explanation:**

![](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-6.png) ![](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-7.png) ![](https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-8.png)

There are three distinct ways to pick four points that form a horizontal trapezoid:

	Using points [1,0]`, [2,0]`, [3,2]`, and [2,2]`.

	Using points [2,0]`, [3,0]`, [3,2]`, and [2,2]`.

	Using points [1,0]`, [3,0]`, [3,2]`, and [2,2]`.

Example 2:**

**Input:** points = [[0,0],[1,0],[0,1],[2,1]]

**Output:** 1

**Explanation:**

![](https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-5.png)

There is only one horizontal trapezoid that can be formed.

 

**Constraints:**

	- `4 <= points.length <= 10^5`

	- `&ndash;10^8 <= x_i, y_i <= 10^8`

	- All points are pairwise distinct.

## 🧠 Solution Explanation

**Intuition**
The solution uses a hash table to count the number of points at each y-coordinate. It then iterates over the y-coordinates, calculating the number of horizontal lines (i.e., pairs of points with the same y-coordinate) and the number of trapezoids that can be formed using these lines. The key insight is that each pair of horizontal lines can form multiple trapezoids, and the number of trapezoids formed by a pair of lines is proportional to the number of points above and below the lines.

**Approach**
1. Create a hash table `coord_points` to store the number of points at each y-coordinate.
2. Iterate over the points and update the hash table accordingly.
3. Initialize variables `prev` and `res` to keep track of the total number of horizontal lines and the total number of trapezoids, respectively.
4. Iterate over the y-coordinates in the hash table, calculating the number of horizontal lines `horizontal_lines` that can be formed using the points at the current y-coordinate.
5. Update the total number of trapezoids `res` by adding the product of `horizontal_lines` and `prev`, which represents the number of trapezoids that can be formed using the current pair of horizontal lines and all previous pairs.
6. Update `prev` by adding `horizontal_lines`, which represents the number of new horizontal lines that can be formed using the points at the current y-coordinate.
7. Return the total number of trapezoids modulo `10^9 + 7`.

**Time Complexity**
O(n), where n is the number of points. This is because we iterate over the points once to populate the hash table, and then iterate over the y-coordinates in the hash table once to calculate the number of trapezoids.

**Space Complexity**
O(n), where n is the number of points. This is because we store the number of points at each y-coordinate in the hash table.

**Key Insight**
The key insight is that each pair of horizontal lines can form multiple trapezoids, and the number of trapezoids formed by a pair of lines is proportional to the number of points above and below the lines. This allows us to calculate the total number of trapezoids by iterating over the y-coordinates and updating the total number of trapezoids accordingly.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 71 ms (Beats 70%) |
| 💾 Memory | 63.4 MB (Beats 100%) |
| 📅 Solved | 2025-12-02 |
| 💻 Language | Python |