> 📌 **Cross-listed:** Primary location is [Array/3195-Find-the-Minimum-Area-to-Cover-All-Ones-I](../../Array/3195-Find-the-Minimum-Area-to-Cover-All-Ones-I). This problem also appears under: **Array**, **Matrix**

# 3195. Find the Minimum Area to Cover All Ones I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/)


## 📝 Problem Description

You are given a 2D **binary** array `grid`. Find a rectangle with horizontal and vertical sides with the** smallest** area, such that all the 1's in `grid` lie inside this rectangle.

Return the **minimum** possible area of the rectangle.

 

Example 1:**

**Input:** grid = [[0,1,0],[1,0,1]]

**Output:** 6

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/05/08/examplerect0.png)

The smallest rectangle has a height of 2 and a width of 3, so it has an area of `2 * 3 = 6`.

Example 2:**

**Input:** grid = [[1,0],[0,0]]

**Output:** 1

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/05/08/examplerect1.png)

The smallest rectangle has both height and width 1, so its area is `1 * 1 = 1`.

 

**Constraints:**

	- `1 <= grid.length, grid[i].length <= 1000`

	- `grid[i][j]` is either 0 or 1.

	- The input is generated such that there is at least one 1 in `grid`.

## 🧠 Solution Explanation

**Intuition**
The solution works by finding the topmost and bottommost rows, and the leftmost and rightmost columns that contain at least one '1' in the grid. The minimum area rectangle is then determined by the height and width of this bounding box.

**Approach**
1. Initialize variables `up` and `down` to `None`, which will store the indices of the topmost and bottommost rows containing '1's, respectively.
2. Iterate through the grid from top to bottom, and for each cell, check if it's a '1'. If it's the first '1' encountered (`up` is `None`), update `up` to its row index. If it's a '1' in the bottom row (`d = m - (r + 1)`), update `down` to its row index if `down` is `None`.
3. If both `up` and `down` are not `None`, break out of the loop as we've found the topmost and bottommost rows.
4. Repeat steps 1-3 for the columns, initializing `left` and `right` to `None`, and updating them to the indices of the leftmost and rightmost columns containing '1's, respectively.
5. Calculate the height and width of the bounding box as `height = (down - up) + 1` and `width = (right - left) + 1`, respectively.
6. Return the product of the height and width as the minimum area.

**Time Complexity**
O(m*n), where m is the number of rows and n is the number of columns in the grid. This is because we're iterating through the grid twice, once for rows and once for columns.

**Space Complexity**
O(1), as we're only using a constant amount of space to store the indices of the topmost and bottommost rows and columns.

**Key Insight**
The key insight is that the minimum area rectangle must contain the topmost and bottommost rows, and the leftmost and rightmost columns that contain at least one '1'. By finding these indices, we can determine the height and width of the bounding box, and thus the minimum area.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 2571 ms (Beats 6.35%) |
| 💾 Memory | 47.4 MB (Beats 100%) |
| 📅 Solved | 2025-08-22 |
| 💻 Language | Python |