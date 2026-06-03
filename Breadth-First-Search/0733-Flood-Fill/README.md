> 📌 **Cross-listed:** Primary location is [Array/0733-Flood-Fill](../../Array/0733-Flood-Fill). This problem also appears under: **Array**, **Depth-First Search**, **Breadth-First Search**, **Matrix**

# 733. Flood Fill


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Depth-First Search](https://img.shields.io/badge/Depth--First%20Search-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/flood-fill/)


## 📝 Problem Description

You are given an image represented by an `m x n` grid of integers `image`, where `image[i][j]` represents the pixel value of the image. You are also given three integers `sr`, `sc`, and `color`. Your task is to perform a **flood fill** on the image starting from the pixel `image[sr][sc]`.

To perform a **flood fill**:

	- Begin with the starting pixel and change its color to `color`.

	- Perform the same process for each pixel that is **directly adjacent** (pixels that share a side with the original pixel, either horizontally or vertically) and shares the **same color** as the starting pixel.

	- Keep **repeating** this process by checking neighboring pixels of the *updated* pixels and modifying their color if it matches the original color of the starting pixel.

	- The process **stops** when there are **no more** adjacent pixels of the original color to update.

Return the **modified** image after performing the flood fill.

 

Example 1:**

**Input:** image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

**Output:** [[2,2,2],[2,2,0],[2,0,1]]

**Explanation:**

![](https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg)

From the center of the image with position `(sr, sc) = (1, 1)` (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is **not** colored 2, because it is not horizontally or vertically connected to the starting pixel.

Example 2:**

**Input:** image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

**Output:** [[0,0,0],[0,0,0]]

**Explanation:**

The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

 

**Constraints:**

	- `m == image.length`

	- `n == image[i].length`

	- `1 <= m, n <= 50`

	- `0 <= image[i][j], color < 2^16`

	- `0 <= sr < m`

	- `0 <= sc < n`

## 🧠 Solution Explanation

**Intuition**
The flood fill algorithm works by performing a breadth-first search (BFS) from the starting pixel, changing the color of adjacent pixels that match the original color, and repeating this process until all reachable pixels have been updated.

**Approach**
1. Initialize variables to store the number of rows (`m`) and columns (`n`) in the image, as well as the starting pixel's color (`st_color`).
2. Define a helper function `check` to verify if a pixel is within the image boundaries, has the same color as the starting pixel, and has not been updated yet.
3. Create a queue (`q`) to store pixels to be processed and add the starting pixel to it.
4. Update the starting pixel's color to the target color (`color`).
5. While the queue is not empty, pop the next pixel from the queue and iterate over its adjacent pixels.
6. For each adjacent pixel, check if it is valid using the `check` function. If it is, update its color to the target color and add it to the queue.
7. Repeat step 5 until the queue is empty.

**Time Complexity**
O(m \* n) because in the worst case, we need to visit every pixel in the image.

**Space Complexity**
O(m \* n) due to the use of a queue to store pixels to be processed, which can grow up to the size of the image in the worst case.

**Key Insight**
The key insight here is to use a BFS approach to efficiently update all reachable pixels in the image, rather than using a recursive approach that could lead to stack overflow errors for large images.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.9 MB (Beats 100%) |
| 📅 Solved | 2025-09-07 |
| 💻 Language | Python |