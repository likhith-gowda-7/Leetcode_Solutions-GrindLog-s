# 836. Rectangle Overlap


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Geometry](https://img.shields.io/badge/Geometry-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rectangle-overlap/)


## 📝 Problem Description

An axis-aligned rectangle is represented as a list `[x1, y1, x2, y2]`, where `(x1, y1)` is the coordinate of its bottom-left corner, and `(x2, y2)` is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is **positive**. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles `rec1` and `rec2`, return `true`* if they overlap, otherwise return *`false`.

 

Example 1:**

```
**Input:** rec1 = [0,0,2,2], rec2 = [1,1,3,3]
**Output:** true

```
Example 2:**

```
**Input:** rec1 = [0,0,1,1], rec2 = [1,0,2,1]
**Output:** false

```
Example 3:**

```
**Input:** rec1 = [0,0,1,1], rec2 = [2,2,3,3]
**Output:** false

```

 

**Constraints:**

	- `rec1.length == 4`

	- `rec2.length == 4`

	- `-10^9 <= rec1[i], rec2[i] <= 10^9`

	- `rec1` and `rec2` represent a valid rectangle with a non-zero area.

## 🧠 Solution Explanation

**Intuition**  
For two axis‑aligned rectangles to overlap, their projections on both the X‑axis and Y‑axis must overlap with a positive length. If either projection has zero or negative length, the rectangles only touch or are disjoint.

**Approach**  
1. Compute the horizontal overlap:  
   `width = min(rec1.x2, rec2.x2) – max(rec1.x1, rec2.x1)`.  
2. Compute the vertical overlap:  
   `height = min(rec1.y2, rec2.y2) – max(rec1.y1, rec2.y1)`.  
3. If both `width` and `height` are strictly greater than zero, the rectangles share a positive‑area intersection; return `True`.  
   Otherwise return `False`.

**Time Complexity**  
O(1). The algorithm performs a constant number of arithmetic operations regardless of input size.

**Space Complexity**  
O(1). Only a few integer variables are used; no additional data structures are allocated.

**Key Insight**  
Overlap exists iff the intervals on both axes overlap with positive length. Checking the signed difference between the max of left edges and min of right edges (and similarly for y) captures this condition in a single comparison.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.3 MB (Beats 60.13%) |
| 📅 Solved | 2026-09-14 |
| 💻 Language | Python |