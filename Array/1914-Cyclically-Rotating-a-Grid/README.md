# 1914. Cyclically Rotating a Grid


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Matrix](https://img.shields.io/badge/Matrix-purple) ![Simulation](https://img.shields.io/badge/Simulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/cyclically-rotating-a-grid/)


## 📝 Problem Description

You are given an `m x n` integer matrix `grid`​​​, where `m` and `n` are both **even** integers, and an integer `k`.



The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:



![](https://assets.leetcode.com/uploads/2021/06/10/ringofgrid.png)



A cyclic rotation of the matrix is done by cyclically rotating **each layer** in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the **counter-clockwise** direction. An example rotation is shown below:


![](https://assets.leetcode.com/uploads/2021/06/22/explanation_grid.jpg)
Return *the matrix after applying *`k` *cyclic rotations to it*.



 


Example 1:**


![](https://assets.leetcode.com/uploads/2021/06/19/rod2.png)
```

**Input:** grid = [[40,10],[30,20]], k = 1
**Output:** [[10,20],[40,30]]
**Explanation:** The figures above represent the grid at every state.

```


Example 2:**


**![](https://assets.leetcode.com/uploads/2021/06/10/ringofgrid5.png)** **![](https://assets.leetcode.com/uploads/2021/06/10/ringofgrid6.png)** **![](https://assets.leetcode.com/uploads/2021/06/10/ringofgrid7.png)**

```

**Input:** grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
**Output:** [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
**Explanation:** The figures above represent the grid at every state.

```


 


**Constraints:**




	- `m == grid.length`

	- `n == grid[i].length`

	- `2 <= m, n <= 50`

	- Both `m` and `n` are **even** integers.

	- `1 <= grid[i][j] <=^ 5000`

	- `1 <= k <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by iterating over each layer of the grid, rotating it, and then moving on to the next layer. The key insight is to treat each layer as a ring and rotate it by moving elements in a counter-clockwise direction.

**Approach**
1. Initialize variables to keep track of the top, left, bottom, and right boundaries of the grid.
2. While there are still layers to process (i.e., top < bottom and left < right):
   1. Calculate the length and width of the current layer.
   2. Calculate the perimeter of the layer.
   3. Calculate the number of rotations needed for the current layer (k % perimeter).
   4. While there are still rotations needed:
      1. Save the top-left element of the layer.
      2. Shift all elements in the top row to the left.
      3. Shift all elements in the right column up.
      4. Shift all elements in the bottom row to the right.
      5. Shift all elements in the left column down.
      6. Place the saved top-left element in its new position.
      7. Decrement the number of rotations needed.
   5. Move to the next layer by incrementing top and left, and decrementing bottom and right.
3. Return the rotated grid.

**Time Complexity**
O(m*n) where m and n are the dimensions of the grid. This is because each element in the grid is visited at most once.

**Space Complexity**
O(1) as we only use a constant amount of space to store the variables and do not use any additional data structures that scale with the input size.

**Key Insight**
The key insight is to treat each layer as a ring and rotate it by moving elements in a counter-clockwise direction. This allows us to efficiently rotate each layer without having to shift all elements in the entire grid.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 214 ms (Beats 10.77%) |
| 💾 Memory | 19.5 MB (Beats 88.42%) |
| 📅 Solved | 2026-05-09 |
| 💻 Language | Python |